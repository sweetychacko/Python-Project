import sqlite3

def create_db():
    conn=sqlite3.connect("Restaurant.db")
    print("Database created successfully")
    C=conn.cursor()
    C.execute(""" 
        CREATE TABLE User(
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(50) NOT NULL,
                password VARCHAR(100) UNIQUE,
                role VARCHAR(50))              
    """)
    C.execute(""" 
        CREATE TABLE Menus(
                item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name VARCHAR(50) NOT NULL,
                category VARCHAR(100),
                price REAL,
                is_available BOOLEAN DEFAULT 1)            
    """)
    C.execute(""" 
        CREATE TABLE Tables(
            table_id INTEGER PRIMARY KEY AUTOINCREMENT,
            table_no INTEGER,
            capacity INTEGER,
            status VARCHAR(50) NOT NULL)            
    """)

    C.execute(""" 
        CREATE TABLE Order_details(
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_status VARCHAR(20),
            total_amount REAL,
            order_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            user_id INTEGER NOT NULL,
            table_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES User(user_id),
            FOREIGN KEY (table_id) REFERENCES Tables (table_id))            
    """)
    C.execute(""" 
        CREATE TABLE OrderItems(
            orderitem_id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            item_id INTEGER NOT NULL,
            quantity INTEGER,
            FOREIGN KEY (order_id) REFERENCES Order_details(order_id),
            FOREIGN KEY (item_id) REFERENCES menus (item_id))            
    """)
    C.execute(""" ALTER TABLE Order_details ADD COLUMN feedback TEXT """)
    conn.commit()
    conn.close()
    print("Successfull")
# create_db()

def mainheading():
    # print("═══════════════════════════════════════════════")
    # print("                 GRILL & CHILL     ")
    # print("═══════════════════════════════════════════════")
    print("   ════════════════════ WELCOME TO THE GRILL & CHILL ════════════════════   ".center(20))
mainheading()

# Table User

from tabulate import tabulate
def view_user():
    conn=sqlite3.connect("Restaurant.db")
    C=conn.cursor()                   
    C.execute(""" SELECT * FROM User """)
    rows=C.fetchall()
    conn.commit()
    conn.close()
    print("------------------- USERS LIST-------------------")
    headers=["Roll No","Username","Password","Role"]
    print(tabulate(rows,headers,tablefmt="rounded_grid"))
# view_user()

def add_users(username,password,role):
    conn=sqlite3.connect("Restaurant.db")
    C=conn.cursor()
    C.execute("""
              INSERT INTO User(username,password,role) VALUES(?,?,?)
            """, (username,password,role))
    conn.commit()
    conn.close()
# username=input("Enter username:")
# password=input("Enter password:")
# role=input("Enter the role:")
# add_users(username,password,role)
# print("Successfull")

def update_user(username,password,role,user_id):
    conn=sqlite3.connect("Restaurant.db")
    C=conn.cursor()
    C.execute("""
              UPDATE User SET username=? , password=? , role=? WHERE user_id=?
            """, (username,password,role,user_id))
    conn.commit()
    conn.close()
# user_id=int(input("Enter user_id:"))
# username=input("Enter username:")
# password=input("Enter password:")
# role=input("Enter the role:")
# update_user(username,password,role,user_id)
# print("Successfull")

def delete_user(user_id):
    conn=sqlite3.connect("Restaurant.db")
    C=conn.cursor()
    C.execute("""
              DELETE FROM user WHERE user_id=?
            """, (user_id,))
    conn.commit()
    conn.close()
    
# user_id=int(input("Enter user_id:"))
# delete_user(user_id)
# print("Deleted Successfully")

# Table Menus

def view_items():
    conn=sqlite3.connect("Restaurant.db")
    C=conn.cursor()                   
    C.execute(""" SELECT * FROM Menus """)
    rows=C.fetchall()
    conn.commit()
    conn.close()
    print("--------------------------------- MENU---------------------------------")
    headers=["item_id","Item_name","category","price","is_available"]
    print(tabulate(rows,headers,tablefmt="rounded_grid"))
