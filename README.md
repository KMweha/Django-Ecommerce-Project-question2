# E-Commerce Django Project

## Overview
This project is an e-commerce application developed using Django. It includes models for Customers and Orders, establishing a one-to-many relationship where a customer can place multiple orders.

## Models
- **Customer**
    - `name`: The full name of the customer.
    - `email`: The unique email address of the customer.

- **Order**
    - `customer`: A foreign key linking to the Customer model (one customer can have multiple orders).
    - `order_date`: The date and time when the order was created (automatically set).
    - `total_amount`: The total amount for the order.

### Steps to Set Up the Environment

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
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