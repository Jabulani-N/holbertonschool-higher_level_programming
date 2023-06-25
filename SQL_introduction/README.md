# SQL - Introduction

This project utilizes **MySQL**

All SQL Queries must start with a comment just above

<details>
    <summary>
        Install MySQL 8.0 on Ubuntu 20.04 LTS
    </summary>
    <code>
        $ sudo apt update<br>
        $ sudo apt install mysql-server<br>
        ...<br>
        $ mysql --version<br>
        mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))<br>
        $<br>
    </code>
</details>

<details>
    <summary>
        Connect to your MySQL server:
    </summary>
        <code>
$ sudo mysql <br>
Welcome to the MySQL monitor.  Commands end with ; or \g.<br>
Your MySQL connection id is 11<br>
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)<br>

Copyright (c) 2000, 2021, Oracle and/or its affiliates.<br>

Oracle is a registered trademark of Oracle Corporation and/or its<br>
affiliates. Other names may be trademarks of their respective<br>
owners.<br>

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.<br>

mysql><br>
mysql> quit<br>
Bye<br>
$<br>
</code>
</details>

<details>
    <summary>
        To run the example test operations on your terminal within the container
    </summary>
    run
    <code>service mysql start</code>

your password will be "Database"


</details>
<details>
    <summary>
        Example test
    </summary>
    <code>cat 0-list_databases.sql | mysql -uroot -p</code>
</details>

* [MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)

* [SQL Query Structure](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/queries.php)
## Task1 - create database if it does not already exist

database creationo and conditional actions

*database creation*

`CREATE database databaseName`

*with conditional*

`CREATE database IF NOT EXISTS databaseName`

## Task2 - Database deletion

`DROP` is used to remove databases

## Task3 - List Tables

* The database name will be passed as argument of mysql command (in the following example: mysql is the name of the database)

**Write a script that lists all the tables of a database in your MySQL server.**

<details>
    <summary>
        Hint
    </summary>
The reason you probably can't find the command to get it to take an input command is that it doesn't need you to give it one.
</details>


