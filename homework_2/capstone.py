CREATE TABLE employees (
    employee_id INT,
    employe_name VARCHAR(50),
    age INT,
    gender VARCHAR(10),
    department VARCHAR(30),
    job_title VARCHAR(40),
    salary INT,
    city VARCHAR(30),
    phone_no VARCHAR(15),
    email VARCHAR(50)
);

INSERT INTO employees VALUES
(101, 'Rahul Sharma', 28, 'Male', 'IT', 'Software Engineer', 65000, 'Mumbai', '9876543210', 'rahul@gmail.com'),
(102, 'Priya Mehta', 32, 'Female', 'HR', 'HR Manager', 72000, 'Delhi', '9876543211', 'priya@gmail.com'),
(103, 'Arjun Patel', 25, 'Male', 'Finance', 'Accountant', 48000, 'Mumbai', '9876543212', 'arjun@gmail.com'),
(104, 'Sneha Shah', 29, 'Female', 'IT', 'Web Developer', 58000, 'Pune', '9876543213', 'sneha@gmail.com'),
(105, 'Rohan Gupta', 35, 'Male', 'Sales', 'Sales Manager', 75000, 'Delhi', '9876543214', 'rohan@gmail.com'),
(106, 'Ananya Rao', 27, 'Female', 'IT', 'Software Engineer', 62000, 'Bangalore', '9876543215', 'ananya@gmail.com'),
(107, 'Karan Singh', 31, 'Male', 'Marketing', 'Marketing Executive', 51000, 'Mumbai', '9876543216', 'karan@gmail.com'),
(108, 'Isha Verma', 24, 'Female', 'Finance', 'Junior Accountant', 42000, 'Pune', '9876543217', 'isha@gmail.com'),
(109, 'Aditya Jain', 30, 'Male', 'Sales', 'Sales Executive', 46000, 'Mumbai', '9876543218', 'aditya@gmail.com'),
(110, 'Meera Nair', 26, 'Female', 'HR', 'HR Executive', 50000, 'Bangalore', '9876543219', 'meera@gmail.com');

SELECT * FROM employees;

SELECT employe_name, salary
FROM employees;

SELECT employe_name, department, job_title
FROM employees
WHERE department = 'IT';

SELECT *
FROM employees
WHERE salary > 60000;

SELECT *
FROM employees
WHERE city = 'Mumbai';

SELECT *
FROM employees
WHERE age < 30;

SELECT DISTINCT department
FROM employees;

SELECT DISTINCT city
FROM employees;

SELECT COUNT(employee_id)
FROM employees;

SELECT COUNT(employee_id)
FROM employees
WHERE department = 'IT';

SELECT SUM(salary)
FROM employees;

SELECT SUM(salary)
FROM employees
WHERE department = 'IT';

SELECT employe_name, salary
FROM employees
ORDER BY salary DESC;

SELECT employe_name, age
FROM employees
ORDER BY age;

SELECT employe_name, email, phone_no
FROM employees
WHERE gender = 'Female';

SELECT employe_name, job_title, salary
FROM employees
WHERE salary >= 50000;

SELECT employe_name, department
FROM employees
WHERE city = 'Mumbai';