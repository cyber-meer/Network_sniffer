Basic Network Sniffer:

A Python-based network sniffer developed using Scapy to capture and analyze network packets in real time.

 Project Description:

The Basic Network Sniffer is a cybersecurity project developed using Python and the Scapy library. The main purpose of this project is to capture network packets and display important information about network traffic. The program captures packets in real time and provides details such as source IP address, destination IP address, network protocol, source port, destination port, packet payload, packet number, and timestamp.

 Project Objective:

The objective of this project is to understand how network communication works at the packet level and gain practical experience in network traffic analysis. This project also helps in understanding IP addresses, network protocols, ports, and packet data using Python.

 Technologies Used:

This project was developed using Python 3 and the Scapy library. Visual Studio Code was used as the development environment, and the project was tested on Windows.

 Features:

The network sniffer captures network packets in real time and identifies commonly used protocols such as TCP, UDP, and ICMP. It displays the source and destination IP addresses, source and destination ports, packet number, timestamp, payload length, and payload information when available. The program also includes basic error handling and allows the user to stop packet capturing using CTRL+C.

 Installation:

Before running the project, Python should be installed on the system. The Scapy library can be installed using the following command:

```bash
pip install scapy

If pip does not work, the following command can be used:
python -m pip install scapy

How to Run:
Open the project folder in Visual Studio Code and open the terminal. Run the following command:
python network_sniffer.py
After running the program, the network sniffer will start capturing packets in real time. To stop the packet capture, press CTRL+C in the terminal.

Sample Output:
The program displays information about each captured packet, including its packet number, timestamp, source IP address, destination IP address, protocol, source port, destination port, payload length, and payload information. For example, a captured TCP packet may display a source IP address, destination IP address, TCP protocol, source and destination ports, and the size of the captured payload.
Learning Outcomes:
Through this project, I gained practical experience in Python programming, Scapy, network packet capturing, IP addressing, TCP and UDP communication, network ports, ICMP, and basic network traffic analysis. I also learned how packet information can be captured and and displayed in real time for cybersecurity and network monitoring purposes.

Cybersecurity Relevance:
Network packet analysis is an important concept in cybersecurity and network administration. Understanding network traffic helps security professionals analyze communication between devices, troubleshoot network issues, understand protocols, and identify unusual or suspicious network activity.

Disclaimer:
This project was developed for educational and cybersecurity learning purposes only. Network traffic should only be captured and analyzed on systems or networks where proper authorization and permission have been provided. This project should not be used to monitor or intercept network traffic without permission.
Author:
Cyber meer
