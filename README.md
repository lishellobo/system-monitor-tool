# System Monitor Tool

## Overview

The System Monitor Tool is a Python-based application that provides real-time monitoring of various system metrics, such as CPU usage, memory usage, disk usage, network activity, and running processes. It features a simple graphical user interface (GUI) created using `tkinter` and `matplotlib`.

## Features

- **CPU Usage**: Monitor the current CPU usage.
- **Memory Usage**: Check the current memory usage.
- **Disk Usage**: View the current disk usage.
- **Network Usage**: See the network activity including bytes sent and received.
- **Process List**: Display a list of running processes with PID, name, and user.
- **System Uptime**: Show how long the system has been running.

## Requirements

- Python 3.x
- `psutil` library
- `tkinter` library (usually included with Python installations)
- `matplotlib` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/lishellobo/system-monitor-tool.git
    cd system-monitor-tool
    ```

2. Install the required Python packages:
    ```bash
    pip install psutil matplotlib
    ```

## Usage

Run the script to start the system monitor tool:
```bash
python system_monitor_gui.py
