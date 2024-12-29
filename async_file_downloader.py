import aiohttp
import asyncio
import os
from google.colab import drive
from google.colab import files
import shutil
import re

# Mount Google Drive
drive.mount('/content/drive')

async def fetch_file_size_and_name(url):
    """Fetch the file size and name from the server."""
    async with aiohttp.ClientSession() as session:
        async with session.head(url) as response:
            # Get the 'Content-Length' header to determine file size
            file_size = int(response.headers.get('Content-Length', 0))

            # Try to extract the file name from the 'Content-Disposition' header
            content_disposition = response.headers.get('Content-Disposition', '')
            match = re.search('filename="(.+)"', content_disposition)
            if match:
                file_name = match.group(1)
            else:
                # Fallback to the URL if we can't extract the file name
                file_name = url.split('/')[-1].split('?')[0]

            return file_size, file_name

async def download_chunk(session, url, start_byte, end_byte, chunk_num, output_file):
    """Download a single chunk of the file."""
    headers = {'Range': f"bytes={start_byte}-{end_byte}"}
    async with session.get(url, headers=headers) as response:
        chunk_data = await response.read()
        print(f"Downloading chunk {chunk_num}: bytes {start_byte}-{end_byte}")
        with open(output_file, 'r+b') as f:
            f.seek(start_byte)
            f.write(chunk_data)

async def download_file(url):
    """Main function to download the file asynchronously."""
    # Step 1: Get file size and file name
    file_size, file_name = await fetch_file_size_and_name(url)
    print(f"File size: {file_size} bytes")
    print(f"File name: {file_name}")

    # Step 2: Create output file and prepare to download in chunks
    with open(file_name, 'wb') as f:
        f.truncate(file_size)

    # Step 3: Determine chunk size and number of chunks
    chunk_size = 1024 * 1024  # 1MB per chunk
    num_chunks = (file_size // chunk_size) + (1 if file_size % chunk_size > 0 else 0)

    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(num_chunks):
            start_byte = i * chunk_size
            end_byte = min(start_byte + chunk_size - 1, file_size - 1)
            tasks.append(download_chunk(session, url, start_byte, end_byte, i + 1, file_name))

        # Step 4: Execute all tasks asynchronously
        await asyncio.gather(*tasks)

    print("File download complete!")
    return file_name

async def upload_to_drive(file_name):
    """Upload the downloaded file to Google Drive."""
    # Define the Google Drive path where the file will be uploaded
    drive_path = '/content/drive/MyDrive/'

    # Move the downloaded file to Google Drive
    shutil.move(file_name, os.path.join(drive_path, file_name))
    print(f"File uploaded to Google Drive at: {drive_path}{file_name}")

# URL to download from (replace with the URL of the file you want to download)
url = "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"

# Check if we're in an existing event loop (i.e., Jupyter/IPython environment)
async def main():
    file_name = await download_file(url)
    await upload_to_drive(file_name)

# In Colab, we can use await directly as there is an existing event loop
await main()
