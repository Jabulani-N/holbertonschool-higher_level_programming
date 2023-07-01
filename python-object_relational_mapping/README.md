# Python - Object-relational mapping

In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project


* Your files will be executed with MySQLdb version 2.0.x
* Your files will be executed with SQLAlchemy version 1.4.x
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
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
        Install <code>MySQLdb</code> module version <code>2.0.x</code>
    </summary>
For installing MySQLdb, you need to have MySQL installed.
<br>
    $ sudo apt-get install python3-dev
    $ sudo apt-get install libmysqlclient-dev
    $ sudo apt-get install zlib1g-dev
    $ sudo pip3 install mysqlclient
    ...
    $ python3
    >>> import MySQLdb
    >>> MySQLdb.version_info
    (2, 0, 3, 'final', 0)

</details>

<details>
    <summary>
        Install <code>SQLAlchemy</code> module version <code>1.4.x</code>
    </summary>
    $ sudo pip3 install SQLAlchemy
    ...
    $ python3
    >>> import sqlalchemy
    >>> sqlalchemy.__version__
    '1.4.22'

</details>

Ignore this warning message if you get it:

    /usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
    moved in a future release.")
      cursor.execute(statement, parameters)

----

<details>
    <summary>
        To run the example test operations on your terminal within the container
    </summary>
    run
    <code>service mysql start</code><br>

your password can be skipped (Enter key) through

</details>


## task0

[steps to getting to write SQL scripts in pyhton](https://www.mikusa.com/python-mysql-docs/connection.html)

`import MySQLdb`

Afterwards, define a function, and put this in it:

`db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)`

* MY_HOST, MY_USER, MY_PASS, and MY_DB can be stirng variables, or actual string objects.

next, you'll need to create a cursor:

`cursorName = db.cursor()`

now, you can use that cursor to execute SQL queries. For example:

`cur.execute("CREATE TABLE song ( id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, title TEXT NOT NULL )")`

* Remember that SQL queries are one transaciton over one or multiple lines, and end with `;`. SQL doesn't see the newlines; it only sees and `;` as the end of a command.

finish with

```
if __name__ == '__main__':
    function_name()
```

Example insert:

    songs = ('Purple Haze', 'All Along the Watch Tower', 'Foxy Lady')
    for song in songs:
        cur.execute("INSERT INTO song (title) VALUES (%s)", song)
        print "Auto Increment ID: %s" % cur.lastrowid

Cleanup - do this within the python file when you are done with the cursor and database
```
    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
```

**testing**

`cat tests/0-select_states.sql | mysql -uroot -p;./0-select_states.py root root hbtn_0e_0_usa`

## Task1

SQL Wildcard characters: https://www.w3schools.com/sql/sql_wildcards.asp

### Potential Pitfall

* Be sure to use the correct wildcard for the service. `Wildcard Characters in SQL Server` is **not** the first option.

* Must be Case sensitive. `BINARY` is one way to do this. [Collate](https://stackoverflow.com/questions/14962419/is-the-like-operator-case-sensitive-with-sql-server) is another

**testing**

`cat tests/0-select_states.sql | mysql -uroot -p;./1-filter_states.py root root hbtn_0e_0_usa`

