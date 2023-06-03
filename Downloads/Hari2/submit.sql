-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS submit;

-- Use the database
USE submit;

-- Create the table if it doesn't exist
CREATE TABLE IF NOT EXISTS details (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    mobile INT(13) NOT NULL ,
    email VARCHAR(255) NOT NULL,
    message TEXT
);
