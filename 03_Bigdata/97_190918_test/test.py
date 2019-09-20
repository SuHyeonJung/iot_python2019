import openpyxl
import os

title = 'test2.xlsx'
b = ['a', 'b', 'c', 'd', 'e']
a = [1, 2, 3, 4, 5]
if not os.path.exists(title):
    wb = openpyxl.Workbook()
    wb1 = wb.active
    wb1.append(b)
    wb.save(title)

wb = openpyxl.load_workbook(filename=title, read_only=False, data_only=False)
sheet1 = wb.active
for i in range(5):
    sheet1.append(a)

wb.save(title)

