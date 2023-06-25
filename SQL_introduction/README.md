# SQL - Introduction

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
    <code>
service mysql start
    </code>

your password will be "Database"

    <details>
        <summary>
            Example test
        </summary>
        <code>
cat 0-list_databases.sql | mysql -uroot -p
        </code>
    </details>
</details>

## Task1 - create database if it does not already exist

[conditional actions](https://stackoverflow.com/questions/19088368/conditionally-create-stored-procedure-using-tsql)

