import psycopg2
import csv

source_conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="postgres")
cur = source_conn.cursor()
source_conn.autocommit = True
cur.execute("CREATE DATABASE north_2")
source_conn.close()

conn_to_db = psycopg2.connect(host="localhost", database="north_2", user="postgres", password="postgres")
cur = conn_to_db.cursor()

cur.execute("""CREATE TABLE customers (
	customer_id varchar(20) PRIMARY KEY,
	company_name varchar(50) NOT NULL,
	contact_name varchar(50) NOT NULL
)""")

cur.execute("""CREATE TABLE employees (
    employee_id int PRIMARY KEY,
	first_name varchar(30) NOT NULL,
	last_name varchar (30) NOT NULL,
	title varchar(50) NOT NULL,
	birth_date date NOT NULL,
	notes text NOT NULL
)""")

cur.execute("""CREATE TABLE orders (
	order_id int PRIMARY KEY,
	customer_id varchar(20) REFERENCES customers(customer_id) NOT NULL,
	employee_id int REFERENCES employees(employee_id) NOT NULL,
	order_date date NOT NULL,
	ship_city varchar(30) NOT NULL
)""")

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