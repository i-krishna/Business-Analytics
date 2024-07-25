-- Create an index on product_id
CREATE INDEX idx_product_id ON sales_data (product_id);

-- Create indexes on the partitions
CREATE INDEX idx_sales_2021_product_id ON sales_2021 (product_id);
CREATE INDEX idx_sales_2022_product_id ON sales_2022 (product_id);

-- Query with partition pruning and index usage

SELECT *
FROM sales_data
WHERE product_id = 123 AND sale_date BETWEEN '2021-01-01' AND '2021-12-31';
