# Order Alert System

This project is a Django-based backend system for managing customers and orders, with additional features such as REST API endpoints, OpenID Connect authentication, SMS notifications, and a CI/CD pipeline.

## Step 1: Setting up Django Project and PostgreSQL Database

- Generate a new Django project and configure PostgreSQL as the database.
- Create models for Customers and Orders.
- Ensure simple fields: name, code for Customers; item, amount, time for Orders.

## Step 2: Building REST API Endpoints

- Use Django REST Framework (DRF) to create API endpoints:
  - POST endpoint to add a new customer.
  - POST endpoint to add a new order.

## Step 3: Adding OpenID Connect Authentication

- Integrate OAuth2 using a suitable library for OpenID Connect (e.g., `django-oauth-toolkit`).
- Implement token-based authentication for API access.

## Step 4: SMS Notification on Order Creation

- Add logic to trigger SMS using Africa’s Talking API when a new order is created.
  - Send customer name and order details via SMS.

## Step 5: Unit Testing & Coverage

- Write unit tests to validate:
  - Customer and Order creation.
  - Authentication and API access.
  - SMS functionality.
- Ensure coverage is above 90%.

## Step 6: CI/CD Pipeline

- Set up GitHub Actions or another CI/CD tool to automate testing and deployment.
- Deploy to platforms like Heroku or AWS Lambda.

## Step 7 (Bonus): Frontend in ReactJS

- Create a simple ReactJS frontend to add customers and orders via the API. Make use of Components and Style in Material UI if possible.

## Installation

```bash
# Clone the repository
git clone https://github.com/MrBytes10/Customer-Order-Alerts-Backend-v2

# Navigate to the project directory
cd Customer-Order-Alerts-Backend-v2

# Install dependencies
pip install -r requirements.txt

# Set up PostgreSQL database
# Ensure you have PostgreSQL installed and running
# Create a database and update the DATABASE_CONFIG in settings.py

# Apply migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Run the development server
python manage.py runserver


# Usage
- Access the admin panel at http://127.0.0.1:8000/admin/
- Use the API endpoints to add customers and orders:
-- POST /api/customers/ to add a new customer.
-- POST /api/orders/ to add a new order.


# Contributing
1. Fork the repository
2. Create a new branch (git checkout -b feature-branch)
3. Make your changes
4. Commit your changes (git commit -m 'Add some feature')
5. Push to the branch (git push origin feature-branch)
6. Open a pull request

# License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact Information
MrBytes10 - a.m.ndeti@gmail.com

Project Link: https://github.com/MrBytes10/Customer-Order-Alerts-Backend-v2