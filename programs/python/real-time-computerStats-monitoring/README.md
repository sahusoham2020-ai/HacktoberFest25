# Real-Time System Monitor 📊

A lightweight, cross-platform command-line system monitor built with Python that displays real-time CPU, memory, disk, and network usage statistics with beautiful visual progress bars.

## Features ✨

- **CPU Monitoring** - Real-time CPU usage (overall and per-core) with frequency information
- **Memory Tracking** - RAM and swap memory usage with detailed statistics
- **Disk Usage** - Storage information for all mounted drives
- **Network I/O** - Total data transferred and real-time transfer rates
- **Process Management** - Top 5 processes by CPU and memory consumption
- **Visual Progress Bars** - Easy-to-read usage indicators
- **Auto-Refresh** - Updates every 2 seconds automatically
- **Cross-Platform** - Works on Windows, macOS, and Linux

## Screenshots

```
================================================================================
                              SYSTEM MONITOR                                
                         2024-10-14 15:30:45                               
================================================================================

📊 CPU USAGE
--------------------------------------------------------------------------------
Overall: [████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 28.5%
Cores: 4 | Threads: 8
Frequency: 2400 MHz / 3600 MHz

Per-Core Usage:
  Core 0: [██████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 25.3%
  Core 1: [████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 31.2%
  ...
```

## Installation 🚀

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Steps

1. **Clone or download this repository**
   ```bash
   git clone <repository-url>
   cd system-monitor
   ```

2. **Install required dependencies**
   ```bash
   pip install psutil
   ```

   Or if you're using a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install psutil
   ```

## Usage 💻

### Basic Usage

Simply run the script:

```bash
python system_monitor.py
```

Or make it executable (Linux/macOS):

```bash
chmod +x system_monitor.py
./system_monitor.py
```

### Exiting the Monitor

Press `Ctrl+C` to safely exit the system monitor.

## Requirements 📦

- **Python**: 3.6+
- **psutil**: 5.8.0+ (cross-platform library for system and process utilities)

Install dependencies using:
```bash
pip install -r requirements.txt
```

Create a `requirements.txt` file with:
```
psutil>=5.8.0
```

## How It Works 🔧

The system monitor uses the `psutil` library to gather system information:

1. **CPU Usage**: Monitors overall and per-core CPU percentages
2. **Memory**: Tracks RAM and swap memory utilization
3. **Disk**: Scans all mounted partitions and calculates usage
4. **Network**: Monitors network I/O counters and calculates transfer rates
5. **Processes**: Lists top processes sorted by CPU and memory usage

The display refreshes every 2 seconds to provide real-time updates.

## Customization ⚙️

You can customize the monitor by modifying these parameters in the code:

- **Refresh Interval**: Change `time.sleep(2)` in the `main()` function
- **Number of Processes**: Modify the `limit` parameter in `get_top_processes(limit=5)`
- **Progress Bar Width**: Adjust the `width` parameter in `get_bar(percentage, width=50)`

## Platform Support 🌍

| Platform | Supported | Notes |
|----------|-----------|-------|
| Linux | ✅ | Full support |
| macOS | ✅ | Full support |
| Windows | ✅ | Full support |

## Troubleshooting 🔍

### Permission Errors

Some disk partitions may require elevated permissions. The monitor will skip inaccessible partitions automatically.

**Solution**: Run with administrator/sudo privileges:
```bash
# Linux/macOS
sudo python system_monitor.py

# Windows (Run Command Prompt as Administrator)
python system_monitor.py
```

### Module Not Found Error

If you see `ModuleNotFoundError: No module named 'psutil'`:
```bash
pip install psutil
```

### Display Issues

If the display doesn't clear properly, ensure your terminal supports ANSI escape codes or try a different terminal emulator.

## Future Enhancements 🚀

Potential features to add:
- [ ] Temperature monitoring (CPU/GPU)
- [ ] Battery status for laptops
- [ ] Export data to CSV/JSON
- [ ] Alert system for high resource usage
- [ ] Configuration file support
- [ ] Historical data graphs
- [ ] Web interface option

## Contributing 🤝

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests


## Author ✍️

Created with ❤️ for system monitoring enthusiasts

## Acknowledgments 🙏

- Built using the excellent [psutil](https://github.com/giampaolo/psutil) library
- Inspired by tools like `htop`, `top`, and `Task Manager`

---

**Note**: This tool is for monitoring purposes only. Be cautious when running with elevated privileges.