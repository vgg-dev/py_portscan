<p align="center">
<img src="py_scanner_icon.png" alt="Port Scanner" width="200" height="200"/>
</p>

# py_portscan

A lightweight Python TCP port scanner that checks a target host across a user-defined port range.

## Features

- Scans a specific TCP port range on an IP or hostname.
- Validates ports (`1-65535`) and rejects invalid ranges.
- Supports configurable socket timeout with `--timeout`.
- Prints a summary of scanned and open ports.
- Handles Ctrl+C interruption cleanly.

## Usage

1. Clone the repository:

```bash
git clone https://github.com/vgg-dev/py_portscan.git
```

2. Navigate to the project directory:

```bash
cd py_portscan
```

3. Run the scanner:

```bash
python py_portscan.py <target> <start_port> <end_port> [--timeout 1.0]
```

## Example

Scan ports `1-100` on `example.com` using a `0.5s` timeout:

```bash
python py_portscan.py example.com 1 100 --timeout 0.5
```

## Notes

- Use only on systems/networks where you have explicit authorization.
