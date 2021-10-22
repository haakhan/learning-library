# DATABASE DESIGN - MYSQL DOCUMENT STORE

## Introduction

4c) MySQL Document Store
Objective: Understanding the functioning of MySQL Document Store and practicing some CRUD operations.

Server: serverB

*Describe the lab in one or two sentences, for example:* This lab walks you through the steps to ...

Estimated Lab Time: -- minutes

### Objectives

*List objectives for this lab using the format below*

In this lab, you will:
* *Use Xprotocol and use collection
* Work with 1ndexes

### Prerequisites 

This lab assumes you have:
* An Oracle account
* All previous labs successfully completed

**Server:** serverB

**Notes:**
- Please note that we use the port for Xdev (33070) instead of usual classic protocol port (3307)


## Task 1: Use Xprotocol and use collection

1. Please connect to MySQL Database via X Protocol

	**shell>** 

    ```
    <copy>mysqlsh -uroot -h127.0.0.1 -P33070 -p</copy>
    ```
2. Create and use a test schema. (We use javascript mode, but python is available also)
	
	a. **MySQL … JS >** 

    ```
    <copy>session.createSchema('test')</copy>
    ```
	b. **MySQL … JS >** 

    ```
    <copy>\use test</copy>
    ```
3. Now create and populate a small collection
	
	c. **MySQL … JS >** 

    ```
    <copy>db.createCollection('posts');</copy>
    ```
	d. **MySQL … JS >** 

    ```
    <copy>db.posts.add({"title":"MySQL 8.0 rocks", "text":"My first post!", "code": "42"})</copy>
    ```
	e. **MySQL … JS >** 

    ```
    <copy>db.posts.add({"title":"Polyglot database", "text":"Developing both SQL and NoSQL applications"})</copy>
    ```
4. Checking the built-in JSON validation
	
	**MySQL … JS >** 

    ```
    <copy>db.posts.add("This is not a valid JSON document")</copy>
    ```
5. Inspect the posts collection you have just created 
	
	**MySQL … JS >** 

    ```
    <copy>db.posts.find()</copy>
    ```
6. What can you notice? Did the system add something to content by itself?
	
	**MySQL … JS >** 

    ```
    <copy>db.posts.find().limit(1)</copy>
    ```
7.  Modify existing elements of the collection
	
	a. **MySQL … JS >** db.posts.modify("title = 'MySQL 8.0 rocks'").set("title", " MySQL 8.0 rocks!!!")

    ```
    <copy>exit</copy>
    ```
	b. **MySQL … JS >** db.posts.find()

    ```
    <copy>exit</copy>
    ```
## Task 2: Work with 1ndexes

1. Check that that a collection is just a table with 2 columns: Index and JSON Document
	
	a. **MySQL … JS >** 

    ```
    <copy>session.sql("desc posts")</copy>
    ```
	b. **MySQL … JS >** 

    ```
    <copy>session.sql("show create table posts")</copy>
    ```
	c. **MySQL … JS >** 

    ```
    <copy>session.sql("select * from posts")</copy>
    ```
2. Therefore, it is possible to add indexes on specific JSON elements of the collection

	a. **MySQL … JS >** 

    ```
    <copy>db.posts.createIndex('myIndex', {fields: [{field: "$.title", type: "TEXT(20)"}]} )</copy>
    ```
	b. **MySQL … JS >** 

    ```
    <copy>session.sql("show create table posts")</copy>
    ```

## Learn More

*(optional - include links to docs, white papers, blogs, etc)*

* [URL text 1](http://docs.oracle.com)
* [URL text 2](http://docs.oracle.com)

## Acknowledgements
* **Author** - Perside Foster, MySQL Engineering
* **Contributors** -  Marco Carlessi, MySQL Engineering
* **Last Updated By/Date** - <Perside Foster, October 2021