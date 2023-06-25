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
</details>

<details>
    <summary>
        Some terminology around relational databases
    </summary>
    One good thing about relational databases is that whether they’re PostgreSQL, MySQL, Oracle, or other, they’ve managed to be pretty consistent across brands. Therefore, not only are their versions of SQL pretty decently similar (at least for CRUD operations), but the terminology they’re using are mostly the same.<br>

    Say you need to store users. To do that, you create a table that is called “users”.<br>

    Your users have 3 pieces of information to store: their “id”, their “login”, and their “password”. Those are called columns, and they all have types, like integer for the “id”, varchar(32) for “login” (a string of variable length, but maximum 32), and char(32) (a string of exactly 32 characters, which is the case for all text encrypted with the md5 algorithm, for instance). The available types may vary heavily from one database “brand” to the other.<br>

    Now, let’s add a user in the database with SQL:<br>
    <code>INSERT INTO users (login, password) VALUES ('rudy','01234567890123456789012345678901');</code><br>
    This adds a row in the table (sometimes also refered to as a record, or more rarely, a tuple).
</details>

<details>
    <summary>
        Some more terminology around relational databases
    </summary>
**Indexes**<br>
Say you want to get all of the comments that are attached to the post of ID 12:<br>

<code>SELECT * FROM comments WHERE post_id=12;</code><br>

If you have millions or billions of comments, having your database extract the comments that match this condition can be amazingly time-consuming. Therefore, you can add an index on the comments table, that applies to the post_id column. This will “precompute” every possible SELECT query with WHERE conditions on this column, which will update themselves every time you modify data, so that those calls are ready to respond very quickly.<br>

Let’s complicate things a bit, and say you want to optimize this query:<br>

<code>SELECT * FROM comments WHERE post_id=12 AND published=1;</code><br>

Your index on the post_id column might not help much on that query. However, for that query, you can absolutely define an index on multiple column (in this case, the columns post_id and published).

Setting indexes properly is a known quick win to improve performance of relational databases on queries that are performed very often and take a long time to respond (so-called slow queries). I can quote at least a dozen occurrences in my career where setting up an index properly boosted a database’s performance with minimal effort, the most notable of which allowed us to boost a data migration that was taking ~48 hours, to suddenly complete in about 3 hours.<br>

**Joins**<br>

You can join tables together that have relations between each other, so that you can operate on data across those tables. For instance, I want the titles of all posts that have published comments.<br>

You can join tables together that have relations between each other, so that you can operate on data across those tables. For instance, I want the titles of all posts that have published comments.<br>

<code>SELECT posts.title FROM posts JOIN comments ON posts.id = comments.post_id WHERE comments.published=1;</code><br>

(Note: each post on that query will appear as many times as it has comments, but let’s focus on the join for now.)<br>

Performance is dramatically better if you manage to get the database to do most of the work, as opposed to your application, because the database knows most about your data and how to handle it most efficiently. Joins are amazing wins for that, because the other way to get it done is to perform many separate SQL queries, and manipulate that data in your code, which is very inefficient.<br>

Note: you can join tables together across many relations. The largest join in my career was 7-fold, in a database at Apple that contained information about localization projects.<br>
</details>

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


