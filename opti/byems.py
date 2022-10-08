#!/usr/bin/env python3

import psycopg2
import csv

db = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="217.75.161.89",
    port=5432,
)

c = db.cursor()

c.execute("select * from product_items")
product_items = c.fetchall()

with open("product_items.csv", "w") as file:
    writer = csv.writer(file, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL)
    for product_item in product_items:
        writer.writerow(product_item)

c.close()
