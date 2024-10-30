import os
from datetime import datetime

import xlrd
from xlrd.sheet import Sheet

from task_2.parser.data_classes import Product

directory_path = "downloaded_files"
products = []

def get_filename() -> str:
    for filename in os.listdir(directory_path):
        yield filename

def parse_files() -> None:
    for filename in get_filename():
        workbook = xlrd.open_workbook(os.path.join(directory_path, filename))
        sheet = workbook.sheet_by_index(0)
        create_product(sheet)

def create_product(sheet: Sheet) -> None:
    write_flag = False
    product_date = ''
    for row_num in range(sheet.nrows):
        row_values = sheet.row_values(row_num)
        if row_values[1] == 'Единица измерения: Метрическая тонна':
            write_flag = True
        elif row_values[1] == 'Единица измерения: Килограмм':
            write_flag = False
        elif row_values[1] and row_values[1].split()[0] == "Дата":
            product_date = row_values[1].split()[2]

        if write_flag:
            try:
                if row_values[1] and row_values[1].split()[0] == "Итого:":
                    continue
                elif int(row_values[-1]) > 0:
                    exchange_product_id = row_values[1]
                    exchange_product_name = row_values[2].split(',')[0]
                    oil_id = exchange_product_id[:4]
                    delivery_basis_id = exchange_product_id[4:7]
                    delivery_basis_name = row_values[3]
                    delivery_type_id = exchange_product_id[-1]
                    volume = int(row_values[4])
                    total = int(row_values[5])
                    count = int(row_values[-1])
                    date = datetime.strptime(product_date, "%d.%m.%Y")
                    product = Product(
                        exchange_product_id,
                        exchange_product_name,
                        oil_id,
                        delivery_basis_id,
                        delivery_basis_name,
                        delivery_type_id,
                        volume,
                        total,
                        count,
                        date
                    )
                    products.append(product)
            except ValueError:
                continue


def get_products() -> list[Product]:
    parse_files()
    return products
