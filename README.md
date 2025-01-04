**Name:** HARNIL MODI

**Company:** CODTECH IT SOLUTIONS

**ID:** CT08DAN

**Domain:** Cyber Security & Ethical Hacking

**Duration:** December to January 2025

**Mentor:** Neela Santhosh Kumar

## **Overview of the Project :-** 

### Project:- PENETRATION TESTING TOOLKIT

## Objective:

The goal of this project is to develop a Python-based modular penetration testing toolkit with various modules for conducting penetration tests. Each module serves a distinct function to help security professionals evaluate vulnerabilities in a network or system. The modules include a port scanner, brute force SSH login tester, web application vulnerability scanner, packet sniffer, and banner grabber.

## Key Features:

1.Port Scanner:

Scans specified ports on a target system to identify open ports.

Uses a socket connection to check if a port is open or closed.

Supports user input for target IP and list of ports to scan.

2.Brute Force SSH Login Tester:

Attempts to login to a target via SSH using a wordlist.

Multi-threaded to speed up brute-forcing.

Supports user-provided username and password wordlist file.

3.Web Application Vulnerability Scanner:

Identifies SQL Injection and Cross-Site Scripting (XSS) vulnerabilities in web forms.

Retrieves all forms from the target URL and submits malicious payloads to test for vulnerabilities.

Reports the presence of SQL Injection or XSS vulnerabilities.

4.Packet Sniffer:

Captures network packets in real time using the Scapy library.

Displays packet summaries for analysis.

User-defined number of packets to capture.

5.Banner Grabber:

Connects to a specific port on a target system to capture service banners.

Useful for identifying the software and version running on a specific port.

Logs the banner if found.

## Technologies Used:
Python: Primary programming language.

## Libraries:
socket for creating network connections and handling TCP/IP communications.

paramiko for SSH brute-forcing.

requests & BeautifulSoup for interacting with and parsing HTML forms from web applications.

scapy for sniffing network packets.

Threading: Used in the brute force module for concurrent password attempts.

## Programming Language:

Python 3.x: The toolkit is developed using Python as it is versatile and supports numerous libraries and tools that are essential for penetration testing tasks.

## Additional Download Commands:
To run and install the required libraries, use the following commands in the terminal:

-pip install paramiko requests beautifulsoup4 scapy

-pip install lxml

## How It Works:
1.Port Scanner:

The script asks for a target IP and a list of ports.

It attempts to connect to each port in the list and checks whether the connection is successful.

If the connection is successful, the port is considered "open" and is logged.

2.SSH Brute Force:

The user inputs the target IP, SSH username, and the path to a password wordlist.

The script attempts to brute-force the SSH login using each password in the wordlist.

If a successful login is found, it logs the username and password combination.

3.Web Vulnerability Scanner (SQL Injection and XSS):

The user inputs the target URL.

The script extracts all forms from the page and tests each form for SQL Injection and XSS vulnerabilities.

It sends crafted payloads to the form fields and analyzes the response for signs of vulnerabilities.

4.Packet Sniffer:

The user inputs the number of packets to capture.

The script uses Scapy to sniff network traffic and prints out summaries of each captured packet.

This is useful for monitoring traffic for signs of malicious activity.

5.Banner Grabber:

The user provides the target IP and the port to grab a banner from.

The script attempts to establish a TCP connection to the target and port.

If successful, it logs and displays the service banner (e.g., HTTP, FTP) that identifies the software and version running on that port.

![Screenshot 2025-01-04 182317](https://github.com/user-attachments/assets/5808f6f9-e1cd-495f-8f03-9034f5b93284)


