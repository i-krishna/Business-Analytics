-- Split the 1nf table further by moving product information to a separate table.

-- Create products table
CREATE TABLE products (
  product_id INT PRIMARY KEY,
  product_name VARCHAR(255)
);

-- Update order_items table
CREATE TABLE order_items (
  order_id INT,
  product_id INT,
  quantity INT,
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);
