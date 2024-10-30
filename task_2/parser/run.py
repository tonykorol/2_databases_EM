import asyncio
import time

from task_2.parser.database_saver import save_to_database
from task_2.parser.downloader import Downloader
from task_2.parser.file_parser import get_products
from task_2.parser.site_parser import SiteParser


async def main():
    try:
        start_time = time.time()
        print(f"Start at {start_time}")

        parser = SiteParser()
        print(f"Run parser")
        urls = await parser.start()

        downloader = Downloader(urls)
        print(f"Run downloader")
        await downloader.download()
        print(f"download time {time.time() - start_time}")

        products = await get_products()
        print(f"Run save to database")
        await save_to_database(products)


    except Exception as e:
        print(e)
    finally:
        print(f"Delete files")
        await downloader.delete_downloaded_files()
        end_time = time.time()
        print(end_time - start_time)



if __name__ == "__main__":
    asyncio.run(main())
