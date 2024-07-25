-- Create a partitioned table by date (year)

CREATE TABLE sales_data (
  sale_id INT,
  sale_date DATE,
  product_id INT,
  sale_amount DECIMAL(10, 2)
)
PARTITION BY RANGE (YEAR(sale_date)) (
  PARTITION p_2020 VALUES LESS THAN (2021),
  PARTITION p_2021 VALUES LESS THAN (2022),
  PARTITION p_2022 VALUES LESS THAN (2023)
);
