import os
import shutil
import time
from datetime import datetime, UTC

import requests

from task_2.parser.site_parser import SiteParser


class Downloader:
    def __init__(self):
        parser = SiteParser()
        self.urls = parser.start()
        os.mkdir("downloaded_files")

    def download(self):
        for url in self.urls:
            response = requests.get(f"https://spimex.com{url}")
            if response.status_code == 200:
                self.save_file(response)

    def save_file(self, response):
        with open(f"downloaded_files/{self.filename_creator()}", "wb") as file:
            file.write(response.content)

    @staticmethod
    def filename_creator():
        return f"file_{datetime.date(datetime.now())}_{datetime.time(datetime.now())}.xls"

    @staticmethod
    def delete_downloaded_files():
        shutil.rmtree("downloaded_files")
