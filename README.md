# Smart Inventory & Expense System

## 📌 Project Overview
The **Smart Inventory & Expense System** is a Python-based **Command-Line Interface (CLI)** application designed for small businesses to efficiently manage inventory, record sales, track expenses, and generate insightful financial reports.

This system uses **SQLAlchemy ORM** for database management and follows **Object-Oriented Programming (OOP) best practices** to ensure modularity and scalability.

---
## 🚀 Features

### 1️⃣ **Inventory Management**
- ✅ Add new products with **name, price, stock quantity, and category**
- ✅ Update **stock levels** when items are **sold or restocked**
- ✅ View **all available products**
- ✅ Delete products when needed

### 2️⃣ **Sales Recording**
- ✅ Record **sales transactions** (automatically reducing stock)
- ✅ Track **total revenue and profit margins**

### 3️⃣ **Expense Tracking**
- ✅ Log expenses with **category, amount, and description**
- ✅ View **total expenses** per **day, week, or month**
- ✅ Generate **expense reports by category**

### 4️⃣ **Reports & Insights**
- ✅ Show **total revenue** from sales
- ✅ Display **total expenses**
- ✅ Calculate **profit or loss** (Revenue - Expenses)
- ✅ Identify **best-selling products**
- ✅ Show **top expense categories**

---
## 📂 Project Structure
```
smart_inventory/
│── cli/
│   │── main_menu.py      # Main CLI menu logic
│── database/
│   │── connection.py     # Database setup and connection
│── models/
│   │── product.py        # Product Model (Inventory Management)
│   │── sale.py           # Sale Model (Sales Transactions)
│   │── expense.py        # Expense Model (Expense Tracking)
│── database_setup.py     # Database initialization script
│── Pipfile               # Dependency management (Pipenv)
│── README.md             # Project Documentation
```

---
## 🛠️ Installation & Setup
### **Step 1: Clone the Repository**
```sh
git clone https://github.com/edwin463/smart_inventory.git
cd smart_inventory
```

### **Step 2: Set Up Virtual Environment** (Using Pipenv)
```sh
pip install pipenv
pipenv install
pipenv shell  # Activate the virtual environment
```

### **Step 3: Initialize the Database**
```sh
python database_setup.py
```

---
## 🚀 How to Use
Run the CLI application with:
```sh
python cli/main_menu.py
```

### **📌 CLI Menu Options**
- **1: Manage Inventory** → Add, View, Update, Delete products
- **2: Record a Sale** → Log sales and update stock
- **3: Track Expenses** → Add and view business expenses
- **4: View Reports** → Check revenue, expenses, profit/loss, and top-selling products
- **5: Exit** → Quit the application

---
## 🛠️ Technologies Used
- **Python** (Core logic)
- **SQLAlchemy ORM** (Database management)
- **Pipenv** (Dependency management)

---
## 📌 Future Improvements
- ✅ Implement **User Authentication**
- ✅ Add **Export Reports (CSV, PDF)**
- ✅ Develop a **Graphical User Interface (GUI)**

---
## 📜 License
This project is open-source and free to use under the **MIT License**.

---
## 📞 Contact
For any questions or contributions, feel free to reach out:
📧 **Email:** eliudedwin5@gmail.com  
🐙 **GitHub:** [Your GitHub](https://github.com/edwin463)

