import sys
import os

# Ensure the parent directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.product import Product
from models.sale import Sale
from models.expense import Expense
from database.connection import session

def main_menu():
    while True:
        print("\n📌 SMART INVENTORY SYSTEM 📌")
        print("1. Manage Inventory")
        print("2. Record a Sale")
        print("3. Track Expenses")
        print("4. View Reports")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            inventory_menu()
        elif choice == "2":
            record_sale()
        elif choice == "3":
            track_expenses()
        elif choice == "4":
            view_reports()
        elif choice == "5":
            print("Exiting... Goodbye!")
            session.close()
            sys.exit()
        else:
            print("Invalid choice! Please enter a number between 1-5.")

def inventory_menu():
    while True:
        print("\n🔹 INVENTORY MANAGEMENT 🔹")
        print("1. Add a Product")
        print("2. View All Products")
        print("3. Update Stock")
        print("4. Delete a Product")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            update_stock()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please enter a number between 1-5.")

def add_product():
    name = input("Enter product name: ").strip()
    category = input("Enter product category: ").strip()
    price = input("Enter product price (Ksh): ").strip()
    stock_quantity = input("Enter stock quantity: ").strip()

    if not name or not category or not price.isdigit() or not stock_quantity.isdigit():
        print("Invalid input! Please enter correct values.")
        return

    price = float(price)
    stock_quantity = int(stock_quantity)

    existing_product = session.query(Product).filter_by(name=name).first()
    if existing_product:
        print("Product already exists!")
        return

    new_product = Product(name=name, category=category, price=price, stock_quantity=stock_quantity)
    session.add(new_product)
    session.commit()
    print(f"✅ Product '{name}' added successfully!")

def view_products():
    products = session.query(Product).all()
    if not products:
        print("No products found.")
        return

    print("\n📦 PRODUCT LIST 📦")
    for product in products:
        print(f"{product.id}. {product.name} - {product.category} - Ksh {product.price} - Stock: {product.stock_quantity}")

def update_stock():
    product_id = input("Enter product ID to update stock: ").strip()
    quantity = input("Enter new stock quantity: ").strip()

    if not product_id.isdigit() or not quantity.isdigit():
        print("Invalid input! Please enter correct values.")
        return

    product = session.query(Product).filter_by(id=int(product_id)).first()
    if not product:
        print("Product not found!")
        return

    product.stock_quantity = int(quantity)
    session.commit()
    print(f"✅ Stock updated for '{product.name}'!")

def delete_product():
    product_id = input("Enter product ID to delete: ").strip()

    if not product_id.isdigit():
        print("Invalid input! Please enter a valid product ID.")
        return

    product = session.query(Product).filter_by(id=int(product_id)).first()
    if not product:
        print("Product not found!")
        return

    session.delete(product)
    session.commit()
    print(f"✅ Product '{product.name}' deleted successfully!") 

def record_sale():
    print("\n🛒 RECORD A SALE 🛒")
    product_id = input("Enter product ID: ").strip()
    quantity_sold = input("Enter quantity sold: ").strip()

    if not product_id.isdigit() or not quantity_sold.isdigit():
        print("Invalid input! Please enter correct values.")
        return

    product = session.query(Product).filter_by(id=int(product_id)).first()
    if not product:
        print("Product not found!")
        return

    quantity_sold = int(quantity_sold)
    if product.stock_quantity < quantity_sold:
        print("❌ Not enough stock available!")
        return

    total_price = quantity_sold * product.price
    new_sale = Sale(product_id=product.id, quantity_sold=quantity_sold, total_price=total_price)
    product.stock_quantity -= quantity_sold  # Deduct stock
    session.add(new_sale)
    session.commit()

    print(f"✅ Sale recorded! Sold {quantity_sold} x {product.name} for Ksh {total_price}. Stock updated.") 

def track_expenses():
    while True:
        print("\n💰 EXPENSE TRACKING 💰")
        print("1. Add an Expense")
        print("2. View All Expenses")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            break
        else:
            print("Invalid choice! Please enter a number between 1-3.")

def add_expense():
    category = input("Enter expense category (e.g., Rent, Utilities, Supplies): ").strip()
    amount = input("Enter expense amount (Ksh): ").strip()
    description = input("Enter description (optional): ").strip()

    if not category or not amount.replace(".", "").isdigit():
        print("Invalid input! Please enter correct values.")
        return

    amount = float(amount)
    
    new_expense = Expense(category=category, amount=amount, description=description)
    session.add(new_expense)
    session.commit()

    print(f"✅ Expense of Ksh {amount} added under '{category}' category.")

def view_expenses():
    expenses = session.query(Expense).all()
    if not expenses:
        print("No expenses found.")
        return

    print("\n💵 EXPENSE LIST 💵")
    for expense in expenses:
        print(f"{expense.id}. {expense.category} - Ksh {expense.amount} - {expense.description} - {expense.date.strftime('%Y-%m-%d')}")

def view_reports():
    while True:
        print("\n📊 REPORTS & INSIGHTS 📊")
        print("1. View Total Revenue")
        print("2. View Total Expenses")
        print("3. View Profit & Loss")
        print("4. Best-Selling Products")
        print("5. Top Expense Categories")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            total_revenue()
        elif choice == "2":
            total_expenses()
        elif choice == "3":
            profit_loss()
        elif choice == "4":
            best_selling_products()
        elif choice == "5":
            top_expense_categories()
        elif choice == "6":
            break
        else:
            print("Invalid choice! Please enter a number between 1-6.")

def total_revenue():
    revenue = session.query(Sale).all()
    total = sum(sale.total_price for sale in revenue)
    print(f"\n💰 Total Revenue: Ksh {total}")

def total_expenses():
    expenses = session.query(Expense).all()
    total = sum(exp.amount for exp in expenses)
    print(f"\n📉 Total Expenses: Ksh {total}")

def profit_loss():
    revenue = session.query(Sale).all()
    total_revenue = sum(sale.total_price for sale in revenue)

    expenses = session.query(Expense).all()
    total_expenses = sum(exp.amount for exp in expenses)

    profit = total_revenue - total_expenses
    print(f"\n📈 Profit/Loss Calculation: Ksh {profit}")

def best_selling_products():
    from sqlalchemy.sql import func

    best_products = session.query(Product.name, func.sum(Sale.quantity_sold).label("total_sold")) \
        .join(Sale) \
        .group_by(Product.name) \
        .order_by(func.sum(Sale.quantity_sold).desc()) \
        .limit(5) \
        .all()

    if not best_products:
        print("No sales data available.")
        return

    print("\n🏆 BEST-SELLING PRODUCTS 🏆")
    for product, total_sold in best_products:
        print(f"{product} - {total_sold} units sold")

def top_expense_categories():
    from sqlalchemy.sql import func

    top_expenses = session.query(Expense.category, func.sum(Expense.amount).label("total_spent")) \
        .group_by(Expense.category) \
        .order_by(func.sum(Expense.amount).desc()) \
        .limit(5) \
        .all()

    if not top_expenses:
        print("No expense data available.")
        return

    print("\n💸 TOP EXPENSE CATEGORIES 💸")
    for category, total_spent in top_expenses:
        print(f"{category} - Ksh {total_spent}")

if __name__ == "__main__":
    main_menu()
