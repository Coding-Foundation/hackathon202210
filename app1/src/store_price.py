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


def clone_product(product_id, new_product_id, coef):
    with open("/data/code/product_items.json", "r") as file:
        products = json.load(file)
    print("load successful")
    print(str(products)[:500])

    # LIST_PRODUCT_URL = "http://ms1:8000/product_items"
    # items = requests.get(url=f"{LIST_PRODUCT_URL}/{product_id}").json()

    # ADD_PRODUCT_URL = "http://ms1:8000/product_item"
    new_items = []
    for id, name, price in products[str(product_id)]:
        new_items.append([str(new_product_id), name, float(price) * coef])
    products[str(product_id)].extend(new_items)

    with open("/data/code/product_items.json", "w") as file:
        json.dump(products, file)

    print("clone")
    print(len(products(product_id)))
    return len(products[product_id])


"""
Find the sum of items prices of a product
"""


def sum_of_prices(product_id):
    with open("/data/code/product_items.json", "r") as file:
        products = json.load(file)
    print("load successful")
    print(str(products)[:500])
    items = products[str(product_id)]
    return round(sum(int(item[2]) for item in items))


"""
Delete all product's items
"""


def delete_product(product_id):
    with open("/data/code/product_items.json", "r") as file:
        products = json.load(file)
    print("load successful")
    print(str(products)[:500])
    del products[str(product_id)]
    with open("/data/code/product_items.json", "w") as file:
        json.dump(products, file)
    return f"Product {product_id} was successefully deleted"


if __name__ == "__main__":
    print(clone_product(1, 4, 1.5))
    print(sum_of_prices(1))
    print(delete_product(1))
