-- creating data base and a table with auto incremented primary key id
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa
USE hbtn_0d_usa
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);