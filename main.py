from packet_sniffer import capture_packets
from packet_analyzer import analyze_packets
from visualizer import visualize_data

if __name__ == "__main__":
    packets = capture_packets(interface="wlan0")  
    analyzed_data = analyze_packets(packets)
    visualize_data(analyzed_data)
