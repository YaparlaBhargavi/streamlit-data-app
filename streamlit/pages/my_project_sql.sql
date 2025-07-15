-- 1. Create a new database (if not exists)
CREATE DATABASE railway;

-- 2. Switch to that database
USE railway;

-- 3. Create the signup_user table
CREATE TABLE  signup_us (
    username VARCHAR(120) UNIQUE,
    Full_name VARCHAR(255),
    phone VARCHAR(12),
    email VARCHAR(255),
    passwordd VARCHAR(255)
);

-- 4. Insert data into the table (replace values with real data)
INSERT INTO signup_us (username, Full_name, phone, email, passwordd)
VALUES ('your_username', 'Your Full Name', '9876543210', 'your@email.com', 'your_password');

-- 5. (Optional) View all data in the table
SELECT * FROM signup_us;
