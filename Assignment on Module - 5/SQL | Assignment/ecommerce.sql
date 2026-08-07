-- Active: 1786012263874@@127.0.0.1@5432@ecommerce_db
-- =====================================
-- SQL Assignment Project
-- Simple E-Commerce Database System
-- =====================================

-- =====================================
-- PART 1 : CREATE TABLES
-- =====================================

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    city VARCHAR(50)
);

CREATE TABLE Categories (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(50)
);

CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10,2),
    stock INT,
    category_id INT,
    FOREIGN KEY (category_id)
    REFERENCES Categories(category_id)
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (customer_id)
    REFERENCES Customers(customer_id)
);

-- =====================================
-- PART 2 : INSERT DATA
-- =====================================

-- Customers

INSERT INTO Customers (customer_id, name, email, phone, city)
VALUES
(1, 'Ahmed', 'ahmed@gmail.com', '01711111111', 'Dhaka'),
(2, 'Ayesha', 'ayesha@gmail.com', '01722222222', 'Chittagong'),
(3, 'Rahim', 'rahim@gmail.com', '01733333333', 'Dhaka'),
(4, 'Karim', 'karim@gmail.com', '01744444444', 'Khulna'),
(5, 'Sadia', 'sadia@gmail.com', '01755555555', 'Rajshahi');

-- Categories

INSERT INTO Categories (category_id, category_name)
VALUES
(1, 'Electronics'),
(2, 'Fashion'),
(3, 'Grocery'),
(4, 'Books'),
(5, 'Sports');

-- Products

INSERT INTO Products (product_id, product_name, price, stock, category_id)
VALUES
(1, 'Laptop', 85000, 10, 1),
(2, 'Smart Phone', 30000, 15, 1),
(3, 'Head Phone', 2500, 20, 1),
(4, 'T-Shirt', 700, 50, 2),
(5, 'Jeans', 1500, 25, 2),
(6, 'Rice Bag', 1800, 40, 3),
(7, 'Cooking Oil', 900, 35, 3),
(8, 'Python Book', 1200, 18, 4),
(9, 'Football', 1500, 12, 5),
(10, 'Cricket Bat', 3500, 8, 5);

-- Orders

INSERT INTO Orders (order_id, customer_id, order_date, total_amount)
VALUES
(1, 1, '2026-08-01', 85000),
(2, 2, '2026-08-01', 1500),
(3, 3, '2026-08-02', 30000),
(4, 4, '2026-08-02', 3500),
(5, 5, '2026-08-03', 900),
(6, 1, '2026-08-03', 2500),
(7, 2, '2026-08-04', 1800),
(8, 3, '2026-08-04', 1200);

-- =====================================
-- PART 3 : UPDATE DATA
-- =====================================

-- Update Laptop Price

UPDATE Products
SET price = 90000
WHERE product_name = 'Laptop';

-- Update Customer City

UPDATE Customers
SET city = 'Sylhet'
WHERE customer_id = 2;

-- Update Product Stock

UPDATE Products
SET stock = 9
WHERE product_name = 'Laptop';

-- =====================================
-- PART 4 : DELETE DATA
-- =====================================

-- Delete the order first because of the foreign key

DELETE FROM Orders
WHERE customer_id = 5;

-- Delete the customer

DELETE FROM Customers
WHERE customer_id = 5;

-- Delete one product

DELETE FROM Products
WHERE product_id = 10;

-- =====================================
-- PART 5 : BASIC QUERIES
-- =====================================

-- 1. Show all customers

SELECT * FROM Customers;

-- 2. Show all products

SELECT * FROM Products;

-- 3. Show products whose price is greater than 1000

SELECT *
FROM Products
WHERE price > 1000;

-- 4. Show products whose stock is less than 10

SELECT *
FROM Products
WHERE stock < 10;

-- 5. Show customers from Dhaka

SELECT *
FROM Customers
WHERE city = 'Dhaka';

-- 6. Sort products by price (Highest to Lowest)

SELECT *
FROM Products
ORDER BY price DESC;

-- 7. Sort customers alphabetically

SELECT *
FROM Customers
ORDER BY name ASC;

-- 8. Show the first 5 products

SELECT *
FROM Products
LIMIT 5;

-- 9. Count total customers

SELECT COUNT(*) AS total_customers
FROM Customers;

-- 10. Calculate the average product price

SELECT AVG(price) AS average_price
FROM Products;

-- =====================================
-- PART 6 : AGGREGATE FUNCTIONS
-- =====================================

-- Maximum product price

SELECT MAX(price) AS highest_price
FROM Products;

-- Minimum product price

SELECT MIN(price) AS lowest_price
FROM Products;

-- Total stock

SELECT SUM(stock) AS total_stock
FROM Products;

-- Average stock

SELECT AVG(stock) AS average_stock
FROM Products;

-- Total number of orders

SELECT COUNT(*) AS total_orders
FROM Orders;

-- =====================================
-- PART 7 : JOIN QUERIES
-- =====================================

-- 1. Show customer name and their orders

SELECT
    Customers.name,
    Orders.order_id,
    Orders.order_date,
    Orders.total_amount
FROM Customers
JOIN Orders
ON Customers.customer_id = Orders.customer_id;

-- 2. Show product name with category name

SELECT
    Products.product_name,
    Categories.category_name
FROM Products
JOIN Categories
ON Products.category_id = Categories.category_id;

-- 3. Show order details with customer name

SELECT
    Orders.order_id,
    Customers.name,
    Orders.order_date,
    Orders.total_amount
FROM Orders
JOIN Customers
ON Orders.customer_id = Customers.customer_id;

-- =====================================
-- PART 8 : SEARCH QUERIES
-- =====================================

-- Products containing the word "Phone"

SELECT *
FROM Products
WHERE product_name LIKE '%Phone%';

-- Customers whose name starts with "A"

SELECT *
FROM Customers
WHERE name LIKE 'A%';

-- Products priced between 500 and 3000

SELECT *
FROM Products
WHERE price BETWEEN 500 AND 3000;

-- =====================================
-- PART 9 : BONUS CHALLENGE
-- =====================================

-- 1. Which product has the highest price?

SELECT *
FROM Products
ORDER BY price DESC
LIMIT 1;

-- 2. Which customer placed the largest order?

SELECT
    Customers.name,
    Orders.total_amount
FROM Customers
JOIN Orders
ON Customers.customer_id = Orders.customer_id
ORDER BY Orders.total_amount DESC
LIMIT 1;

-- 3. How many products belong to each category?

SELECT
    Categories.category_name,
    COUNT(Products.product_id) AS total_products
FROM Categories
LEFT JOIN Products
ON Categories.category_id = Products.category_id
GROUP BY Categories.category_name;

-- 4. Which category has the most products?

SELECT
    Categories.category_name,
    COUNT(Products.product_id) AS total_products
FROM Categories
JOIN Products
ON Categories.category_id = Products.category_id
GROUP BY Categories.category_name
ORDER BY total_products DESC
LIMIT 1;

-- 5. List all customers who have placed at least one order

SELECT DISTINCT
    Customers.name
FROM Customers
JOIN Orders
ON Customers.customer_id = Orders.customer_id;

