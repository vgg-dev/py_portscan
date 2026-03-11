<p align="center">
  <img src="py_scanner_icon.png" alt="py_portscan" width="180" height="180" />
</p>

<h1 align="center">py_portscan</h1>
<p align="center">A tiny <b>TCP connect</b> port scanner in Python (sequential).</p>

<p align="center">
  <a href="https://github.com/vgg-dev/py_portscan/releases">
    <img alt="release" src="https://img.shields.io/github/v/release/vgg-dev/py_portscan?sort=semver" />
  </a>
  <a href="LICENSE">
    <img alt="license" src="https://img.shields.io/github/license/vgg-dev/py_portscan" />
  </a>
  <img alt="python" src="https://img.shields.io/badge/python-3.x-blue" />
  <a href="https://github.com/vgg-dev/py_portscan/commits/main">
    <img alt="last commit" src="https://img.shields.io/github/last-commit/vgg-dev/py_portscan" />
  </a>
</p>

> [!IMPORTANT]
> Use this tool only on systems/networks where you have **explicit authorization**.

## ✨ Features

- 🎯 Scan a host across a TCP port range
- ✅ Validates port inputs (`1-65535`) and range order
- ⏱️ Configurable socket timeout via `--timeout`
- 🧾 Prints open ports + a scan summary
- 🛑 Handles Ctrl+C cleanly

## ⚡ Quickstart

```bash
python py_portscan.py example.com 1 100 --timeout 0.5
```

## 📦 Install

Clone the repo:

```bash
git clone https://github.com/vgg-dev/py_portscan.git
cd py_portscan
```

Requirements:

- Python 3.x

## 🧪 Usage

```bash
python py_portscan.py <target> <start_port> <end_port> [--timeout 1.0]
```

Examples:

```bash
# Scan common web ports
python py_portscan.py example.com 80 443 --timeout 0.5

# Scan a small range on an IP
python py_portscan.py 192.168.1.10 1 1024 --timeout 0.2
```

## 🧠 How it works

- Resolves the target with `socket.gethostbyname()`
- Iterates ports from `start_port` to `end_port`
- Attempts a TCP connection (`connect_ex`) with the configured timeout
- Reports ports where the connection succeeds

## ⏳ Performance notes

This scanner is **sequential**, so large ranges can take a while:

- Rough estimate: `ports_scanned * timeout` (worst case)
- Keep ranges tight when possible (e.g., `1-1024` or a few common ports)
- Lower `--timeout` for faster scans (may increase false negatives)

## 🧯 Troubleshooting

- **Name resolution failed**: try an IP instead of a hostname.
- **No open ports found**: the host may be filtered/firewalled or ports may be closed.
- **Slow scan**: reduce the port range and/or lower `--timeout`.

## 📄 License

See `LICENSE`.
