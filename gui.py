import tkinter as tk
from tkinter import ttk, messagebox
from packet_sniffer import capture_packets
from packet_analyzer import analyze_packets

def start_analysis(interface, packet_count):
    try:
        packets = capture_packets(interface, packet_count)
        analyzed_packets = analyze_packets(packets)
        display_packets(analyzed_packets)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def display_packets(analyzed_packets):
    # Clear existing rows
    for row in tree.get_children():
        tree.delete(row)


    for i, packet in enumerate(analyzed_packets):
        tree.insert("", "end", iid=i, values=(
            i + 1,
            packet.get("timestamp", "Unknown"),
            packet.get("src", "Unknown"),
            packet.get("dst", "Unknown"),
            packet.get("protocol", "Unknown"),
            packet.get("details", "Unknown")
    ))


    def on_packet_select(event):
        selected = tree.selection()
        if selected:
            packet_id = int(selected[0])
            packet = analyzed_packets[packet_id]
            details_text.delete(1.0, tk.END)
            details_text.insert(tk.END, f"Packet #{packet_id + 1}\n\n")
            details_text.insert(tk.END, f"Timestamp: {packet['timestamp']}\n")
            details_text.insert(tk.END, f"Source IP: {packet['src']}\n")
            details_text.insert(tk.END, f"Destination IP: {packet['dst']}\n")
            details_text.insert(tk.END, f"Protocol: {packet['protocol']}\n")
            details_text.insert(tk.END, f"Details: {packet['details']}\n")

    tree.bind("<ButtonRelease-1>", on_packet_select)

# Create GUI
root = tk.Tk()
root.title("Network Packet Analyzer")

frame = tk.Frame(root)
frame.pack(pady=10, padx=10)

# Input fields
interface_label = tk.Label(frame, text="Network Interface:")
interface_label.grid(row=0, column=0, sticky="w")
interface_entry = tk.Entry(frame)
interface_entry.grid(row=0, column=1)

packet_count_label = tk.Label(frame, text="Packet Count:")
packet_count_label.grid(row=1, column=0, sticky="w")
packet_count_entry = tk.Entry(frame)
packet_count_entry.grid(row=1, column=1)

# Start Button
start_button = tk.Button(frame, text="Start Analysis", command=lambda: start_analysis(interface_entry.get(), int(packet_count_entry.get())))
start_button.grid(row=2, columnspan=2, pady=5)

# Table for displaying packets
tree = ttk.Treeview(root, columns=("#", "Timestamp", "Source", "Destination", "Protocol", "Details"), show="headings")
tree.heading("#", text="#")
tree.heading("Timestamp", text="Timestamp")
tree.heading("Source", text="Source")
tree.heading("Destination", text="Destination")
tree.heading("Protocol", text="Protocol")
tree.heading("Details", text="Details")

tree.column("#", width=40, anchor="center")
tree.column("Timestamp", width=150)
tree.column("Source", width=120)
tree.column("Destination", width=120)
tree.column("Protocol", width=80)
tree.column("Details", width=300)

tree.pack(pady=10, padx=10, fill="x")

# Detailed packet view
details_label = tk.Label(root, text="Packet Details:")
details_label.pack(anchor="w", padx=10)

details_text = tk.Text(root, height=10, wrap="word")
details_text.pack(padx=10, pady=5, fill="x")

root.mainloop()
