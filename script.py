import psycopg2
import csv

source_conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="postgres")
cur = source_conn.cursor()
source_conn.autocommit = True
cur.execute("CREATE DATABASE north_3")
source_conn.close()

conn_to_db = psycopg2.connect(host="localhost", database="north_3", user="postgres", password="postgres")
cur = conn_to_db.cursor()

file_sql = open('create_tables.sql', "r")
sql_commands = file_sql.read().split(";")

for command in sql_commands:
    if not command:
        continue
    cur.execute(command)

with open('north\customers_data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    count = 0
    for row in reader:
        count += 1
        if count == 1:
            continue
        cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", (row[0], row[1], row[2]))

with open('north\employees_data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    count = 0
    employee_id = 0
    for row in reader:
        count += 1
        if count == 1:
            continue
        employee_id += 1
        cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", (employee_id, row[0], row[1], row[2], row[3], row[4]))

with open('north\orders_data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    count = 0
    for row in reader:
        count += 1
        if count == 1:
            continue
        cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", (row[0], row[1], row[2], row[3], row[4]))

conn_to_db.commit()
conn_to_db.close()
print('successfully')