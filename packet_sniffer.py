from scapy.all import sniff

def capture_packets(interface):
    print(f"Starting packet capture on {interface}...")
    packets = sniff(iface=interface, count=100)  # Capture 100 packets
    print(f"Captured {len(packets)} packets.")
    return packets
