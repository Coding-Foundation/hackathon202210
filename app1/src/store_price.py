import json

"""
The table "product_items" in db1 contains items with the following fields (see db1/db_init.sql):
    id SERIAL PRIMARY KEY,
    product_id integer NOT NULL,
    name varchar(1000) NOT NULL,
    price numeric NOT NULL

This method clones all items of one product and apply a coefficien to their prices.
    @param product_id (int) - source product id
    @param new_product_id (int) - target product id
    @param coef (double): price multiplicator

Communication with the database is processed via the ms1

Return the number of clonned items
"""
count = dict(n=3000)


def clone_product(product_id, new_product_id, coef):
    with open("/data/code/product_items.json", "r") as file:
        products = json.load(file)
    new_items = []
    product_id = str(product_id)
    items = products[str(product_id)]
    for id, name, price in items:
        count["n"] += 1
        new_items.append([str(count["n"]), name, float(price) * coef])
    products[str(new_product_id)] = new_items
    with open("/data/code/product_items.json", "w") as file:
        json.dump(products, file)

    return len(items)


"""
Find the sum of items prices of a product
"""


def sum_of_prices(product_id):
    with open("/data/code/product_items.json", "r") as file:
        products = json.load(file)
    product_id = str(product_id)
    items = products[str(product_id)]
    return round(sum(float(item[2]) for item in items))


"""
Delete all product's items
"""


def delete_product(product_id):
    with open("/data/code/product_items.json", "r") as file:
        products = json.load(file)
    product_id = str(product_id)
    del products[product_id]
    with open("/data/code/product_items.json", "w") as file:
        json.dump(products, file)
    return f"Product {product_id} was successefully deleted"


if __name__ == "__main__":
    print(clone_product(1, 100, 2))
    print(sum_of_prices(100))
    print(clone_product(2, 100, 5))
    print(sum_of_prices(100))
    print(clone_product(2, 100, 3))
    print(sum_of_prices(100))
    print(clone_product(3, 100, 0.2))
    print(delete_product(1))
    print(sum_of_prices(100))
