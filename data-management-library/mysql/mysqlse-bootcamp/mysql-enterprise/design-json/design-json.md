# DATABASE DESIGN - MYSQL JSON 

## Introduction

4b) MySQL JSON datatype 
Objective: practice with JSON

Server: serverB

*Describe the lab in one or two sentences, for example:* This lab walks you through the steps to ...

Estimated Lab Time: -- minutes

### Objectives


In this lab, you will:
* Create Database and Table
* Load Table
* Retrieve Data
* Use Index

### Prerequisites 

This lab assumes you have:
* An Oracle account
* All previous labs successfully completed

**Server:** serverB

## Task 1: Create Database and Table

1. Create a database for JSON tests

    a. **mysql>**

    ```
    <copy>CREATE DATABASE json_test;</copy>
    ```
    b. **mysql>** 

    ```
    <copy>USE json_test;</copy>
    ```
2.	Create a JSON table

    a. **mysql>**  

    ```
    <copy>CREATE TABLE jtest (id bigint NOT NULL AUTO_INCREMENT, doc JSON, PRIMARY KEY (id));</copy>
    ```
    b. **mysql>** 

    ```
    <copy>SELECT * FROM jtest;</copy>
    ```
## Task 2: Load Table

1.	add data to this table

    a. **mysql>** 

    ```
    <copy>INSERT INTO jtest(doc) VALUE('{"A": "hello", "b": "test", "c": {"hello": 1}}');</copy>
    ```
    b. **mysql>** 

    ```
    <copy>INSERT INTO jtest(doc) VALUE('{"b": "hello"}'),('{"c": "help"}');</copy>
    ```
2.	Display table dada  

    **mysql>**

    ```
    <copy>SELECT * FROM jtest;</copy>
    ```
## Task 3: Retrieve Data 

1.	Retrieve json documents with shortcut “->” 

    a. **mysql>** 

    ```
    <copy>SELECT json_extract (doc, "$.b") FROM jtest;</copy>
    ```
    b. **mysql>** 

    ```
    <copy>SELECT doc->"$.b" FROM jtest;</copy>
    ```
2.	Retrieve json documents with shortcut “$.” 

    a. **mysql>** 

    ```
    <copy>SELECT json_extract (doc, "$.c") FROM jtest;</copy>
    ```
    b. **mysql>** 

    ```
    <copy>SELECT doc->"$.b" from jtest;</copy>
    ```
    c. **mysql>** 

    ```
    <copy>SELECT doc->>"$.b" from jtest;</copy>
    ```
## Task 4: Use Index
5.	Create Index on the virtual column

    a. **mysql>**  

    ```
    <copy>alter table jtest add column gencol CHAR(7) AS (doc->"$.b");</copy>
    ```
    b. **mysql>** 

    ```
    <copy>CREATE INDEX myvirtindex ON jtest(gencol);</copy>
    ```
    c. **mysql>** 

    ```
    <copy>SELECT * FROM jtest;</copy>
    ```

## Learn More

*(optional - include links to docs, white papers, blogs, etc)*

* [URL text 1](http://docs.oracle.com)
* [URL text 2](http://docs.oracle.com)

## Acknowledgements
* **Author** - Perside Foster, MySQL Engineering
* **Contributors** -  Marco Carlessi, MySQL Engineering
* **Last Updated By/Date** - <Perside Foster, October 2021