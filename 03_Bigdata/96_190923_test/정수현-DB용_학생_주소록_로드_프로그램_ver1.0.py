import csv
import MySQLdb
import sys
from datetime import datetime, date


input_file = sys.argv[1] # Basic_Student_Info.csv
# con = MySQLdb.connect(host='localhost', port= 3306, db='my_student', user = 'root', passwd = '1111')
con = MySQLdb.connect(host='localhost', port= 3306, db='my_student', user='root', passwd='1111', charset='utf8')
c = con.cursor()

 # Read the CSV file
 # Insert the data into the Suppliers table
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader)
for row in file_reader:
    data = []
    for column_index in range(1, len(header)):
        data.append(str(row[column_index].strip()))
    print(data)
    c.execute("""INSERT INTO student_Load 
                (Name,Sex,Age,Major) VALUES (%s, %s, %s, %s);""", data)
con.commit()

c.execute("SELECT * FROM student_Load")
rows = c.fetchall()
for row in rows:
    row_list_output = []
    for column_index in range(len(row)):
        row_list_output.append(str(row[column_index]))
    print(row_list_output)
