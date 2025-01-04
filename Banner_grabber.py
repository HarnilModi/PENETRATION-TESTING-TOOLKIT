import socket
import logging
import sys

# Set up logging
logging.basicConfig(level=logging.INFO)

def banner_grabbing(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((target, port))
        banner = sock.recv(1024).decode('utf-8')
        logging.info(f"Banner for {target}:{port}: {banner}")
        sock.close()
    except socket.error as e:
        logging.error(f"Could not grab banner for {target}:{port} - {e}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        target = input("Enter target IP: ")
        port = int(input("Enter port to grab banner from: "))
        banner_grabbing(target, port)
    except ValueError:
        logging.error("Invalid port input. Please enter a valid number.")
        sys.exit(1)
