CREATE DATABASE IF NOT EXISTS ctfdb;
USE ctfdb;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    password VARCHAR(255)
);

INSERT INTO users (username, password) VALUES ('administrator', 'supersecretWSU25');