# view_items()

def add_items(item_name,category,price,is_available):
    conn=sqlite3.connect("Restaurant.db")
    C=conn.cursor()
    C.execute("""
              INSERT INTO Menus(item_name,
                category,price,is_available) VALUES(?,?,?,?)
            """, (item_name,category,price,is_available))
    conn.commit()
    conn.close()

# item_name=input("Enter the item name:")
# category=input("Enter the category of items:")
# price=int(input("Enter the Price:"))
# is_available=input("Enter the availability:")
# add_items(item_name,category,price,is_available)
# print("Item added successfully")

def update_items(item_name,category,price,is_available,item_id):
    conn=sqlite3.connect("Restaurant.db")
    C=conn.cursor()
    C.execute("""
                UPDATE Menus SET Item_name=? ,category=? ,price=? , is_available=? WHERE item_id=? """,
                (item_name,category,price,is_available,item_id))
    conn.commit()
    conn.close()
# item_id=int(input("Enter item id:"))
# item_name=input("Enter item name:")
# category=input("Enter category:")
# price=int(input("Enter price:"))
# is_available=input("Enter availability:")
# update_items(item_name,category,price,is_available,item_id)
# print("Item updated successfully")

def update_status_of_items(is_available,item_id):
    conn=sqlite3.connect("Restaurant.db")
    C=conn.cursor()
    C.execute("""
                UPDATE Menus SET is_available=? WHERE item_id=? """,
                (is_available,item_id))
    conn.commit()
    conn.close()
# item_id=int(input("Enter item id:"))
# is_available=input("Enter availability:")
# update_status_of_items(is_available,item_id)
# print("Item updated successfully")

def delete_items(item_id):
    conn=sqlite3.connect("Restaurant.db")
    C=conn.cursor()
    C.execute("""
              DELETE FROM Menus WHERE item_id=?
            """, (item_id,))
    conn.commit()
    conn.close()
# item_id=int(input("Enter item_id:"))
# delete_items(item_id)
# print("Deleted Successfully")


# Table Tables

def view_table_details():
    conn=sqlite3.connect("Restaurant.db")
    C=conn.cursor()                   
    C.execute(""" SELECT * FROM Tables """)
    rows=C.fetchall()
    conn.commit()
    conn.close()
    print("--------------------------------- Table Details---------------------------------")
    headers=["table_no","capacity","status"]
    print(tabulate(rows,headers,tablefmt="rounded_grid"))
# view_table_details()

def add_tables(table_no,
                capacity,status):
    conn=sqlite3.connect("Restaurant.db")
    C=conn.cursor()
    C.execute("""
              INSERT INTO Tables(table_no,
                capacity,status) VALUES(?,?,?)
            """, (table_no,capacity,status))
    conn.commit()
    conn.close()

# table_no=int(input("Enter the Table Number:"))
# capacity=int(input("Enter the capacity of the table:"))
# status=input("Enter the status:")
# add_tables(table_no,capacity,status)
# print("Table details added successfully")



def update_table_details(table_no,capacity,status,table_id):
    conn=sqlite3.connect("Restaurant.db")
    C=conn.cursor()
    C.execute("""
                UPDATE Tables SET table_no=? ,capacity=? ,status=? WHERE table_id=? """,
                (table_no,capacity,status,table_id))
    conn.commit()
    conn.close()
# table_id=int(input("Enter Table id:"))
# table_no=int(input("Enter Table Number:"))
# capacity=int(input("Enter capaity of the table:"))
# status=input("Enter Status:")
# update_table_details(table_no,capacity,status,table_id)
# print("Table Details updated successfully")


def delete_table(table_id):
    conn=sqlite3.connect("Restaurant.db")
    C=conn.cursor()
    C.execute("""
              DELETE FROM Tables WHERE table_id=?
            """, (table_id,))
    conn.commit()
    conn.close()
# table_id=int(input("Enter table_id:"))
# delete_table(table_id)
# print("Deleted Successfully")

# Table Order_details

