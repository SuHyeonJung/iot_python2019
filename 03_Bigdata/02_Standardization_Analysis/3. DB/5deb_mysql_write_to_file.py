import csv
import MySQLdb
import sys

# Path to and name of a CSV input file
output_file = sys.argv[1] # output_files/5data_from_mysql.csv

# Connect to a MySQL database
con = MySQLdb.connect(host='localhost', port = 3306, db='my_suppliers', user = 'root', passwd = '1111')
c = con.cursor()

# Create a file writer objext and write the header row
filewriter = csv.writer(open(output_file, 'w', newline=''), delimiter =',')
header = ['Su[[lier Name', 'Invoice Number', 'Part Number', 'Purchase Date']
filewriter.writerow(header)

# Query the Suppliers table and write the ouput to a CSV file
c.execute("""SELECT *
        From Suppliers
        WHERE Cost > 700.0;""")
rows = c.fetchall()
for row in rows:
    filewriter.writerow(row)