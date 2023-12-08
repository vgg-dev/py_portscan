<p align="center">
<img src="py_scanner_icon.png" alt="Port Scanner" width="200" height="200"/>
</p>

# py_portscan

# Port Scanner

This Python script is a simple port scanner that checks for open ports within a specified range on a given target (IP address or hostname).

## Features

- Scans a range of ports on a specified target to check for open ports.
- Provides information about open ports on the target machine.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/vgg-dev/py_portscan.git
    ```

2. Navigate to the project directory:

    ```bash
    cd py_portscan
    ```

3. Run the port scanner with the following command:

    ```bash
    python py_portscan.py <target> <start_port> <end_port>
    ```

    Replace `<target>` with the IP address or hostname to scan, `<start_port>` with the starting port number, and `<end_port>` with the ending port number.

## Example

Scan ports 1 to 100 on `example.com`:

```bash
python py_portscan.py example.com 1 100
```

### Notes

- **Be Cautious:** It's important to use this tool responsibly and ethically. Unauthorized port scanning may violate network policies or laws.