def view_order_details():
    conn=sqlite3.connect("Restaurant.db")
    C=conn.cursor()                   
    C.execute(""" SELECT * FROM Order_details """)
    rows=C.fetchall()
    conn.commit()
    conn.close()
    print("--------------------------------- Order Details---------------------------------")
    headers=["Order_id","order_status","total_amount","Order Time","user_id","table_id","feedback"]
    print(tabulate(rows,headers,tablefmt="rounded_grid"))
# view_order_details()

def add_orders(user_id,table_id):
    conn=sqlite3.connect("Restaurant.db")
    C=conn.cursor()
    order_status = "Pending"
    total_amount = 0.0
    feedback = None
    C.execute("""
              INSERT INTO Order_details(order_status,total_amount,user_id,table_id,feedback)
                VALUES(?,?,?,?,?)
            """, (order_status,total_amount,user_id,table_id,feedback))
    C.execute(""" UPDATE Tables SET status = 'Occupied' WHERE table_id = ? """, (table_id,))
    conn.commit()
    conn.close()

# user_id=int(input("Enter the user_id:"))
# table_id=int(input("Enter the table_id:"))
# add_orders(user_id,table_id)
# print("Order details added successfully")


def update_status(order_status,order_id):
    conn=sqlite3.connect("Restaurant.db")
    C=conn.cursor()                   
    C.execute("""UPDATE Order_details SET order_status = ? WHERE order_id = ?""",
        (order_status,order_id))
    conn.commit()
    conn.close()
# order_id=int(input("Enter the Order_id:"))
# order_status=input("Enter the Order status:")
# update_status(order_status,order_id)

def update_order_details(order_status,total_amount,user_id,table_id,order_id):
    conn=sqlite3.connect("Restaurant.db")
    C=conn.cursor()
    C.execute("""
                UPDATE Order_details SET order_status=? ,total_amount=? ,user_id=? , table_id=? WHERE order_id=? """,
                (order_status,total_amount,user_id,table_id,order_id))
    conn.commit()
    conn.close()
# print("-------Please enter details to update:-------")
# order_id=int(input("Enter the order_id:"))
# order_status=input("Enter status of order:")
# total_amount=int(input("Enter Total Amount:"))
# user_id=int(input("Enter user_id:"))
# table_id=int(input("Enter table_id:"))
# update_order_details(order_status,total_amount,user_id,table_id,order_id)

#admin sales report
from datetime import datetime
def admin_sales_report(period="daily"):
    conn = sqlite3.connect("Restaurant.db")
    C = conn.cursor()
    now = datetime.now()
    current_month = now.strftime('%Y-%m') 
    current_year = now.strftime('%Y')    
    current_date = now.strftime('%Y-%m-%d')

    if period=="daily":
        C.execute(f""" SELECT SUM(total_amount) FROM Order_details WHERE order_status = "Paid" AND date(order_time) = "{current_date}" """)
    elif period=="monthly":
        C.execute(f""" SELECT SUM(total_amount) FROM Order_details WHERE order_status = "Paid" AND strftime('%Y-%m', order_time) = "{current_month}" """)
    elif period=="yearly":
        C.execute(f""" SELECT SUM(total_amount) FROM Order_details WHERE order_status = "Paid" AND strftime('%Y', order_time) = "{current_year}" """)
    result = C.fetchone()
    if result and result[0] is not None:
        total_revenue = result[0]
    else:
        total_revenue = 0.0
    print("\n" + "="*35)
    print("    RESTAURANT SALES REPORT    ")
    print("="*35)
    print(f"  {'Description':<20} | {'Value':<10}")
    print("-" * 35)
    print(f"  {'Total Revenue':<20} | ₹{total_revenue:>8.2f}")
    print("="*35)
# admin_sales_report()


def delete_orderdetails(order_id):
    conn=sqlite3.connect("Restaurant.db")
    C=conn.cursor()
    C.execute("""
              DELETE FROM Order_details WHERE order_id=?
            """, (order_id,))
    conn.commit()
    conn.close()
# print("-------Please enter details to update:-------")
# order_id=int(input("Enter order_id:"))
# delete_orderdetails(order_id)
# print("Deleted Successfully")

