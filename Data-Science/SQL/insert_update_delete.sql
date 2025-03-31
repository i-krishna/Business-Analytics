INSERT INTO employees (employee_id, first_name, last_name, email, hire_date)
VALUES (1001, 'John', 'Doe', 'john.doe@example.com', '2024-08-01');

UPDATE employees
SET email = 'john.newemail@example.com', hire_date = '2024-08-02'
WHERE employee_id = 1001;

DELETE FROM employees
WHERE employee_id = 1001;
