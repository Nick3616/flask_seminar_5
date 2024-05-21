import sys
import time
import asyncio
from image_downloader import ThreadedDownloader, MultiprocessDownloader, AsyncDownloader


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <url1> <url2> ...")
        sys.exit(1)

    urls = sys.argv[1:]

    threaded_downloader = ThreadedDownloader()
    threaded_start_time = time.time()
    threaded_downloader.download_images(urls)
    threaded_end_time = time.time()

    multiprocess_downloader = MultiprocessDownloader()
    multiprocess_start_time = time.time()
    multiprocess_downloader.download_images(urls)
    multiprocess_end_time = time.time()

    async_downloader = AsyncDownloader()
    async_start_time = time.time()
    asyncio.run(async_downloader.download_images(urls))
    async_end_time = time.time()

    print(f"Multi-threaded download time: {threaded_end_time - threaded_start_time} seconds")
    print(f"Multiprocess download time: {multiprocess_end_time - multiprocess_start_time} seconds")
    print(f"Asynchronous download time: {async_end_time - async_start_time} seconds")

if __name__ == "__main__":
    main()