# E-Commerce Django Project

## Overview
This project is an e-commerce application developed using Django. It includes models for Customers and Orders, establishing a one-to-many relationship where a customer can place multiple orders. Additionally, the project provides a REST API to manage customers and orders.

## Models
- **Customer**
    - `name`: The full name of the customer.
    - `email`: The unique email address of the customer.

- **Order**
    - `customer`: A foreign key linking to the Customer model (one customer can have multiple orders).
    - `order_date`: The date and time when the order was created (automatically set).
    - `total_amount`: The total amount for the order.

## REST API Endpoints

### Customers
- **POST /api/customers/**: Create a new customer.
    - Request Body:
      ```json
      {
          "name": "Khachina Mweha",
          "email": "kmweha@gmail.com"
      }
      ```
    - Response:
        - 201 Created: Customer created successfully.
        - 400 Bad Request: Invalid input data.

- **GET /api/customers/**: Retrieve a list of all customers.
    - Response:
        - 200 OK: Returns a list of customers.

### Orders
- **POST /api/orders/**: Create a new order.
    - Request Body:
      ```json
      {
          "customer": 2,
          "total_amount": 99.99
      }
      ```
    - Response:
        - 201 Created: Order created successfully.
        - 400 Bad Request: Invalid input data.

- **GET /api/orders/**: Retrieve a list of all orders.
    - Response:
        - 200 OK: Returns a list of orders.

## Steps to Set Up the Environment

1. **Clone the Repository**
   ```bash
   git clone https://github.com/KMweha/Django-Ecommerce-Project-question2
   cd ecommerce

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   
4. **Install Dependencies**
   ```bash
   pip install django

5. **Run Migrations**
   ```bash
   python manage.py migrate

6. Access the Application Open your web browser and go to http://127.0.0.1:8000/.

## Testing the REST API

You can test the REST API using tools like Postman or `curl`. Below are example requests for creating customers and orders, as well as retrieving lists of customers and orders.

### Example Requests

#### Create a Customer
To create a new customer, use the following `curl` command:
    
    curl -X POST http://127.0.0.1:8000/api/customers/ -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john.doe@example.com"}'


#### Get All Customers
To retrieve a list of all customers, use the following `curl` command:
    
     curl -X GET http://127.0.0.1:8000/api/customers/

#### Create an Order
To create a new order, use the following curl command (make sure to replace 1 with the actual customer ID):

     curl -X POST http://127.0.0.1:8000/api/orders/ -H "Content-Type: application/json" -d '{"customer": 1, "total_amount": 99.99}'

#### Get All Orders
To retrieve a list of all orders, use the following curl command:

     curl -X GET http://127.0.0.1:8000/api/orders/