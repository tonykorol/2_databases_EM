from datetime import datetime

import aiohttp
from bs4 import BeautifulSoup


class SiteParser:
    PAGE_URL = "https://spimex.com/markets/oil_products/trades/results/?page=page-{0}&bxajaxid=d609bce6ada86eff0b6f7e49e6bae904"

    async def start(self) -> list:
        file_links = await self.get_file_links()
        return file_links

    async def fetch_page(self, session: aiohttp.ClientSession, n: int = 1) -> str:
        url = self.PAGE_URL.format(n)
        async with session.get(url) as response:
            if response.status == 200:
                return await response.text()
            else:
                raise ValueError(f"Request failed with status code {response.status}")

    @staticmethod
    def parse_blocks(page_html: str) -> list:
        soup = BeautifulSoup(page_html, 'html.parser')
        blocks = soup.find_all(class_="accordeon-inner__item")
        file_links = []
        for block in blocks:
            file_date_str = block.select_one("div.accordeon-inner__item-inner > div > p > span")
            if file_date_str:
                file_date_str = file_date_str.text
            else:
                continue
            file_date = datetime.strptime(file_date_str, "%d.%m.%Y")
            if file_date > datetime(2022, 12, 31):
                file_link = block.select_one("div.accordeon-inner__header > a")["href"]
                file_links.append(file_link)
            else:
                break
        return file_links

    async def get_file_links(self) -> list:
        async with aiohttp.ClientSession() as session:
            file_links = []
            page_number = 1
            while True:
                page_html = await self.fetch_page(session, page_number)
                new_links = self.parse_blocks(page_html)
                if not new_links:
                    break
                file_links.extend(new_links)
                page_number += 1
            return file_links
