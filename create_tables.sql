CREATE DATABASE north;

CREATE TABLE customers (
	customer_id varchar(20) PRIMARY KEY,
	company_name varchar(50) NOT NULL,
	contact_name varchar(50) NOT NULL
);

CREATE TABLE employees (
	first_name varchar(30) NOT NULL,
	last_name varchar (30) NOT NULL,
	title varchar(50) NOT NULL,
	birth_date date NOT NULL,
	notes text NOT NULL
);

CREATE TABLE orders (
	order_id int PRIMARY KEY,
	customer_id varchar(20) NOT NULL,
	employee_id int NOT NULL,
	order_date date NOT NULL,
	ship_city varchar(30) NOT NULL
);


