import socket
import argparse

def is_port_open(host, port):
    """
    Attempts to establish a connection to the given host on the specified port.
    Returns True if the connection is successful (indicating the port is open), False otherwise.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Timeout after 1 second
            s.connect((host, port))
            return True
    except (socket.timeout, ConnectionRefusedError):
        return False
    except OSError as e:
        print(f"Error scanning port {port}: {e}")
        return False

def scan_ports(host, start_port, end_port):
    """
    Scans a range of ports on the given host and reports which are open.
    """
    open_ports = []
    for port in range(start_port, end_port + 1):
        if is_port_open(host, port):
            open_ports.append(port)
            print(f"Port {port} is **OPEN**")
        else:
            print(f"Port {port} is closed")
    return open_ports

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simple Port Scanner')
    parser.add_argument('-H', '--host', required=True, help='Target host to scan')
    parser.add_argument('-s', '--start', type=int, default=1, help='Starting port number (default: 1)')
    parser.add_argument('-e', '--end', type=int, default=1024, help='Ending port number (default: 1024)')
    args = parser.parse_args()

    print(f"Scanning {args.host} from port {args.start} to {args.end}...")
    open_ports = scan_ports(args.host, args.start, args.end)
    print(f"\nScan Complete. Found {len(open_ports)} open port(s).")
