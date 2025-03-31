-- Split unnormalized table into separate tables for customers and orders.

-- Create customers table
CREATE TABLE customers (
  customer_id INT PRIMARY KEY,
  customer_name VARCHAR(255),
  customer_address VARCHAR(255)
);

-- Create orders table
CREATE TABLE orders (
  order_id INT PRIMARY KEY,
  customer_id INT,
  order_date DATE,
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Create order_items table
CREATE TABLE order_items (
  order_id INT,
  product_name VARCHAR(255),
  quantity INT,
  FOREIGN KEY (order_id) REFERENCES orders(order_id)
);