# Table Orderitems

def view_orderitems():
    conn=sqlite3.connect("Restaurant.db")
    C=conn.cursor()                   
    C.execute(""" SELECT * FROM orderitems """)
    rows=C.fetchall()
    conn.commit()
    conn.close()
    print("--------------------------------- Orderitems Details---------------------------------")
    headers=["Order_id","items_id","Quanity"]
    print(tabulate(rows,headers,tablefmt="rounded_grid"))
# view_orderitems()


def add_orderitems(order_id):
    while True:
        conn=sqlite3.connect("Restaurant.db")
        C=conn.cursor()
        item_id=int(input("Enter Item_id:"))
        quantity=int(input("Enter the Quantity:"))
        C.execute("""
                INSERT INTO orderitems(order_id,item_id,quantity)
                    VALUES(?,?,?)
                """, (order_id,item_id,quantity))
        conn.commit()
        more_items=input("Add another item? (y/n): ")
        if more_items.lower()=='n':
            break
    conn.close()
# order_id=int(input("Enter the Order_id:"))
# add_orderitems(order_id)
# print("Items added successfully")

def update_quantity_orderitems(quantity,orderitem_id,order_id,item_id):
    conn=sqlite3.connect("Restaurant.db")
    C=conn.cursor()
    C.execute("""
                UPDATE orderitems SET quantity=? WHERE orderitem_id=? AND order_id=? AND item_id=? """,
                (quantity,orderitem_id,order_id,item_id))
    conn.commit()
    conn.close()
# print("-------Please enter details to update:-------")
# orderitem_id=int(input("Enter the orderitem_id:"))
# order_id=int(input("Enter the order_id:"))
# item_id=int(input("Enter the item_id:"))
# quantity=int(input("Enter the quantity:"))
# update_quantity_orderitems(quantity,orderitem_id,order_id,item_id)
# print("Orderitems Details updated successfully")

def delete_orderitems(orderitem_id):
    conn=sqlite3.connect("Restaurant.db")
    C=conn.cursor()
    C.execute("""
              DELETE FROM orderitems WHERE orderitem_id=?
            """, (orderitem_id,))
    conn.commit()
    conn.close()
# print("-------Please enter details to delete:-------")
# orderitem_id=int(input("Enter the orderitem_id:"))
# delete_orderitems(orderitem_id)
# print("Deleted Successfully")

#Cashier
#bill details
def update_bill(order_id):     
    conn = sqlite3.connect("Restaurant.db")
    C = conn.cursor()
    C.execute(""" SELECT item_id, quantity FROM OrderItems WHERE order_id = ? """, (order_id,))
    items=C.fetchall()
    total_bill = 0
    for item_id, quantity in items:
        C.execute(""" SELECT price FROM Menus WHERE item_id = ? """, (item_id,))
        result = C.fetchone()
        if result:
            price = result[0]
            total_bill += (price * quantity)
    gst_rate = 0.05
    gst_amount = total_bill * gst_rate
    final_total = total_bill + gst_amount
    C.execute("""
        UPDATE Order_details SET total_amount = ? WHERE order_id = ? """, (total_bill, order_id,))
    conn.commit()
    print("\n" + "="*35)
    print("    Bill Breakdown    ")
    print("="*35)
    print(f" Order ID: {order_id}")
    print(f" Subtotal: ₹{total_bill:.2f}")
    print(f" GST (5%): ₹{gst_amount:.2f}")
    print(f" Grand Total: ₹{final_total:.2f}")
    conn.close()
# order_id=int(input("Enter your order_id:"))
# update_bill(order_id)


def cashier_Update_details(order_id):
    conn=sqlite3.connect("Restaurant.db")
    C=conn.cursor()
    C.execute("""
            UPDATE Order_details SET order_status = "Paid" WHERE order_id = ?
        """, (order_id,))
    C.execute(""" SELECT table_id FROM Order_details WHERE order_id = ?""", (order_id,))
    res=C.fetchone()
    if res and res[0] is not None:
        table_free = res[0]
        C.execute("""
            UPDATE Tables SET status = "Available" WHERE table_id = ? """, (table_free,))
        conn.commit()
        print(f" Table {table_free} is now available")
    else:
        print("There is no Order")    
    conn.commit()
    conn.close()
