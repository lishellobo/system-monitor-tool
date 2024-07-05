#!/usr/bin/env python3
import psutil
import os
from datetime import datetime
import tkinter as tk
from tkinter import ttk

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return disk.percent

def get_network_usage():
    net_io = psutil.net_io_counters()
    return f"Bytes Sent: {net_io.bytes_sent}, Bytes Received: {net_io.bytes_recv}"

def get_process_list():
    process_list = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        process_list.append(proc.info)
    return process_list

def get_uptime():
    boot_time_timestamp = psutil.boot_time()
    boot_time = datetime.fromtimestamp(boot_time_timestamp)
    current_time = datetime.now()
    uptime = current_time - boot_time
    return str(uptime).split('.')[0]  # Remove microseconds

def clear_screen():
    os.system('clear')

def update_gui():
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()
    disk_usage = get_disk_usage()
    network_usage = get_network_usage()
    uptime = get_uptime()

    cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
    memory_label.config(text=f"Memory Usage: {memory_usage}%")
    disk_label.config(text=f"Disk Usage: {disk_usage}%")
    network_label.config(text=f"Network: {network_usage}")
    uptime_label.config(text=f"Uptime: {uptime}")

    # Update process list
    for item in process_tree.get_children():
        process_tree.delete(item)
    for proc in get_process_list()[:10]:  # Display only first 10 processes for brevity
        process_tree.insert("", "end", values=(proc['pid'], proc['name'], proc['username']))

    root.after(1000, update_gui)

# Create main window
root = tk.Tk()
root.title("System Monitor")
root.configure(bg='black')

# Create labels
cpu_label = tk.Label(root, text="", fg='white', bg='black', font=("Helvetica", 10))
cpu_label.pack()
memory_label = tk.Label(root, text="", fg='white', bg='black', font=("Helvetica", 10))
memory_label.pack()
disk_label = tk.Label(root, text="", fg='white', bg='black', font=("Helvetica", 10))
disk_label.pack()
network_label = tk.Label(root, text="", fg='white', bg='black', font=("Helvetica", 10))
network_label.pack()
uptime_label = tk.Label(root, text="", fg='white', bg='black', font=("Helvetica", 10))
uptime_label.pack()

# Create process list
columns = ("PID", "Name", "User")
process_tree = ttk.Treeview(root, columns=columns, show="headings", style="mystyle.Treeview")
for col in columns:
    process_tree.heading(col, text=col)
process_tree.pack()

# Apply styles to the Treeview
style = ttk.Style()
style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Helvetica', 8))  # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Helvetica', 10, 'bold'))  # Modify the font of the headings

# Start updating the GUI
update_gui()

# Run the application
root.mainloop()

