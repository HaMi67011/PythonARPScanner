from scapy.layers.l2 import Ether, ARP
from scapy.sendrecv import srp
import netifaces as ni

def get_all_interfaces_subnets():
    """Get all active network interfaces and their subnets."""
    subnets = []
    interfaces = ni.interfaces()
    for iface in interfaces:
        try:
            addr = ni.ifaddresses(iface)[ni.AF_INET][0]
            ip = addr['addr']
            netmask = addr['netmask']
            subnet = f"{ip}/{netmask_to_cidr(netmask)}"
            subnets.append((iface, subnet))
        except (KeyError, ValueError):
            # Skip interfaces without an IPv4 address
            continue
    return subnets

def netmask_to_cidr(netmask):
    """Convert a netmask to CIDR notation."""
    return sum(bin(int(octet)).count('1') for octet in netmask.split('.'))

def scan_network(iface, ip_range):
    """Scan a given IP range for active devices."""
    print(f"Scanning network {ip_range} on interface {iface}...")
    broadcast = "FF:FF:FF:FF:FF:FF"
    my_arp_layer = ARP(pdst=ip_range)
    ether_layer = Ether(dst=broadcast)
    packet = ether_layer / my_arp_layer

    ans, unans = srp(packet, iface=iface, timeout=2, verbose=False)
    for snd, rcv in ans:
        ip = rcv[ARP].psrc
        mac = rcv[Ether].src
        print(f"IP : {ip}\tMAC : {mac}")

if __name__ == "__main__":
    all_subnets = get_all_interfaces_subnets()
    if not all_subnets:
        print("No active network interfaces found!")
    else:
        for iface, subnet in all_subnets:
            try:
                scan_network(iface, subnet)
            except PermissionError:
                print(f"Permission denied! Please run as root to scan {iface}.")
