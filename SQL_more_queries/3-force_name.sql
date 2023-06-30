-- script that creates the table force_name on your MySQL server
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
ALTER TABLE force_name
DROP CONSTRAINT PK_id;
