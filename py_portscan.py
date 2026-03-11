import argparse
import socket


def validate_port(value):
    port = int(value)
    if port < 1 or port > 65535:
        raise argparse.ArgumentTypeError("Port must be between 1 and 65535.")
    return port


def port_scan(target, start_port, end_port, timeout):
    print(f"Scanning {target} ({start_port}-{end_port}) for open ports...\n")
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Invalid target or unable to resolve target IP.")
        return

    open_ports = []
    try:
        for port in range(start_port, end_port + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(timeout)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    print(f"Port {port} is open")
                    open_ports.append(port)
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
    finally:
        total_ports = end_port - start_port + 1
        print(f"\nScan complete. Checked {total_ports} ports on {ip}.")
        if open_ports:
            print(f"Open ports found ({len(open_ports)}): {', '.join(map(str, open_ports))}")
        else:
            print("No open ports found in the specified range.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Simple TCP Port Scanner",
        epilog="Usage: python py_portscan.py target start_port end_port [--timeout 1.0]",
    )
    parser.add_argument("target", help="Target IP or hostname")
    parser.add_argument("start_port", type=validate_port, help="Starting port number (1-65535)")
    parser.add_argument("end_port", type=validate_port, help="Ending port number (1-65535)")
    parser.add_argument(
        "--timeout",
        type=float,
        default=1.0,
        help="Socket timeout in seconds (default: 1.0)",
    )

    args = parser.parse_args()
    if args.start_port > args.end_port:
        parser.error("start_port must be less than or equal to end_port.")
    if args.timeout <= 0:
        parser.error("--timeout must be a positive number.")

    port_scan(args.target, args.start_port, args.end_port, args.timeout)
