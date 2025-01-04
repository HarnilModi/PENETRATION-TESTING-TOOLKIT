from scapy.all import sniff
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def packet_sniffer(packet_count):
    def process_packet(packet):
        logging.info(packet.summary())

    logging.info(f"Sniffing {packet_count} packets...")
    sniff(prn=process_packet, count=packet_count)

if __name__ == "__main__":
    try:
        packet_count = int(input("Enter the number of packets to capture: "))
        packet_sniffer(packet_count)
    except ValueError:
        logging.error("Invalid number of packets. Please enter a valid number.")