# order_id=int(input("Enter order_id:"))
# cashier_Update_details(order_id)


#customer feedback
def cust_feedback(order_id,feedback):
    conn=sqlite3.connect("Restaurant.db")
    C=conn.cursor()
    C.execute(""" UPDATE Order_details SET feedback = ? WHERE order_id = ? """,(feedback, order_id,))
    if C.rowcount == 0:
            print(" Order ID not found.")
    else:
        conn.commit()
        conn.close()
        print("Thank you! Feedback saved.") 
# order_id = input("Enter your Order ID: ")
# feedback = input("How was your experience? ")
# cust_feedback(order_id,feedback)

#customer_view_status
def customer_view_status(table_no):
    conn = sqlite3.connect("Restaurant.db")
    C = conn.cursor()
    C.execute(""" SELECT order_id, order_status FROM Order_details WHERE table_id = ? AND order_status != "Paid" """, (table_no,))
    order_data = C.fetchone() 
    if not order_data:
        print("No active orders for this table.")
        conn.close()
        return
    order_id = order_data[0]
    status = order_data[1]
    C.execute(""" SELECT item_id, quantity FROM OrderItems WHERE order_id = ? """, (order_id,))
    items_in_order = C.fetchall()

    print(f"\n Status for Table {table_no} is : {status}")
    for row in items_in_order:
        item_id = row[0]
        qty = row[1]        
        C.execute("SELECT item_name FROM Menus WHERE item_id = ?", (item_id,))
        item_name = C.fetchone()
        print(f" {item_name[0]} (Qty: {qty})")
    conn.close()
# table_no=int(input("Enter table number:"))
# customer_view_status(table_no)



#Admin
def admin_menu():
    while True:
        menu_data = [
                ["1", "Add User"],
                ["2", "View User"],
                ["3", "Update User"],
                ["4", "Delete User"],
                ["5", "Add Menu_details"],
                ["6", "View Menu_details"],
                ["7", "Update Menu_details"],
                ["8", "Delete Menu_details"],
                ["9", "Add Tables"],
                ["10", "View Tables"],
                ["11", "Update Tables"],
                ["12", "Delete Tables"],
                ["13", "View Order Details"],
                ["14", "View Sales Report"],
                ["15", "Exit"]
            ]
        print("\n" + "="*40)
        print("         ADMIN MENU         ")
        print("="*40)

        headers=["CHOICE","ACTION"]
        print(tabulate(menu_data,headers,tablefmt="fancy_grid"))
        try:

            choices=int(input("Enter your choice: "))
            if choices==1:
                username=input("Enter username:")
                password=input("Enter password:")
                role=input("Enter the role:")
                add_users(username,password,role)

            elif choices==2:
                view_user()
            elif choices==3:
                user_id=int(input("Enter user_id:"))
                username=input("Enter username:")
                password=input("Enter password:")
                role=input("Enter the role:")
                update_user(username,password,role,user_id)
            elif choices==4:
                user_id=int(input("Enter user_id:"))
                delete_user(user_id)
            elif choices==5:
                item_name=input("Enter the item name:")
                category=input("Enter the category of items:")
                price=int(input("Enter the Price:"))
                is_available=input("Enter the availability:")
                add_items(item_name,category,price,is_available)
            elif choices==6:
                view_items()
            elif choices==7:
                item_id=int(input("Enter item id:"))
                item_name=input("Enter item name:")
                category=input("Enter category:")
                price=int(input("Enter price:"))
                is_available=input("Enter availability:")
                update_items(item_name,category,price,is_available,item_id)
            elif choices==8:
                item_id=int(input("Enter item id:"))
                delete_items(item_id)
            elif choices==9:
                table_no=int(input("Enter the Table Number:"))
                capacity=int(input("Enter the capacity of the table:"))
                status=input("Enter the status:")
                add_tables(table_no,capacity,status)
            elif choices==10: 
                view_table_details()
            elif choices==11:
                table_id=int(input("Enter Table id:"))
                table_no=int(input("Enter Table Number:"))
                capacity=int(input("Enter capaity of the table:"))
                status=input("Enter Status:")
                update_table_details(table_no,capacity,status,table_id)
                print("Table Details updated successfully")
            elif choices==12:
                table_id=int(input("Enter table_id:"))
                delete_table(table_id)
            elif choices==13:
                view_order_details() 
            elif choices==14:
                print("\n--- Select Report Type ---")
                print("1. Daily Sales")
                print("2. Monthly Sales")
                print("3. Yearly Sales")                
                Admin_choice = input("Enter Choice (1-3): ")
                if Admin_choice == "1":
                    admin_sales_report("daily")
                elif Admin_choice == "2":
                    admin_sales_report("monthly")
                elif Admin_choice == "3":
                    admin_sales_report("yearly")
                else:
                    print("Invalid Choice!")
            else:    
                print("Exiting program. Goodbye!")
                break
        except ValueError:
            print(" Invalid Input! Please enter a proper choice.")

