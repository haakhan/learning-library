# SECURITY - MYSQL ENTERPRISE FIREWALL

## Introduction
3c) MySQL Enterprise Firewall
Objective: Firewall in action…
Server: serverB

*Describe the lab in one or two sentences, for example:* This lab walks you through the steps to ...

Estimated Lab Time: -- minutes

### Objectives

In this lab, you will:
* Install and connect Firewall
* Use fwtest

### Prerequisites (Optional)

This lab assumes you have:
* An Oracle account
* All previous labs successfully completed

**Server:** serverB

**Notes:**
- References
- https://dev.mysql.com/doc/refman/8.0/en/firewall-installation.html


## Task 1: Install and connect  Firewall
1.	Install MySQL Enterprise Firewall on mysql-advanced using CLI (you can’t install on mysql-gpl, why? 

    **shell>** 
    ```
    <copy>mysql -uadmin -p -P3307 -h127.0.0.1 < /mysql/mysql-latest/share/linux_install_firewall.sql</copy>
    ```
2.	Connect to the instance with administrative account first SSH connection - administrative

    a. **shell>** 
    ```
    <copy>mysql -uroot -p -P3307 -h127.0.0.1</copy>
    ```
    b. **mysql>** 
    ```
    <copy>SHOW GLOBAL VARIABLES LIKE 'mysql_firewall_mode'; </copy>
    ```
    c. **mysql>** 
    ```
    <copy>SHOW GLOBAL STATUS LIKE "firewall%";</copy>
    ```
3.	Create a new user 'fwtest' and assign full privileges to database world

    a. **mysql>** 
    ```
    <copy>CREATE USER 'fwtest'@'%' IDENTIFIED BY 'Welcome1!';</copy>
    ```
    b. **mysql>** 
    ```
    <copy>GRANT ALL PRIVILEGES ON world.* TO 'fwtest'@'%';</copy>
    ```
4.	Now we set firewall in recording mode, to create a white list and verify that allowlist is empty

    a. **mysql>** 
    ```
    <copy>CALL mysql.sp_set_firewall_mode('fwtest@%', 'RECORDING');</copy>
    ```
    b. **mysql>** 
    ```
    <copy>SELECT * FROM mysql.firewall_users;</copy>
    ```
    c. **mysql>** 
    ```
    <copy>SELECT * FROM mysql.firewall_whitelist;</copy>
    ```
5.	Open a second SSH connection (don't close the administrative one) and use it to connect as “fwtest” and submit some commands

    a. **shell>** 
    ```
    <copy>mysql -ufwtest -p -P3307 -h127.0.0.1</copy>
    ```
    b. **mysql>** 
    ```
    <copy>USE world;</copy>
    ```
    c. **mysql>** 
    ```
    <copy>SELECT * FROM city limit 25;</copy>
    ```
    d. **mysql>** 
    ```
    <copy>SELECT Code, Name, Region FROM country WHERE population > 200000;</copy>
    ```
6.	Administrative connection: Return to admin session (first SSH connection terminal) and verify that there are now rules in allowlist (noticed that we interrogate temporary rules from information schema) 

    **mysql>** 
    ```
    <copy>SELECT * FROM information_schema.mysql_firewall_whitelist;</copy>
    ```
7.	Administrative connection: switch Firewall mode from 'recording' to 'protecting' and verify the presence of rules in allowlist

    a. **mysql>** 
    ```
    <copy>CALL mysql.sp_set_firewall_mode('fwtest@%', 'PROTECTING');</copy>
    ```
    b. **mysql>** 
    ```
    <copy>SELECT * FROM mysql.firewall_whitelist;</copy>
    ```
## Task 2: Use fwtest
1.	fwtest connection: run these commands. Which one’s work? Which ones fail and why?

    a. **mysql>** 
    ```
    <copy>USE world;</copy>
    ```
    b. **mysql>** 
    ```
    <copy>SELECT * FROM city limit 25;</copy>
    ```
    c. **mysql>** 
    ```
    <copy>SELECT Code, Name, Region FROM country WHERE population > 200000;</copy>
    ```
    d. **mysql>** 
    ```
    <copy>SELECT * FROM countrylanguage;</copy>
    ```
    e. **mysql>** 
    ```
    <copy>SELECT Code, Name, Region FROM country WHERE population > 500000;</copy>
    ```
    f. **mysql>** 
    ```
    <copy>SELECT Code, Name, Region FROM country WHERE population > 200000 or 1=1;</copy>
    ```
2.	Administrative connection: set firewall in detecting mode in your 

    a. **mysql>** 
    ```
    <copy>CALL mysql.sp_set_firewall_mode('fwtest@%', 'DETECTING');</copy>
    ```
    b. **mysql>** 
    ```
    <copy>SET GLOBAL log_error_verbosity=3;</copy>
    ```
3.	fwtest connection: Repeat a blocked command (it works? Why? ___________________)

    a. **mysql>** 
    ```
    <copy>SELECT Code, Name, Region FROM world.country WHERE population > 200000 or 1=1;</copy>
    ```
    b. **mysql>** 
    ```
    <copy>exit</copy>
    ```
4.	Search the error in the error log

    **shell>** 
    ```
    <copy>grep "MY-011191" /mysql/log/err_log.log</copy>
    ```
5.	Administrative connection: disable firewall for the user Check the Status of Firewall on the command line. Disabling firewall doesn't delete rules.

    a. **mysql>** 
    ```
    <copy>CALL mysql.sp_set_firewall_mode('fwtest@%', 'OFF');</copy>
    ```
    b. **mysql>** 
    ```
    <copy>SELECT MODE FROM INFORMATION_SCHEMA.MYSQL_FIREWALL_USERS WHERE USERHOST = 'fwtest@%';</copy>
    ```
    c. **mysql>** 
    ```
    <copy>SELECT RULE FROM INFORMATION_SCHEMA.MYSQL_FIREWALL_WHITELIST WHERE USERHOST = 'fwtest@%';</copy>
    ```
## Learn More

*(optional - include links to docs, white papers, blogs, etc)*

* [URL text 1](http://docs.oracle.com)
* [URL text 2](http://docs.oracle.com)

## Acknowledgements
* **Author** - Perside Foster, MySQL Engineering
* **Contributors** -  Marco Carlessi, MySQL Engineering
* **Last Updated By/Date** - <Perside Foster, October 2021
