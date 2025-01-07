from scapy.layers.inet import IP, TCP, UDP

def analyze_packets(packets):
    print("Analyzing packets...")
    summary = []
    for packet in packets:
        if IP in packet:
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            proto = packet[IP].proto
            summary.append({"src": src_ip, "dst": dst_ip, "protocol": proto})
    print("Analysis complete.")
    return summary
