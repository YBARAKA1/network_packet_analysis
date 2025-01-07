import matplotlib.pyplot as plt
from collections import Counter

def visualize_data(data):
    protocols = [packet["protocol"] for packet in data]
    protocol_counts = Counter(protocols)

    plt.bar(protocol_counts.keys(), protocol_counts.values())
    plt.title("Protocol Distribution")
    plt.xlabel("Protocol")
    plt.ylabel("Count")
    plt.show()
