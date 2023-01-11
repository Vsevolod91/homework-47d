import psycopg2
import csv

conn_to_db = psycopg2.connect(host="localhost", database="north", user="postgres", password="postgres")
cur = conn_to_db.cursor()
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