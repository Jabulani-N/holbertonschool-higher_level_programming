# Python - Object-relational mapping

In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project

----

This project utilizes **MySQL**


<details>
    <summary>
        Install MySQL 8.0 on Ubuntu 20.04 LTS
    </summary>
        $ sudo apt update
        $ sudo apt install mysql-server
        ...
        $ mysql --version
        mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
        $
</details>

<details>
    <summary>
        Connect to your MySQL server:
    </summary>

    $ sudo mysql
    Welcome to the MySQL monitor.  Commands end with ; or \g.
    Your MySQL connection id is 11
    Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

    Copyright (c) 2000, 2021, Oracle and/or its affiliates.

    Oracle is a registered trademark of Oracle Corporation and/or its
    affiliates. Other names may be trademarks of their respective
    owners.

    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

    mysql>
    mysql> quit
    Bye
    $
</details>

<details>
    <summary>
        To run the example test operations on your terminal within the container
    </summary>
    run
    <code>service mysql start</code><br>

your password can be skipped (Enter key) through

</details>

