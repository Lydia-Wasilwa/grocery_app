FreshMarket - Smart Grocery Web Application

**FreshMarket** is a lightweight, full-stack e-commerce platform built with Django. It provides a seamless shopping experience for local communities, allowing users to browse fresh produce, manage a shopping cart, and place orders online. 

Designed with simplicity and speed in mind, FreshMarket aligns with **SDG 12: Responsible Consumption and Production** by connecting local farmers directly to consumers.

---

## Key Features

### For Customers
* **Product Browsing:** View fresh groceries with high-quality images and descriptions.
* **Category Filtering:** Easily filter products (e.g., Fruits, Vegetables, Dairy).
* **Smart Cart:** Add items, adjust quantities, and see real-time price updates.
* **Secure Checkout:** Streamlined order placement system.
* **User Dashboard:** Track order history and view past purchases.
* **Authentication:** Secure Login and Registration pages with a custom UI.

### For Store Managers (Admin)
* **Inventory Management:** Full CRUD (Create, Read, Update, Delete) for products and categories.
* **Order Tracking:** View incoming orders, customer details, and payment status.
* **Business Insights:** Dashboard showing total products, total orders, and recent activity.

---

## Technical Stack

* **Backend Framework:** Django 5 (Python)
* **Frontend:** HTML5, CSS3, Bootstrap 5 (Responsive Design)
* **Database:** SQLite (Default for development)
* **Templating:** Django Template Language (DTL)
* **Styling:** Custom CSS overrides for a polished "Fresh" look.

---

## Installation Guide

Follow these steps to run the project locally on your machine without errors.

### 1. Prerequisites
Ensure you have **Python** installed on your machine.
```bash
python --version
# Should return Python 3.10 or higher
2. Clone the Repository
Download the project code to your local machine.

Bash

git clone [https://github.com/YourUsername/FreshMarket.git](https://github.com/YourUsername/FreshMarket.git)
cd FreshMarket
3. Create a Virtual Environment
It is highly recommended to use a virtual environment to manage dependencies.

Bash

# Windows
python -m venv env
env\Scripts\activate

# Mac/Linux
python3 -m venv env
source env/bin/activate
(You will see (env) at the start of your terminal line once activated).

4. Install Dependencies
Install Django and other required packages.

Bash

pip install -r requirements.txt
5. Setup the Database
Create the necessary database tables.

Bash

python manage.py makemigrations
python manage.py migrate
6. Create an Admin User
You need a superuser account to manage the store inventory.

Bash

python manage.py createsuperuser
(Follow the prompts to set a Username, Email, and Password).

7. Run the Server
Start the development server.

Bash

python manage.py runserver
Open your browser and visit: http://127.0.0.1:8000/