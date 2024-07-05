#!/usr/bin/env python3
import psutil
import os
from datetime import datetime
import time

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

def main():
    while True:
        clear_screen()
        print(f"System Monitor - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*40)
        print(f"CPU Usage: {get_cpu_usage()}%")
        print(f"Memory Usage: {get_memory_usage()}%")
        print(f"Disk Usage: {get_disk_usage()}%")
        print(f"Network Usage: {get_network_usage()}")
        print(f"System Uptime: {get_uptime()}")
        print("="*40)
        print("Process List:")
        for proc in get_process_list()[:10]:  # Display only first 10 processes for brevity
            print(f"PID: {proc['pid']}, Name: {proc['name']}, User: {proc['username']}")
        print("="*40)
        time.sleep(1)  # Refresh every second

if __name__ == "__main__":
    main()
