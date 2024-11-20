import requests

API_URL = 'http://127.0.0.1:5000/products'


def add_product(name, description, price):
    product_data = {
        "name": name,
        "description": description,
        "price": price
    }
    response = requests.post(API_URL, json=product_data)
    print(response.json())


def get_products():
    response = requests.get(API_URL)
    print(response.json())


if __name__ == '__main__':
    # Add new products
    add_product("TestProduct 1", "Description for product 1", 19.99)
    add_product("TestProduct 2", "Description for product 2", 29.99)

    # Retrieve and print all products
    get_products()
