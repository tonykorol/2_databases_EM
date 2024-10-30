from datetime import datetime

import requests
from bs4 import BeautifulSoup


class SiteParser:
    URL = "https://spimex.com/markets/oil_products/trades/results/?page=page-{0}&bxajaxid=d609bce6ada86eff0b6f7e49e6bae904"


    async def start(self) -> list:
        file_links = await self.get_file_links()
        return file_links

    async def get_page(self, n: int = 1) -> str:
        response = requests.get(self.URL.format(n))
        if response.status_code == 200:
            return response.text

    async def get_file_links(self) -> list:
        file_links = []
        page_number = 1
        work = True
        while work:
            page_html = await self.get_page(page_number)
            page_number += 1
            soup = BeautifulSoup(page_html, 'html.parser')
            blocks = soup.find_all(class_="accordeon-inner__item")
            for block in blocks:
                file_date = block.select("div.accordeon-inner__item-inner > div > p > span")[0].text
                if datetime.strptime(file_date, "%d.%m.%Y") > datetime(2022, 12, 31):
                    file_link = block.select("div.accordeon-inner__header > a")[0]['href']
                    file_links.append(file_link)
                else:
                    work = False
        return file_links
