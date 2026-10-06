from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime


packet_count = 0


def packet_callback(packet):
    global packet_count
    packet_count += 1

    print("\n" + "=" * 70)
    print(f"Packet #{packet_count}")
    print("Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    if IP not in packet:
        print("Protocol: Non-IP")
        return

    source_ip = packet[IP].src
    destination_ip = packet[IP].dst

    print("Source IP       :", source_ip)
    print("Destination IP  :", destination_ip)

    # Identify protocol
    if TCP in packet:
        protocol = "TCP"
        source_port = packet[TCP].sport
        destination_port = packet[TCP].dport

        print("Protocol        :", protocol)
        print("Source Port     :", source_port)
        print("Destination Port:", destination_port)

    elif UDP in packet:
        protocol = "UDP"
        source_port = packet[UDP].sport
        destination_port = packet[UDP].dport

        print("Protocol        :", protocol)
        print("Source Port     :", source_port)
        print("Destination Port:", destination_port)

    elif ICMP in packet:
        print("Protocol        : ICMP")

    else:
        print("Protocol        :", packet[IP].proto)

    # Display payload
    if Raw in packet:
        payload = bytes(packet[Raw].load)

        print("Payload Length  :", len(payload), "bytes")

        # Show only a small portion of payload
        preview = payload[:100]

        try:
            readable_payload = preview.decode(
                "utf-8",
                errors="replace"
            )
            print("Payload Preview :", readable_payload)
        except Exception:
            print("Payload Preview : [Binary data]")
    else:
        print("Payload         : None")


def main():
    print("\n" + "=" * 70)
    print("              BASIC NETWORK SNIFFER")
    print("=" * 70)
    print("Status: Capturing network traffic...")
    print("Press CTRL+C to stop.")
    print("=" * 70)

    try:
        sniff(
            prn=packet_callback,
            store=False
        )

    except KeyboardInterrupt:
        print("\n\n" + "=" * 70)
        print("Packet capture stopped.")
        print("Total packets captured:", packet_count)
        print("=" * 70)

    except PermissionError:
        print("\nPermission denied.")
        print("Please run VS Code as Administrator.")

    except Exception as error:
        print("\nAn error occurred:")
        print(error)


if __name__ == "__main__":
    main()
