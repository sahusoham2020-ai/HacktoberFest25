# 📥 Instagram Reel Downloader

A simple and efficient Python script to download Instagram reels, posts, and IGTV videos directly to your local machine.

## ✨ Features

- 🎥 Download Instagram reels, posts, and IGTV videos
- 🔗 Support for multiple URL formats
- 📁 Automatic folder creation
- 🎯 Clean and intuitive CLI interface
- ⚡ Fast and reliable downloads
- 🔓 Works with public content (no login required)

## 📋 Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## 🚀 Installation

1. Clone this repository or download the script:
```bash
git clone <your-repo-url>
cd instagram-reel-downloader
```

2. Install required dependencies:
```bash
pip install instaloader
```

## 💻 Usage

### Basic Usage

Run the script:
```bash
python instagram_downloader.py
```

Then follow the prompts:
1. Enter the Instagram reel URL
2. Optionally specify a custom download folder (or press Enter for default)

### Example

```
==================================================
Instagram Reel Downloader
==================================================

Note: This downloads public reels only.
For private accounts, you may need to login.

Enter Instagram reel URL: https://www.instagram.com/reel/ABC123xyz/
Download folder (press Enter for 'downloads'): 
📥 Downloading reel with shortcode: ABC123xyz
✅ Reel downloaded successfully to 'downloads' folder!
```

### Supported URL Formats

- Reels: `https://www.instagram.com/reel/SHORTCODE/`
- Posts: `https://www.instagram.com/p/SHORTCODE/`
- IGTV: `https://www.instagram.com/tv/SHORTCODE/`

## 📂 File Structure

```
instagram-reel-downloader/
├── instagram_downloader.py    # Main script
├── README.md                   # Documentation
└── downloads/                  # Default download folder (auto-created)
```

## ⚙️ Configuration

### Custom Download Path

You can specify a custom download location when prompted, or modify the default path in the script:

```python
download_reel(url, download_path='my_custom_folder')
```

### Adding Login Support (Optional)

For downloading content from private accounts you follow, add login functionality:

```python
# Add this before downloading
L.login("your_username", "your_password")
```

**Note:** Be cautious with storing credentials. Consider using environment variables or secure credential management.

## 🔒 Privacy & Legal

- This tool is for **personal use only**
- Only download content you have permission to download
- Respect Instagram's Terms of Service
- Respect content creators' rights
- Do not redistribute downloaded content without permission

## 🐛 Troubleshooting

### Common Issues

**"Invalid Instagram URL"**
- Ensure the URL is complete and properly formatted
- Check that it's a direct link to a reel/post

**"Error downloading"**
- The content might be from a private account
- The post may have been deleted
- Check your internet connection

**Rate Limiting**
- Instagram may temporarily block excessive requests
- Wait a few minutes before trying again

## 📦 Dependencies

- [instaloader](https://instaloader.github.io/) - Instagram content downloader library

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## ⚠️ Disclaimer

This tool is provided for educational purposes. Users are responsible for ensuring their use complies with Instagram's Terms of Service and applicable laws. The developers assume no liability for misuse of this tool.

## 🙏 Acknowledgments

- Built with [Instaloader](https://instaloader.github.io/)
- Inspired by the need for simple, ethical content downloading

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

Made with ❤️ for content archiving and personal use