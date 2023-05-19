"""Скрипт для заполнения данными таблиц в БД Postgres."""

import csv

import psycopg2

conn = psycopg2.connect(host="localhost", database="north", user="postgres", password="1305")
try:
    with conn:
        with conn.cursor() as cur:
            with open('north_data/employees_data.csv', newline='', encoding='utf-8') as f:
                reader = csv.reader(f, delimiter=',', quotechar='"')
                next(reader)
                for row in reader:
                    cur.execute("INSERT INTO employees (first_name, last_name, title, birth_date, notes)"
                                "VALUES (%s, %s, %s, %s, %s)", row)

            with open('north_data/customers_data.csv', newline='', encoding='utf-8') as f:
                reader = csv.reader(f, delimiter=',', quotechar='"')
                next(reader)
                for row in reader:
                    cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", row)

            with open('north_data/orders_data.csv', newline='', encoding='utf-8') as f:
                reader = csv.reader(f, delimiter=',', quotechar='"')
                next(reader)
                for row in reader:
                    cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", row)

finally:
    conn.close()
