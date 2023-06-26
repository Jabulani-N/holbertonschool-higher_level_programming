-- makes a table named after input argument. does nothing if it alraedy exists
IF NOT EXISTS first_table
    CREATE table first_table (
    id INT,
    name VARCHAR(256),
    )
