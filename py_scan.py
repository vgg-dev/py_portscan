import socket
import argparse

def port_scan(target, start_port, end_port):
    print(f"Scanning {target} for open ports...\n")
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Invalid target or unable to resolve target IP.")
        return

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Simple Port Scanner',
        epilog='Usage: python port_scanner.py target start_port end_port'
    )
    parser.add_argument('target', help='Target IP or hostname')
    parser.add_argument('start_port', type=int, help='Starting port number')
    parser.add_argument('end_port', type=int, help='Ending port number')
    

    args = parser.parse_args()

    port_scan(args.target, args.start_port, args.end_port)
