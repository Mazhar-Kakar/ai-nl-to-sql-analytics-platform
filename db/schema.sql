-- ===============================================================================
-- DATABASE SETUP 
-- =============================================================================== 
-- NOTE: PLEAS IMPORT DATA MANUALLY IN TEH EXISTING TABLE CREATIONS SEQUENCE PARENT TABLE FIRST, BECAUSE OF FOREIGN KEY CONSTRAINTS

-- CREATE NEW DATABASE
CREATE DATABASE sales_db;
USE sales_db;

/*
CREATE SIX TABLES:
    - departments
    - category
    - products
    - customers
    - orders
    - order_items
*/

-- ---------------------------------------------------------------------------------
-- ER DIAGRAM
-- ---------------------------------------------------------------------------------

/*
+---------------------+
|      Customers      |
+---------------------+
| CustomerID (PK)     |
| CustomerName        |
| Email               |
| Phone               |
| Address             |
+---------------------+
          |
          | 1
          |
          | M
+---------------------+
|        Orders       |
+---------------------+
| OrderID (PK)        |
| CustomerID (FK)     |
| OrderDate           |
| TotalAmount         |
| Status              |
+---------------------+
          |
          | 1
          |
          | M
+---------------------+
|     Order_Items     |
+---------------------+
| OrderItemID (PK)    |
| OrderID (FK)        |
| ProductID (FK)      |
| Quantity            |
| UnitPrice           |
+---------------------+
          |
          | M
          |
          | 1
+---------------------+
|       Products      |
+---------------------+
| ProductID (PK)      |
| ProductName         |
| CategoryID (FK)     |
| Price               |
+---------------------+
          |
          | M
          |
          | 1
+---------------------+
|      Categories     |
+---------------------+
| CategoryID (PK)     |
| CategoryName        |
| DepartmentID (FK)   |
+---------------------+
          |
          | M
          |
          | 1
+---------------------+
|     Departments     |
+---------------------+
| DepartmentID (PK)   |
| DepartmentName      |
+---------------------+
*/


CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100)
);

-- ---------------------------------------------------------------------------------
CREATE TABLE category (
    category_id INT PRIMARY KEY,
    category_department_id INT,
    category_name VARCHAR(100),
    CONSTRAINT category_department_idFK 
    FOREIGN KEY (category_department_id) 
    REFERENCES departments(department_id)
);

-- ---------------------------------------------------------------------------------
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_category_id INT,
    product_name VARCHAR(150),
    product_description TEXT,
    product_price DECIMAL(10,2),
    product_image VARCHAR(255),
    CONSTRAINT product_category_idFK 
    FOREIGN KEY (product_category_id) 
    REFERENCES category(category_id)
);

-- ---------------------------------------------------------------------------------
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_fname VARCHAR(50),
    customer_lname VARCHAR(50),
    customer_email VARCHAR(100),
    customer_phone VARCHAR(20),
    customer_address VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(100),
    pincode INT
);

-- ---------------------------------------------------------------------------------
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    order_date DATE,
    customer_id INT,
    order_status VARCHAR(50),
    CONSTRAINT customer_idFK 
    FOREIGN KEY (customer_id) 
    REFERENCES customers(customer_id)
);

-- ---------------------------------------------------------------------------------
CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    total_amount DECIMAL(10,2),
    price DECIMAL(10,2),
    CONSTRAINT order_idFK 
    FOREIGN KEY (order_id) 
    REFERENCES orders(order_id),
    CONSTRAINT product_idFK 
    FOREIGN KEY (product_id) 
    REFERENCES products(product_id)
);

-- ---------------------------------------------------------------------------------
SELECT * FROM departments;
SELECT * FROM category;
SELECT * FROM products;
SELECT * FROM customers;
SELECT * FROM orders;
SELECT * FROM order_items;