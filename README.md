# Quick-Recon
Quick Recon is a Python tool that provides quick access to system information like user details, OS version, RAM, CPU stats, private IP, and SSD usage. It's useful for IT professionals and cybersecurity enthusiasts for system monitoring, troubleshooting, and audits.

## Features

- **User Information**: Displays the current user’s name.
- **System Information**: Retrieves and displays detailed information about the system type, version, release, machine type, and processor.
- **RAM Information**: Provides total, available, and used RAM, as well as the percentage of RAM usage.
- **Private IP Address**: Displays the local IP address of the machine.
- **CPU Information**: Shows CPU usage, number of physical cores, and logical cores.
- **SSD Usage**: Displays the current usage of the SSD (if available) on the system.

## Installation

### Prerequisites

- Python 3.6 or higher installed on your system.
- Required Python libraries: `psutil`, `getpass`, `socket`, `platform`.

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/k1r1n-p/Quick-Recon.git
2. **Install the dependencies:
   ```bash
   pip install psutil
3. **Run the Tool**:
   ```bash
   python quick_recon.py
Now you should be able to use the tool to gather system information!

## Usage 
Once the tool is running, you’ll see a menu with options to retrieve user, system, RAM, IP, CPU, and SSD information. Just choose the appropriate option by entering the number corresponding to the information you want.

## License 
This project is licensed under the Apache License 2.0 - see the LICENSE file for details.
