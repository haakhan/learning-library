# DATABASE DESIGN - MYSQL TABLES 

## Introduction

4a) Database Design
Objective: Working with SQL
Server: serverB


Estimated Lab Time: -- minutes


### Objectives

In this lab, you will:
* Create tables
* Create index
* Handle statistics

### Prerequisites (Optional)

This lab assumes you have:
* An Oracle account
* All previous labs successfully completed

**Server:** serverB

## Task 1: Create tables

1.	Now the lab start: connect to your mysql-advanced with admin user 

    **shell>** 
    ```
    <copy>mysql -uroot -p -P3307 -h127.0.0.1</copy>
    ```
2.	Create a new table poi

    **mysql>** use world; 
    ```
    <copy>use world;</copy>
    ```
    **mysql>** 
    ```
    <copy>CREATE TABLE if not exists poi (x Int, y INT, z INT);</copy>
    ```
3.	Add to the table a new column for id used for large integer values

    **mysql>** 
    ```
    <copy>alter table poi add id bigint;</copy>
    ```
    **mysql>**  
    ```
    <copy>ALTER TABLE poi ADD PRIMARY KEY (id);</copy>
    ```
4.	Create a copy of your city table

    **mysql>** 
    ```
    <copy>create table city_part as select * from city;</copy>
    ```
5.	How many records does it contain?

    **mysql>**  
    ```
    <copy>SELECT count(*) FROM city_part;</copy>
    ```
6.	How many records city table contain?

    **mysql>**  
    ```
    <copy>SELECT count(*) FROM city;</copy>
    ```
7.	Verify the difference of the two table creation (there is a big one!)

    **mysql>** 
    ```
    <copy>show create table city\G </copy>
    ```
    **mysql>**  
    ```
    <copy>show create table city_part\G</copy>
    ```
## Task 2: 	Create index

1.	Create an index on new table

    **mysql>** 
    ```
    <copy>CREATE INDEX myidindex ON city_part (ID); </copy>
    ```
2.	Check table statistics. What is the Cardinality (=unique records) of primary key?

    **mysql>** 
    ```
    <copy>SELECT * FROM INFORMATION_SCHEMA.STATISTICS WHERE table&#95;name = 'city' and table&#95;schema='world'\G</copy>
    ```
3.	Create a new index

    **mysql>** 
    ```
    <copy>CREATE INDEX myccindex ON city_part (CountryCode);</copy>
    ```
4.	Delete some columns (Population and CountryCode)

    **mysql>** 
    ```
    <copy>ALTER TABLE city_part DROP COLUMN Population;</copy>
    ```
    **mysql>** 
    ```
    <copy>ALTER TABLE city_part DROP COLUMN CountryCode;</copy>
    ```
5.	Optimize the table
    **mysql>** 
    ```
    <copy>OPTIMIZE TABLE city_part;</copy>
    ```
    **warning is expected:** https://dev.mysql.com/doc/refman/8.0/en/optimize-table.html

## Task 3:  Handle statistics

1.	Update table statistics

    **mysql>** 
    ```
    <copy>ANALYZE TABLE city_part;</copy>
    ```
2.	Create partitions:
    a.	Check the files for the city_part table on your disk. We can do it from the mysql client using the built-in function “system”

    **mysql>** 
    ```
    <copy>system ls -l /mysql/data/world </copy>
    ```
    b.	Partition your table into 5 segments based on hash

    **mysql>** 
    ```
    <copy>ALTER TABLE world.city_part PARTITION BY HASH (id) PARTITIONS 5;</copy>
    ```
    c.	Check the file of the city_part table on your disk

    **mysql>** 
    ```
    <copy>system ls -l /mysql/data/world t</copy>
    ```

## Learn More

*(optional - include links to docs, white papers, blogs, etc)*

* [URL text 1](http://docs.oracle.com)
* [URL text 2](http://docs.oracle.com)

## Acknowledgements
* **Author** - Perside Foster, MySQL Engineering
* **Contributors** -  Marco Carlessi, MySQL Engineering
* **Last Updated By/Date** - <Perside Foster, October 2021