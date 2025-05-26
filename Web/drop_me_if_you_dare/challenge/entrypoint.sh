#!/bin/sh

# Secure entrypoint
# Initialize & Start MariaDB
mkdir -p /run/mysqld
chown -R mysql:mysql /run/mysqld
mysql_install_db --user=mysql --ldata=/var/lib/mysql
mysqld --user=mysql --console --skip-networking=0 &

# Wait for mysql to start
while ! mysqladmin ping -h'localhost' --silent; do echo 'not up' && sleep .2; done

mysql -u root << EOF

CREATE DATABASE IF NOT EXISTS ctfdb;

CREATE TABLE IF NOT EXISTS ctfdb.users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    password VARCHAR(255)
);

CREATE USER 'WSUuser'@'localhost' IDENTIFIED BY 'WayneStateUniversity';
GRANT ALL ON *.* TO 'WSUuser'@'localhost';

INSERT INTO ctfdb.users (username, password) VALUES ('administrator', 'supersecretWSU25');
FLUSH PRIVILEGES;
EOF

node /app/src/app.js