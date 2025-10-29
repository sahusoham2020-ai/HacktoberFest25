from pytube import YouTube
import os

def download_youtube_video():
    print("🎬 === YouTube Video Downloader ===")
    video_url = input("Enter YouTube video URL: ").strip()

    try:
        yt = YouTube(video_url)
    except Exception as e:
        print("❌ Invalid URL or network issue:", e)
        return

    print(f"\n📄 Title: {yt.title}")
    print(f"📺 Channel: {yt.author}")
    print(f"⏱ Duration: {yt.length // 60} min {yt.length % 60} sec")
    print(f"👁 Views: {yt.views:,}\n")

    # Choose resolution
    streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
    print("Available Resolutions:")
    for i, stream in enumerate(streams, 1):
        print(f"{i}. {stream.resolution} ({round(stream.filesize / (1024*1024), 2)} MB)")

    choice = int(input("\nEnter your choice (1/2/...): "))
    stream = streams[choice - 1]

    # Choose save path
    save_path = input("Enter download path (or leave empty for current directory): ").strip() or os.getcwd()

    print(f"\n⬇️ Downloading '{yt.title}' in {stream.resolution}...")
    try:
        stream.download(output_path=save_path)
        print(f"✅ Download complete!\n📂 Saved to: {save_path}")
    except Exception as e:
        print("❌ Download failed:", e)

if __name__ == "__main__":
    download_youtube_video()
