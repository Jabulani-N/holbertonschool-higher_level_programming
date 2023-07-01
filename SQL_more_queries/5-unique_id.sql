-- Write a script that creates the table unique_id on your MySQL server.
CREATE TABLE IF NOT EXISTS force_name (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256) NOT NULL
);
