# FreshMarket – Grocery Web Application

**FreshMarket** is a grocery e-commerce platform that provides a smooth shopping experience for local communities, enabling customers to browse fresh produce, manage their shopping cart, and conveniently place online orders. Store managers can efficiently manage inventory, track orders, and monitor business activity.

---

## 🛒 Key Features

### For Customers
- **Product Browsing:** Explore fresh groceries with high-quality images and clear descriptions.
- **Category Filtering:** Filter items by category such as *Fruits*, *Vegetables*, *Dairy*, etc.
- **Smart Cart:** Add products, update quantities, and get real-time pricing.
- **Secure Checkout:** Simple and intuitive order placement flow.
- **User Dashboard:** View order history and previously purchased items.
- **Authentication:** Custom login and registration pages with a clean UI.

### For Store Managers (Admin)
- **Inventory Management:** Full CRUD operations for products and categories.
- **Order Tracking:** View all orders, customer details, and payment/processing status.
- **Business Insights:** Access admin dashboards showing product counts, order stats, and recent system activity.

---

## 🛠 Technical Stack

- **Backend:** Django 5 (Python)
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Database:** SQLite (default for development)
- **Templating Engine:** Django Template Language (DTL)
- **Styling:** Custom CSS for a modern, fresh grocery-themed layout

---

## Screenshots

### Homepage  
![Homepage](screenshots\home.png)

### Admin page  
![Admin](screenshots\admin.PNG)

### Admin Dashboard page
![Admin dashboard](screenshots\admin_dashboard.PNG)

### Users page  
![Users](screenshots\user.PNG)

### Cart Page  
![Cart Page](screenshots\cart.PNG)
---

## ⚙️ Installation Guide

### 1. Prerequisites
Ensure Python is installed:
```bash
python --version
```

### 2. Clone the Repository

### 3. Create a Virtual Environment

**Windows:**
```bash
python -m venv env
env\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv env
source env/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Setup the Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Admin User
```bash
python manage.py createsuperuser
```

### 7. Run the Development Server
```bash
python manage.py runserver
```

Visit the app:  
👉 http://127.0.0.1:8000/

---