# admin_menu()    

#Waiter
def waiter_menu():
    while True:
        menu_data = [
                ["1", "View Tables"],
                ["2", "Add Order_details"],
                ["3", "Update Order_details"],
                ["4", "Delete Order_details"],
                ["5", "View Order_details"],
                ["6", "Add Orderitems"],
                ["7", "Update quantity of Orderitems"],
                ["8", "Delete OrderItems"],
                ["9", "View OrderItems"],
                ["10", "Update Table Details"],
                ["11", "Exit"]
            ]
        print("\n" + "="*40)
        print("         Waiter MENU         ")
        print("="*40)

        headers=["CHOICE","ACTION"]
        print(tabulate(menu_data,headers,tablefmt="fancy_grid"))
        try:
            choices=int(input("Enter your choice: "))
            if choices==1:
                view_table_details()
            elif choices==2:               
                user_id=int(input("Enter the user_id:"))
                table_id=int(input("Enter the table_id:"))
                add_orders(user_id,table_id)
            elif choices==3:
                print("-------Please enter details to update:-------")
                order_id=int(input("Enter the order_id:"))
                order_status=input("Enter status of order:")
                total_amount=int(input("Enter Total Amount:"))
                user_id=int(input("Enter user_id:"))
                table_id=int(input("Enter table_id:"))
                update_order_details(order_status,total_amount,user_id,table_id,order_id)
            elif choices==4:
                print("-------Please enter details to update:-------")
                order_id=int(input("Enter order_id:"))
                delete_orderdetails(order_id)
            elif choices==5:
                view_order_details()
            elif choices==6:
                print("-------Please enter Order Items details to add:-------")
                order_id=int(input("Enter the Order_id:"))
                add_orderitems(order_id)
                print("Items added successfully")
            elif choices==7:
                print("-------Please enter details to update:-------")
                orderitem_id=int(input("Enter the orderitem_id:"))
                order_id=int(input("Enter the order_id:"))
                item_id=int(input("Enter the item_id:"))
                quantity=int(input("Enter the quantity:"))
                update_quantity_orderitems(quantity,orderitem_id,order_id,item_id)
            elif choices==8:
                print("-------Please enter details to delete:-------")
                orderitem_id=int(input("Enter the orderitem_id:"))
                delete_orderitems(orderitem_id)
            elif choices==9:
                view_orderitems()  
            elif choices==10:
                print("-------Please enter details to update:-------")
                table_id=int(input("Enter Table id:"))
                table_no=int(input("Enter Table Number:"))
                capacity=int(input("Enter capaity of the table:"))
                status=input("Enter Status:")
                update_table_details(table_no,capacity,status,table_id)
            else:    
                print("Exiting program. Goodbye!")
                break
        except ValueError:
            print(" Invalid Input! Please enter a proper choice.")
# waiter_menu()

#Chef

