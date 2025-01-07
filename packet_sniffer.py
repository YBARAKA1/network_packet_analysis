from scapy.all import sniff

def capture_packets(interface="wlan0", count=100):
    print(f"Sniffing {count} packets on interface {interface}...")
    packets = sniff(iface=interface, count=count)
    return packets
