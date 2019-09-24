import csv
import MySQLdb
import sys
from datetime import datetime, date

con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='root', passwd='1111')
c = con.cursor()

# Query the Suppliers table
c.execute("SELECT * FROM Suppliers")
# c.execute("SELECT * FROM Suppliers WHERE supplier_name = 'Supplier X' ")
# c.execute("SELECT * FROM Suppliers WHERE cost > 300 ")
# c.execute("SELECT Supplier_Name FROM Suppliers")
# c.execute("SELECT Supplier_Name, Cost FROM Suppliers")

rows = c.fetchall()
for row in rows:
    row_list_output = []
    for column_index in range(len(row)):
        row_list_output.append(str(row[column_index]))
    print(row_list_output)
