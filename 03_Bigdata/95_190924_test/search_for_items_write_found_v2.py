import csv
import MySQLdb
import sys
import mysql.connector
from datetime import datetime, date
from xlrd import open_workbook, xldate_as_tuple
import glob
import os

input_file = sys.argv[1] #1output.csv
output_file = sys.argv[2] #combine_data.csv

con = MySQLdb.connect(host='localhost', port= 3306, db='suppliers', user='root', passwd='1111', charset='utf8')
c = con.cursor()

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        for row_list in filereader:
            filewriter.writerow(row_list)

c.execute("SELECT * FROM Suppliers")
rows = c.fetchall()
with open(output_file, 'a', newline='') as csv_output_file:
    filewriter = csv.writer(csv_output_file)
    for row in rows:
        row_list_output = []
        for column_index in range(len(row)):
            row_list_output.append(str(row[column_index]))
        print(row_list_output)
        filewriter.writerow(row_list_output)