def chef_menu():
    while True:
        menu_data = [
                ["1", "View Order_details"],
                ["2", "view_orderitems"],
                ["3","Update status of order items"],
                ["4", "View Menu"],
                ["5", "Update Menu"],
                ["6", "Exit"]
            ]
        print("\n" + "="*40)

        print("         CHEF MENU         ")
        print("="*40)

        headers=["CHOICE","ACTION"]
        print(tabulate(menu_data,headers,tablefmt="fancy_grid"))
        try:
            choices=int(input("Enter your choice: "))
            if choices==1:
                view_order_details()
            elif choices==2:
                view_orderitems()
            elif choices==3:
                order_id=int(input("Enter the Order_id:"))
                order_status=input("Enter the order_status:")
                update_status(order_status,order_id)
            elif choices==4:    
                view_items()
            elif choices==5:
                item_id=int(input("Enter item id:"))
                is_available=input("Enter availability:")
                update_status_of_items(is_available,item_id)
            else:    
                print("Exiting program. Goodbye!")
                break
        except ValueError:
            print(" Invalid Input! Please enter a proper choice.")

# chef_menu()

def cashier_menu():
    while True:
        menu_data = [
                ["1", "View Order_details"],
                ["2", "Update Table availability"],
                ["3", "View Table Details"],
                ["4", "Update Amount in the Bill"],
                ["5", "Exit"]
            ]
        print("\n" + "="*40)

        print("         CASHIER MENU         ")
        print("="*40)

        headers=["CHOICE","ACTION"]
        print(tabulate(menu_data,headers,tablefmt="fancy_grid"))
        try:
            choices=int(input("Enter your choice: "))
            if choices==1:
                view_order_details()
            elif choices==2:
                order_id=int(input("Enter order_id:"))
                cashier_Update_details(order_id)
            elif choices==3:
                view_table_details()
            elif choices==4:
                order_id=int(input("Enter order_id:"))
                update_bill(order_id)
            else:    
                print("Exiting program. Goodbye!")
                break
        except ValueError:
            print(" Invalid Input! Please enter a proper choice.")

# cashier_menu()

#Customer Menu

def customer_menu():
    while True:
        menu_data = [
                ["1", "View Menu"],
                ["2", "View Status of ordered items"],
                ["3", "view Bill"],
                ["4", "Feedback"],
                ["5", "Exit"]
            ]
        print("\n" + "="*40)
        print("         CUSTOMER MENU         ")
        print("="*40)

        headers=["CHOICE","ACTION"]
        print(tabulate(menu_data,headers,tablefmt="fancy_grid"))
        try:
            choices=int(input("Enter your choice: "))
            if choices==1:
                view_items()
            elif choices==2:
                table_no=int(input("Enter table number:"))
                customer_view_status(table_no)
            elif choices==3:
                order_id=int(input("Enter order_id:"))
                update_bill(order_id)
            elif choices==4:
                order_id = input("Enter your Order ID: ")
                feedback = input("How was your experience? ")
                cust_feedback(order_id,feedback)
            else:    
                print("Exiting program. Goodbye!")
                break
        except ValueError:
            print(" Invalid Input! Please enter a proper choice.")
# customer_menu()

#Main Menu- Login
def login():
    print("\n===== RESTAURANT LOGIN SYSTEM =====")
    username = input("Enter Username: ")
    password = input("Enter Password: ") 
    try:
        conn=sqlite3.connect("Restaurant.db")
        C=conn.cursor()
        C.execute(""" SELECT role FROM User WHERE username = ? AND password = ? """, (username, password))
        res = C.fetchone()
        conn.commit()
        conn.close()

        if res:
            role=str(res[0]).strip().lower()
            print(f"\nLogin Successful! Welcome, {username} ({role})")
            if role == "admin":
                admin_menu()
            elif role == "waiter":
                waiter_menu()
            elif role == "cashier":
                cashier_menu()
            elif role == "chef":
                chef_menu()
            elif role == "customer":
                customer_menu()
        else:
            print("\n Invalid Username or Password. Please try again.")       
    except Exception as e:
        print(f"\n an unexpected error: {e}")

login()
