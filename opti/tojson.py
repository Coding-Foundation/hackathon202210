#!/usr/bin/env python
import csv
import json

product_dict = {1: [], 2: [], 3: []}

with open("product_items.csv", "r") as file:
    products = csv.reader(file, delimiter=" ", quotechar="|")

    for product in products:
        product_id = int(product[1])
        product_dict[product_id].append([product[0]] + product[2:])

with open("product_items.json", "w") as file:
    json.dump(product_dict, file)
