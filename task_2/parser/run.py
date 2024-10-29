from task_2.parser.downloader import Downloader
from task_2.parser.file_parser import get_products

downloader = Downloader()
downloader.download()
products = get_products()
save_to_database(products)
downloader.delete_downloaded_files()