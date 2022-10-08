#!/usr/bin/env python
import csv
import json

products_dict = {}

with open("product_items.csv", "r") as file:
    products = csv.reader(file, delimiter=" ", quotechar="|")

    for product in products:
        product_id = product[0]
        products_dict[product_id] = product[1:]

with open("product_items.json", "w") as file:
    json.dump(products_dict, file)
