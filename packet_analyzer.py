# packet_analyzer.py
from datetime import datetime

def analyze_packets(packets):
    analyzed = []
    for packet in packets:
        try:
            # Extract timestamp
            timestamp = datetime.fromtimestamp(packet.time).strftime('%Y-%m-%d %H:%M:%S')
            
            # Extract source and destination
            src = packet.getlayer(1).src if packet.haslayer(1) else "Unknown"
            dst = packet.getlayer(1).dst if packet.haslayer(1) else "Unknown"
            
            # Extract protocol
            protocol = packet.getlayer(2).name if packet.haslayer(2) else "Other"
            
            # Extract details
            if packet.haslayer("HTTP"):
                details = "HTTP Packet"
            elif packet.haslayer("DNS"):
                details = f"DNS Query: {packet.getlayer('DNS').qd.qname}"
            else:
                details = "No specific details"
            
            analyzed.append({
                "timestamp": timestamp,
                "src": src,
                "dst": dst,
                "protocol": protocol,
                "details": details
            })
        except Exception as e:
            print(f"Error analyzing packet: {e}")
    return analyzed
