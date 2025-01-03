# Fast File Downloader to Google Drive

Ever tried to download a huge file, only to find that your internet is too slow or you’re limited by download speeds? Or maybe the file is so big that the download takes forever? This script is here to solve that problem! 

It helps you **download large files faster** by **splitting the download into smaller pieces**, which means **faster downloads** and **no waiting around**. Once the download is finished, the script **uploads the file directly to your Google Drive**, so you can download it at **full speed** from there later.

## Why Is This Useful?

When you need to download big files like movies, games, or software, your internet speed can make it frustrating. Slow downloads, time limits, or bandwidth restrictions can ruin the experience. But what if you could **download files faster** without worrying about slow speeds? This is exactly what this script does!

**How?** Instead of downloading the whole file at once (which can be slow), it breaks the file into **smaller parts** and downloads them at the same time. Once it's done, it uploads the file to **Google Drive**, where you can download it again **faster** and **without any limits**.

### The Benefits:
- **Download faster**: The file is broken into smaller pieces, which means it can be downloaded more quickly.
- **No more slow downloads**: If you’re limited by your internet speed, this method helps you work around that by downloading multiple parts at once.
- **Save to Google Drive**: After downloading, the file is uploaded directly to your Google Drive, where you can grab it later at **full speed**.

## Features

- **Speed up slow downloads**: The script splits the file into smaller chunks, which are downloaded at the same time, making the whole process faster.
- **Automatic Google Drive upload**: Once the file is downloaded, it’s automatically uploaded to **your Google Drive**, so you can access it anytime.
- **No need to stay stuck in front of the screen**: Let the script run while you get other things done. It handles the download and upload in the background.

## How It Works

Here’s the simple idea:

1. **Break the file into pieces**: The script **splits** the file into smaller parts (by default 1MB), and downloads them all at once. This **speeds up the download** and helps you bypass slow speeds or download limits.
   
2. **Upload to Google Drive**: When the download is complete, it’s **uploaded to your Google Drive**, where you can download it later at **full speed**.

3. **No more waiting**: Instead of waiting hours for a big file to download, this method lets you download it in parts, much faster, and then you can access it anytime from Google Drive.

## Getting Started

### What You Need:

- **Google Colab**: We’ll use Google Colab because it’s an easy, ready-to-go environment where you don’t have to set up anything complicated.
- **Python 3.x**: The script uses Python and the `aiohttp` library to handle downloads.

To install `aiohttp` in Colab, simply run:
```bash
pip install aiohttp
```

### How to Run It

1. **Clone the repository**:
    ```bash
    git clone https://github.com/abdulsaheel/async-file-downloader.git
    cd async-file-downloader
    ```

2. **Open the script in Google Colab**.

3. **Change the `url`** variable to the download link for the file you want to download.

4. **Run the script** in Google Colab (it's the easiest way to use it!).

### Using It in Google Colab (Super Easy!)

1. **Mount your Google Drive**:
    ```python
    from google.colab import drive
    drive.mount('/content/drive')
    ```

2. **Run the script**, and it will download the file and **automatically upload it to Google Drive** for you.

## Example

Here’s an example of how you use the script by setting the URL for the file:

```python
url = "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"
await main()
```

### Contributing

If you find bugs, want to add new features, or improve the script, **contributions are welcome**! You can open an issue or submit a pull request. Let’s make it even better together!



### Open in Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/abdulsaheel/async-file-downloader/blob/main/async_file_downloader.ipynb)

---

### Why This Is So Helpful:

This script makes **downloading big files easier** and **faster**. If you’re dealing with slow internet or download limits, it helps by **splitting the download into smaller chunks**. After the download is done, the file is sent to **Google Drive**, so you can grab it later at **full speed**, **without any limits**. No more waiting around for downloads — just a quicker, smarter way to handle large files!
