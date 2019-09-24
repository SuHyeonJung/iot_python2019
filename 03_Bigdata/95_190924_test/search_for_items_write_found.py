import csv
import MySQLdb
import sys
import mysql.connector
from datetime import datetime, date
from xlrd import open_workbook, xldate_as_tuple
import glob
import os

input_file = sys.argv[1] #suppliers_2012.csv

# mydb = mysql.connector.connect(host='localhost',user='root', passwd='1111')
# my_cursor = mydb.cursor()
# my_cursor.execute('create database Suppliers')
con = MySQLdb.connect(host='localhost', port= 3306, db='suppliers', user='root', passwd='1111', charset='utf8')
c = con.cursor()
# c.execute("""CREATE TABLE Suppliers
#         (Item_Number int,
#         Description VARCHAR(10),
#         Supplier VARCHAR(10),
#         Cost FLOAT,
#         Date DATE,
#         File_name VARCHAR(20));""")
item_number_to_find = ['1234', '2345', '3456', '4567', '5678', '6789', '7890']

file_reader = csv.reader(open(input_file, 'r'), delimiter = ',')
header = next(file_reader)
for row in file_reader:
     data = []
     for column_index in range(len(header)):
         if str(row[0]).split('.')[0].strip() in item_number_to_find:
             if column_index == 3:
                data.append(str(row[column_index]).lstrip('$')\
                            .replace(',', '').strip())
             else:
                data.append(row[column_index])
     print(data)
     c.execute("""INSERT INTO Suppliers 
     (Item_Number,Description,Supplier,Cost,Date) VALUES (%s, %s, %s, %s, %s);""", data)
con.commit()

c.execute("SELECT * FROM Suppliers")
rows = c.fetchall()
for row in rows:
    row_list_output = []
    for column_index in range(len(row)):
        row_list_output.append(str(row[column_index]))
    print(row_list_output)

