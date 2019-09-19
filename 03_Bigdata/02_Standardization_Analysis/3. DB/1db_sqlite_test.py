#!/usr/bin/env python3
import sqlite3
# :memory:는 휘발성이다.프로그램 종료시 이전 작업 내역은 사라진다.
# 따라서 아래 select문은 정상 수행되지 않는다.
con = sqlite3.connect(':memory:')
# Query the sales table
cursor = con.execute("SELECT * FROM sales")
rows = cursor.fetchall()

# Count the number of rows in the output
row_counter = 0
for row in rows:
    print(row)
    row_counter += 1
print('Number of rows: {}'.format(row_counter))