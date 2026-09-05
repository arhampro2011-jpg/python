CREATE TABLE customers (
    customer_id INT,
    customer_name VARCHAR(50),
    city VARCHAR(30),
    country VARCHAR(30),
    product_name VARCHAR(50),
    product_type VARCHAR(30),
    quantity INT,
    price INT,
    export_country VARCHAR(30)
);

INSERT INTO customers VALUES
(201, 'Arjun Mehta', 'Mumbai', 'India', 'Laptop', 'Electronics', 5, 60000, 'USA'),
(202, 'Aarav Shah', 'Delhi', 'India', 'Mobile Phone', 'Electronics', 10, 30000, 'Canada'),
(203, 'Rohan Verma', 'Pune', 'India', 'Office Chair', 'Furniture', 8, 12000, 'Australia'),
(204, 'Ananya Rao', 'Mumbai', 'India', 'Keyboard', 'Electronics', 15, 3000, 'USA'),
(205, 'Karan Malhotra', 'Bangalore', 'India', 'Desk', 'Furniture', 6, 15000, 'Germany'),
(206, 'Aditya Kapoor', 'Chennai', 'India', 'Headphones', 'Electronics', 12, 5000, 'France'),
(207, 'Priya Nair', 'Mumbai', 'India', 'Monitor', 'Electronics', 7, 18000, 'Japan'),
(208, 'Rahul Arora', 'Delhi', 'India', 'Printer', 'Electronics', 4, 22000, 'USA'),
(209, 'Aman Singh', 'Pune', 'India', 'Table Lamp', 'Home', 20, 2500, 'Canada'),
(210, 'Saurabh Joshi', 'Mumbai', 'India', 'Notebook', 'Stationary', 30, 500, 'Australia');

SELECT * FROM customers;

SELECT customer_name, city, country
FROM customers;

SELECT customer_name, product_name, quantity
FROM customers
WHERE customer_name LIKE 'A%';

SELECT customer_name, product_name
FROM customers
WHERE customer_name LIKE '%or%';

SELECT customer_name, city, product_name
FROM customers
WHERE customer_name LIKE 'A%'
AND customer_name LIKE '%or%';

SELECT DISTINCT export_country
FROM customers;

SELECT DISTINCT product_name
FROM customers;

SELECT DISTINCT product_type
FROM customers;

SELECT COUNT(customer_id)
FROM customers;

SELECT COUNT(customer_id)
FROM customers
WHERE export_country = 'USA';

SELECT SUM(quantity)
FROM customers;

SELECT SUM(price)
FROM customers;

SELECT customer_name, product_name, export_country
FROM customers
WHERE export_country = 'USA';

SELECT customer_name, product_name, export_country
FROM customers
WHERE export_country = 'Canada';

SELECT customer_name, product_name, quantity
FROM customers
WHERE quantity > 10;

SELECT customer_name, product_name, price
FROM customers
WHERE price > 10000;

SELECT customer_name, product_name, export_country
FROM customers
ORDER BY customer_name;

SELECT customer_name, product_name, quantity
FROM customers
ORDER BY quantity DESC;

SELECT customer_name, product_name, export_country
FROM customers
WHERE product_name LIKE '%Phone%';

SELECT customer_name, product_name, export_country
FROM customers
WHERE product_name LIKE '%or%';