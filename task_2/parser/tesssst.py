import xlrd

workbook = xlrd.open_workbook("file_2024-10-29_17:43:09.168761.xls")
sheet = workbook.sheet_by_index(0)
for row_num in range(sheet.nrows):
    row_values = sheet.row_values(row_num)
    print(row_values)