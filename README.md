# PythonARPScanner
Here's a `README.md` file for your ARP scanning script:

```markdown
# ARP Network Scanner

This Python script scans all active network interfaces on your system and performs an ARP scan to discover devices within the reachable subnets. It outputs the IP and MAC addresses of all active devices on the network.

## Features

- Automatically detects all active network interfaces and their associated subnets.
- Performs ARP scanning to discover devices within the subnet.
- Displays the IP and MAC addresses of all reachable devices.
- Works on any Linux-based system.
- Easy to use, with minimal configuration required.

## Requirements

- Python 3.x
- The following Python libraries:
  - `scapy`
  - `netifaces`
- Root (or `sudo`) privileges to allow raw packet handling.

## Installation

1. Clone this repository or download the script directly.
2. Install the required dependencies using pip:
   ```bash
   pip install scapy netifaces
   ```

3. Run the script with `sudo` to enable raw packet handling:
   ```bash
   sudo python3 scanner.py
   ```

## Usage

1. Simply run the script:
   ```bash
   sudo python3 scanner.py
   ```

2. The script will:
   - Detect all active network interfaces.
   - Determine the subnet associated with each interface.
   - Perform an ARP scan on each subnet to identify active devices.

3. Example output:
   ```
   Scanning network 192.168.1.0/24 on interface eth0...
   IP : 192.168.1.1    MAC : 00:11:22:33:44:55
   IP : 192.168.1.100  MAC : aa:bb:cc:dd:ee:ff
   ```

4. If there are no active interfaces or subnets, the script will notify you:
   ```
   No active network interfaces found!
   ```

## Troubleshooting

- **Permission Denied:**
  - Ensure you run the script with `sudo` to allow raw packet handling.
  - Example:
    ```bash
    sudo python3 scanner.py
    ```

- **No Active Interfaces:**
  - Ensure your network interfaces are active and have assigned IP addresses.
  - Use `ip link show` to check the status of your interfaces.

- **Missing Dependencies:**
  - Ensure the required libraries (`scapy`, `netifaces`) are installed:
    ```bash
    pip install scapy netifaces
    ```

## Disclaimer

This script is intended for educational purposes or for legitimate network administration tasks on networks you own or manage. Unauthorized use of this script to scan third-party networks may violate privacy laws and is strictly prohibited.

### How to Use This File
1. Save the text above in a file named `README.md`.
2. Place it in the root directory of your project alongside the script.
3. If this is part of a repository, include the relevant repository link in the instructions.

Let me know if you need further refinements!
