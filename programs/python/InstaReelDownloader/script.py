import instaloader
import os
import re

def get_shortcode_from_url(url):
    """Extract shortcode from Instagram URL"""
    patterns = [
        r'instagram\.com/reel/([^/?]+)',
        r'instagram\.com/p/([^/?]+)',
        r'instagram\.com/tv/([^/?]+)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

def download_reel(url, download_path='downloads'):
    """
    Download Instagram reel from URL
    
    Args:
        url: Instagram reel URL
        download_path: Directory to save the downloaded reel
    """
    # Create download directory if it doesn't exist
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    # Initialize Instaloader
    L = instaloader.Instaloader(
        download_videos=True,
        download_video_thumbnails=False,
        download_geotags=False,
        download_comments=False,
        save_metadata=False,
        compress_json=False,
        dirname_pattern=download_path
    )
    
    try:
        # Extract shortcode from URL
        shortcode = get_shortcode_from_url(url)
        
        if not shortcode:
            print("❌ Invalid Instagram URL. Please provide a valid reel/post URL.")
            return False
        
        print(f"📥 Downloading reel with shortcode: {shortcode}")
        
        # Get post and download
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        
        # Download the post
        L.download_post(post, target=download_path)
        
        print(f"✅ Reel downloaded successfully to '{download_path}' folder!")
        return True
        
    except instaloader.exceptions.InstaloaderException as e:
        print(f"❌ Error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def main():
    print("=" * 50)
    print("Instagram Reel Downloader")
    print("=" * 50)
    print("\nNote: This downloads public reels only.")
    print("For private accounts, you may need to login.\n")
    
    # Get URL from user
    url = input("Enter Instagram reel URL: ").strip()
    
    if not url:
        print("❌ No URL provided!")
        return
    
    # Optional: custom download path
    custom_path = input("Download folder (press Enter for 'downloads'): ").strip()
    download_path = custom_path if custom_path else 'downloads'
    
    # Download the reel
    download_reel(url, download_path)

if __name__ == "__main__":
    main()