mysql> CREATE DATABASE mydatabase;
Query OK, 1 row affected (0.00 sec)

mysql> USE mydatabase;
Database changed
mysql> CREATE TABLE students (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     name VARCHAR(50),
    ->     age INT
    -> );
Query OK, 0 rows affected (0.01 sec)

mysql> INSERT INTO students (name, age) VALUES ('Alice', 20);INSERT INTO students (name, age) VALUES ('kang', 22);INSERT INTO students (name, age) VALUES ('xiao ming', 19);
Query OK, 1 row affected (0.00 sec)

Query OK, 1 row affected (0.00 sec)

Query OK, 1 row affected (0.00 sec)

mysql> SELECT * FROM students;
+----+-----------+------+
| id | name      | age  |
+----+-----------+------+
|  1 | Alice     |   20 |
|  2 | kang      |   22 |
|  3 | xiao ming |   19 |
+----+-----------+------+
3 rows in set (0.00 sec)

mysql> SELECT * FROM students WHERE age > 20;
+----+------+------+
| id | name | age  |
+----+------+------+
|  2 | kang |   22 |
+----+------+------+
1 row in set (0.00 sec)
