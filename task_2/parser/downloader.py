import asyncio
import os
from datetime import datetime

import aiohttp



class Downloader:
    def __init__(self, urls: list) -> None:
        self.urls = urls
        self.download_folder = "downloaded_files"
        if self.download_folder not in os.listdir():
            os.mkdir(self.download_folder)

    async def download(self) -> None:
        async with aiohttp.ClientSession() as session:
            tasks = []
            for url in self.urls:
                task = asyncio.create_task(self.fetch(session, url))
                tasks.append(task)
            await asyncio.gather(*tasks)

    async def fetch(self, session: aiohttp.ClientSession, url: str) -> None:
        async with session.get(f"https://spimex.com{url}") as response:
            if response.status == 200:
                content = await response.read()
                await self.save_file(self.filename_creator(), content)

    async def save_file(self, filename: str, content) -> None:
        filepath = os.path.join(self.download_folder, filename)
        with open(filepath, "wb") as file:
            file.write(content)

    @staticmethod
    def filename_creator() -> str:
        now = datetime.now()
        return f"file_{now.date()}_{str(now.time()).replace(':', '.')}.xls"

    async def delete_downloaded_files(self) -> None:
        for filename in os.listdir("downloaded_files"):
            try:
                os.remove(os.path.join(self.download_folder, filename))
            except Exception as e:
                print(f"Ошибка удаления файла {filename}\n{e}")
