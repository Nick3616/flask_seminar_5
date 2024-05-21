import requests
import threading
import multiprocessing
import asyncio
import aiohttp

class BaseDownloader:
    def download_image(self, url):
        image_name = url.split("/")[-1]
        response = requests.get(url)
        if response.status_code == 200:
            with open(image_name, 'wb') as file:
                file.write(response.content)
                print(f"Downloaded {image_name}")

    def download_images(self, urls):
        for url in urls:
            self.download_image(url)

class ThreadedDownloader(BaseDownloader):
    def download_images(self, urls):
        threads = []
        for url in urls:
            t = threading.Thread(target=self.download_image, args=(url,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

class MultiprocessDownloader(BaseDownloader):
    def download_images(self, urls):
        processes = []
        for url in urls:
            p = multiprocessing.Process(target=self.download_image, args=(url,))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()

class AsyncDownloader:
    async def download_image(self, session, url):
        image_name = url.split("/")[-1]
        async with session.get(url) as response:
            if response.status == 200:
                with open(image_name, 'wb') as file:
                    file.write(await response.read())
                    print(f"Downloaded {image_name}")

    async def download_images(self, urls):
        async with aiohttp.ClientSession() as session:
            tasks = [self.download_image(session, url) for url in urls]
            await asyncio.gather(*tasks)


