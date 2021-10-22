# SECURITY - MYSQL USER ROLES

## Introduction

3b) MySQL Roles
Objective: Discover and Configure roles
Server: serverB

*Describe the lab in one or two sentences, for example:* This lab walks you through the steps to ...

Estimated Lab Time: -- minutes

### Objectives

*List objectives for this lab using the format below*

In this lab, you will:
* Create user
* Set user role

### Prerequisites (Optional)

This lab assumes you have:
* An Oracle account
* All previous labs successfully completed

**Server:** serverB

## Task 1: Create user
1.	Reconnect as root to create a new user
	
	a. **shell>** 
    ```
    <copy>mysql -u admin -p -h 127.0.0.1 -P 3307</copy>
    ```
	b. **mysql>** 
    ```
    <copy>CREATE USER 'appuser2'@'%' IDENTIFIED BY 'Welcome1!';</copy>
    ```
	c. **mysql>** 

    ```
    <copy>SHOW GRANTS FOR 'appuser2'@'%';</copy>
    ```
2.	Now create a new role and grant it to the new user
	
	a. **mysql>** 
    ```
    <copy>CREATE ROLE 'app_read';</copy>
    ```
	b. **mysql>** 
    ```
    <copy>GRANT SELECT ON world.* TO 'app_read';</copy>
    ```
	c. **mysql>** 
    ```
    <copy>GRANT 'app_read' TO 'appuser2'@'%';</copy>
    ```
	d. **mysql>** SHOW GRANTS FOR 'appuser2'@'%';
    ```
    <copy>SHOW GRANTS FOR 'appuser2'@'%';</copy>
    ```
3.	Reconnect as appuser2 and submit some commands (you receive errors, why?)
	
	a. **shell>** 
    ```
    <copy>mysql -u appuser2 -p -h 127.0.0.1 -P 3307</copy>
    ```
	b. **mysql>** ; 
    ```
    <copy>SHOW DATABASES</copy>
    ```
	c. **mysql>** 
    ```
    <copy>SELECT COUNT(*) FROM world.city;</copy>
    ```
	d. **mysql>** 
    ```
    <copy>SELECT current_role();</copy>
    ```
## Task 2: Set user role
4.	Set the role for the user and repeat above commands

	a. **mysql>** 
    ```
    <copy>SET ROLE ALL;</copy>
    ```
	b. **mysql>** 
    ```
    <copy>SELECT current_role();</copy>
    ```
	c. **mysql>**  
    ```
    <copy>SHOW DATABASES;</copy>
    ```
	d. **mysql>** 
    ```
    <copy>SELECT COUNT(*) FROM world.city;</copy>
    ```
5.	We can also assign a default role to don’t ask to set one after every login (you can use user or administrative session)

	**mysql>** 
    ```
    <copy>ALTER USER 'appuser2'@'%' DEFAULT ROLE 'app_read';</copy>
    ```

## Learn More

*(optional - include links to docs, white papers, blogs, etc)*

* [URL text 1](http://docs.oracle.com)
* [URL text 2](http://docs.oracle.com)

## Acknowledgements
* **Author** - Perside Foster, MySQL Engineering
* **Contributors** -  Marco Carlessi, MySQL Engineering
* **Last Updated By/Date** - <Perside Foster, October 2021
