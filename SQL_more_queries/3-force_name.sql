-- script that creates the table force_name on your MySQL server
DROP TABLE IF EXISTS force_name;
CREATE TABLE IF NOT EXISTS force_name (
    id INT UNIQUE,
    name VARCHAR(256) NOT NULL
);
