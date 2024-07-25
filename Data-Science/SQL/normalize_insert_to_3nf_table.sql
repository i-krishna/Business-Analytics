-- Create customers table
CREATE TABLE customers (
  customer_id INT PRIMARY KEY,
  customer_name VARCHAR(255),
  customer_address VARCHAR(255)
);

-- Create products table
CREATE TABLE products (
  product_id INT PRIMARY KEY,
  product_name VARCHAR(255)
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
  product_id INT,
  quantity INT,
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Insert sample data
INSERT INTO customers (customer_id, customer_name, customer_address)
VALUES
  (1, 'John Smith', '123 Main St'),
  (2, 'Jane Doe', '456 Elm St');

INSERT INTO products (product_id, product_name)
VALUES
  (1, 'Product A'),
  (2, 'Product B'),
  (3, 'Product C');

INSERT INTO orders (order_id, customer_id, order_date)
VALUES
  (1, 1, '2022-01-01'),
  (2, 1, '2022-01-15'),
  (3, 2, '2022-02-01');

INSERT INTO order_items (order_id, product_id, quantity)
VALUES
  (1, 1, 2),
  (2, 2, 1),
  (3, 3, 3);
