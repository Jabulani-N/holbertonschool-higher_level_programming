-- Creartes a database in the SQL server if it does not already exist
IF DB_ID('hbtn_0c_0') IS NOT NULL
    -- in this case, we'll create the database
    CREATE database hbtn_0c_0
