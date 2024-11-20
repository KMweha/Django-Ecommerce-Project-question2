from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for products
products = []


# Product resource
class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price


# POST /products
@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()

    # Validate input data
    if not data or 'name' not in data or 'description' not in data or 'price' not in data:
        return jsonify({"error": "Invalid input data"}), 400

    try:
        price = float(data['price'])
    except ValueError:
        return jsonify({"error": "Price must be a number"}), 400

    product = Product(data['name'], data['description'], price)
    products.append(product)

    return jsonify({"message": "Product created", "product": data}), 201


# GET /products
@app.route('/products', methods=['GET'])
def get_products():
    product_list = [{"name": p.name, "description": p.description, "price": p.price} for p in products]
    return jsonify(product_list), 200


if __name__ == '__main__':
    app.run(debug=True)
