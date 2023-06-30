# SQL - More queries

As of 2023 June 27, these files may not run correctly, depending on SQL version installed. Ubuntu 14.14 systems may fail where Ubuntu 20.04 systems succeed.

## Potemtial pitfalls

* There is no such things as `exists`. The keyword is `EXISTS`
* * need review

This project utilizes **MySQL**

All SQL Queries must start with a comment just above


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

## Task0 -

you can use `SHOW GRANTS` on a user to see their permissions

## Task1 - Root user

article on creating users and granthing them permissions: https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql



<details>
    <summary>
        syntax hint
    </summary>
    <code>DO SOMETHING IF CONDITION details of the something to do;</code>
</details>

<details>
    <summary>
        syntax answer
    </summary>
    <code>CREATE USER IF NOT exists 'username' IDENTIFIED WITH mysql_native_password BY 'password';</code>
</details>

**testing**

`cat 1-create_user.sql | mysql -hlocalhost -uroot -p;cat 0-privileges.sql | mysql -hlocalhost -uroot -p`

* successful code will fill the terminal with a spam of words, prefaced by <mark>Grants for user_0d_1@localhost</mark>

## Task2

changing permissions syntax

* `GRANT/REVOKE PRIVILEGEnAME ON SERVERnAME.SERVERcONTENT TO/FROM USERnAME`

* * `ALL PRIVILEGES` is a valid privilege name, for affecting all privileges.

**Testing**

`cat 2-create_read_user.sql | mysql -hlocalhost -uroot -p;cat 0-privileges.sql | mysql -hlocalhost -uroot -p`
