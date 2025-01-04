import socket
import sys
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def port_scanner(target, ports):
    open_ports = []
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except socket.error as e:
            logging.error(f"Error scanning port {port}: {e}")
    return open_ports

if __name__ == "__main__":
    try:
        target = input("Enter target IP: ")
        ports = list(map(int, input("Enter ports to scan (comma-separated): ").split(',')))
        open_ports = port_scanner(target, ports)
        logging.info(f"Open ports on {target}: {open_ports}")
    except ValueError:
        logging.error("Invalid input for ports. Please enter valid numbers.")
        sys.exit(1)
