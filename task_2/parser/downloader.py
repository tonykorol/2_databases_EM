import asyncio
import os
from datetime import datetime

import aiohttp



class Downloader:
    def __init__(self, urls):
        self.urls = urls
        if "downloaded_files" not in os.listdir():
            os.mkdir("downloaded_files")

    async def download(self):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for url in self.urls:
                task = asyncio.create_task(self.fetch(session, url))
                tasks.append(task)
            await asyncio.gather(*tasks)

    async def fetch(self, session: aiohttp.ClientSession, url: str):
        async with session.get(f"https://spimex.com{url}") as response:
            if response.status == 200:
                content = await response.read()
                await self.save_file(await self.filename_creator(), content)

    @staticmethod
    async def save_file(filename: str, content):
        with open(f"downloaded_files/{filename}", "wb") as file:
            file.write(content)

    @staticmethod
    async def filename_creator():
        now = datetime.now()
        return f"file_{now.date()}_{now.time()}.xls"

    @staticmethod
    async def delete_downloaded_files():
        for filename in os.listdir("downloaded_files"):
            try:
                os.remove(f"downloaded_files/{filename}")
            except Exception as e:
                print(f"Ошибка удаления файла {filename}\n{e}")
