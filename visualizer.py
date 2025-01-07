import matplotlib.pyplot as plt
from collections import Counter

def visualize_data(analyzed_data):
    print("Visualizing data...")
    protocols = [data["protocol"] for data in analyzed_data]
    protocol_counts = Counter(protocols)
    
    plt.bar(protocol_counts.keys(), protocol_counts.values())
    plt.xlabel("Protocol")
    plt.ylabel("Count")
    plt.title("Protocol Distribution")
    plt.show()
