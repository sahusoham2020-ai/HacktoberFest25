#!/usr/bin/env python3
"""
Real-Time System Monitor
A command-line system monitor displaying CPU, memory, disk, and network usage in real-time.
"""

import psutil
import time
import os
import sys
from datetime import datetime

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_size(bytes):
    """Convert bytes to human readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024.0

def get_bar(percentage, width=50):
    """Create a visual progress bar."""
    filled = int(width * percentage / 100)
    bar = '█' * filled + '░' * (width - filled)
    return f"[{bar}] {percentage:.1f}%"

def get_cpu_info():
    """Get CPU usage information."""
    cpu_percent = psutil.cpu_percent(interval=0.1)
    cpu_count = psutil.cpu_count(logical=False)
    cpu_count_logical = psutil.cpu_count(logical=True)
    cpu_freq = psutil.cpu_freq()
    
    return {
        'percent': cpu_percent,
        'cores': cpu_count,
        'threads': cpu_count_logical,
        'freq_current': cpu_freq.current if cpu_freq else 0,
        'freq_max': cpu_freq.max if cpu_freq else 0,
        'per_cpu': psutil.cpu_percent(interval=0.1, percpu=True)
    }

def get_memory_info():
    """Get memory usage information."""
    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    
    return {
        'total': mem.total,
        'available': mem.available,
        'used': mem.used,
        'percent': mem.percent,
        'swap_total': swap.total,
        'swap_used': swap.used,
        'swap_percent': swap.percent
    }

def get_disk_info():
    """Get disk usage information."""
    partitions = psutil.disk_partitions()
    disk_info = []
    
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            disk_info.append({
                'device': partition.device,
                'mountpoint': partition.mountpoint,
                'fstype': partition.fstype,
                'total': usage.total,
                'used': usage.used,
                'free': usage.free,
                'percent': usage.percent
            })
        except PermissionError:
            continue
    
    return disk_info

def get_network_info():
    """Get network I/O information."""
    net_io = psutil.net_io_counters()
    
    return {
        'bytes_sent': net_io.bytes_sent,
        'bytes_recv': net_io.bytes_recv,
        'packets_sent': net_io.packets_sent,
        'packets_recv': net_io.packets_recv
    }

def get_top_processes(limit=5):
    """Get top processes by CPU and memory usage."""
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    
    # Sort by CPU usage
    top_cpu = sorted(processes, key=lambda x: x['cpu_percent'] or 0, reverse=True)[:limit]
    # Sort by memory usage
    top_mem = sorted(processes, key=lambda x: x['memory_percent'] or 0, reverse=True)[:limit]
    
    return top_cpu, top_mem

def display_header():
    """Display the header."""
    print("=" * 80)
    print(f"{'SYSTEM MONITOR':^80}")
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S'):^80}")
    print("=" * 80)

def display_cpu(cpu_info):
    """Display CPU information."""
    print("\n📊 CPU USAGE")
    print("-" * 80)
    print(f"Overall: {get_bar(cpu_info['percent'], 60)}")
    print(f"Cores: {cpu_info['cores']} | Threads: {cpu_info['threads']}")
    
    if cpu_info['freq_current']:
        print(f"Frequency: {cpu_info['freq_current']:.0f} MHz / {cpu_info['freq_max']:.0f} MHz")
    
    print("\nPer-Core Usage:")
    for i, percent in enumerate(cpu_info['per_cpu']):
        print(f"  Core {i}: {get_bar(percent, 50)}")

def display_memory(mem_info):
    """Display memory information."""
    print("\n💾 MEMORY USAGE")
    print("-" * 80)
    print(f"RAM: {get_bar(mem_info['percent'], 60)}")
    print(f"Used: {get_size(mem_info['used'])} / Total: {get_size(mem_info['total'])}")
    print(f"Available: {get_size(mem_info['available'])}")
    
    if mem_info['swap_total'] > 0:
        print(f"\nSwap: {get_bar(mem_info['swap_percent'], 60)}")
        print(f"Used: {get_size(mem_info['swap_used'])} / Total: {get_size(mem_info['swap_total'])}")

def display_disk(disk_info):
    """Display disk information."""
    print("\n💿 DISK USAGE")
    print("-" * 80)
    for disk in disk_info:
        print(f"\n{disk['device']} ({disk['mountpoint']}) - {disk['fstype']}")
        print(f"  {get_bar(disk['percent'], 55)}")
        print(f"  Used: {get_size(disk['used'])} / Total: {get_size(disk['total'])}")
        print(f"  Free: {get_size(disk['free'])}")

def display_network(net_info, prev_net_info=None):
    """Display network information."""
    print("\n🌐 NETWORK I/O")
    print("-" * 80)
    print(f"Sent: {get_size(net_info['bytes_sent'])} | Received: {get_size(net_info['bytes_recv'])}")
    
    if prev_net_info:
        sent_rate = net_info['bytes_sent'] - prev_net_info['bytes_sent']
        recv_rate = net_info['bytes_recv'] - prev_net_info['bytes_recv']
        print(f"Rate: ↑ {get_size(sent_rate)}/s | ↓ {get_size(recv_rate)}/s")

def display_processes(top_cpu, top_mem):
    """Display top processes."""
    print("\n⚡ TOP PROCESSES")
    print("-" * 80)
    
    print("By CPU Usage:")
    print(f"  {'PID':<8} {'Name':<30} {'CPU %':<10}")
    for proc in top_cpu:
        cpu_val = proc['cpu_percent'] if proc['cpu_percent'] is not None else 0.0
        print(f"  {proc['pid']:<8} {proc['name'][:29]:<30} {cpu_val:.1f}%")
    
    print("\nBy Memory Usage:")
    print(f"  {'PID':<8} {'Name':<30} {'MEM %':<10}")
    for proc in top_mem:
        mem_val = proc['memory_percent'] if proc['memory_percent'] is not None else 0.0
        print(f"  {proc['pid']:<8} {proc['name'][:29]:<30} {mem_val:.1f}%")

def main():
    """Main function to run the system monitor."""
    print("Starting System Monitor... Press Ctrl+C to exit.")
    time.sleep(1)
    
    prev_net_info = None
    
    try:
        while True:
            clear_screen()
            
            # Gather all system information
            cpu_info = get_cpu_info()
            mem_info = get_memory_info()
            disk_info = get_disk_info()
            net_info = get_network_info()
            top_cpu, top_mem = get_top_processes(5)
            
            # Display everything
            display_header()
            display_cpu(cpu_info)
            display_memory(mem_info)
            display_disk(disk_info)
            display_network(net_info, prev_net_info)
            display_processes(top_cpu, top_mem)
            
            print("\n" + "=" * 80)
            print("Press Ctrl+C to exit | Refreshing every 2 seconds...")
            
            prev_net_info = net_info
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\n\nSystem Monitor stopped.")
        sys.exit(0)

if __name__ == "__main__":
    main()