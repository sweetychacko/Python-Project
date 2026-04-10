# This is an application for a Restaturant Management system
# In this application,it manages everything from user authentication and table bookings to menu management, order processing, and sales reporting.
# There are 5 tables added here - Menus, Order_Details, OrderItems,Tables and User
# There are 5 roles in this system, they are admin,waiter,cashier,chef and customer
# Features under each role:
  **Admin**: Full control over users, menu items, table management, and detailed sales reports (Daily/Monthly/Yearly).
  **Waiter**: Manage live orders, link customers to tables, and update order items.
  **Chef**: View active orders and manage real-time item availability.
  **Cashier**: Process bills, calculate GST, and release tables for new customers.
  **Customer**: View the menu, check live order status, and provide feedback.
# Tables Details as follows: 
  **User**: Stores credentials and roles.
  **Menus**: Stores food items,category, prices, and availability.
  **Tables**: Tracks table capacity and status (Available/Occupied).
  **Order_details**: Header-level information for orders (Status, Total Amount,Order_Time, Feedback).
  **OrderItems**: Item details for every order.

# First create database using create_db()
# Manually add admin user to the user table and add each roles to the table
# Run the login script,login using credentials for each role and access to the particular roles for thier features
