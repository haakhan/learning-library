# SECURITY - MYSQL USERS

## Introduction

3a) Users management
Objective: explore user creation and privileges
Server: 
•	serverA as client
•	serverB as server



*Describe the lab in one or two sentences, for example:* This lab walks you through the steps to ...

Estimated Time: -- minutes


### Objectives

In this lab, you will  do the followings:
- Connect to mysql-advanced om serverA
- Connect to a second mysql-advanced om serverA
- Use appuser connection
- Restore user privileges

### Prerequisites

This lab assumes you have:
* An Oracle account
* All previous labs successfully completed

**Server:** 
- serverA as client
- serverB as server

**Notes:**
- use two shell, one per server
- Open a notepad file and  your linux Private IP on student###-serverA and serverB 

- serverA  PRIVATE ip: (client_ip)
- serverB  PRIVATE ip: (server_ip)

## Task 1: Connect to mysql-advanced om serverA

1. Connect to your mysql-advanced with administrative user

   **shell>** 

    ```
    <copy>mysql -uroot -p -h 127.0.0.1 -P 3307</copy>
    ```

2. Create a new user and restrict the user to your “serverA” IP

	a. **mysql>** 

    ```
    <copy>CREATE USER 'appuser'@<client_ip> IDENTIFIED BY 'Welcome1!';</copy>
    ```

	b. **mysql>** 

    ```
    <copy>GRANT ALL PRIVILEGES ON world.* TO 'appuser'@<client_ip>;</copy>
    ```

	c. **mysql>** 

    ```
    <copy>SHOW GRANTS FOR 'appuser'@<client_ip>;</copy>
    ```
## Task 2: Connect to a second mysql-advanced om serverA
1. Open a new SSH connection on serverA and from there connect to mysql-advanced with appuser

	a. Install mysql client
	 
    **shell>** 

    ```
    <copy>sudo yum install /workshop/linux/client/*.rpm</copy>
    ```

	b. connect to mysql-advanced with appuser
   **shell>** 

    ```
    <copy>mysql -u appuser -p -h <server_ip> -P 3307</copy>
    ```
	c. Run a select on the tables e.g.

    **mysql>** 

    ```
    <copy>USE world;</copy>
    ```

    **mysql>** 

    ```
    <copy>SELECT * FROM city;</copy>
    ```

2. Switch to the administrative connection revoke privilege on city to appuser

    **mysql>** 

    ```
    <copy>REVOKE SELECT ON world.* FROM 'appuser'@<client_ip>;</copy>
    ```

    **mysql>** 

    ```
    <copy>SHOW GRANTS FOR 'appuser'@<client_ip>;</copy>
    ```
3. Repeat the select on appuser connection for the user. There is a difference?

    **mysql>** 

    ```
    <copy>SELECT * FROM city;</copy>
    ```

## Task 3: Use appuser connection
1.	Close and reopen the appuser connection for the user, then repeat above commands. There is a difference? 

    **mysql>** 

    ```
    <copy>exit</copy>
    ```

	**shell>** 

    ```
    <copy>mysql -u appuser -p -h <server_ip> -P 3307</copy>
    ```
	**mysql>** 

    ```
    <copy>USE world;</copy>
    ```
    **mysql>** 
    ```
    <copy>SELECT * FROM city;</copy>
    ```
2.	Switch to the administrative connection revoke ‘USAGE’ privilege using and administrative connection and verify (tip: this privilege can’t be revoked…)

	**mysql>**
	```
	<copy>REVOKE USAGE ON *.* FROM 'appuser'@<client_ip>;</copy>
	```
	**mysql>**
	```
	<copy>SHOW GRANTS FOR 'appuser'@<client_ip>;</copy>
	```

3.	Using the administrative connection revoke all privileges using and administrative connection and verify

	**mysql>**
	```
    <copy>REVOKE ALL PRIVILEGES ON *.* FROM 'appuser'@<client_ip>;</copy>
    ```
	**mysql>**
	```
    <copy>SHOW GRANTS FOR 'appuser'@<client_ip>;</copy>
    ```   
4.	Close and reopen appuser session, do you see schemas?

## Task 4: Restore user privileges
1.	Using the administrative connection restore user privileges to reuse it in next labs

	**mysql>**
    ```
    <copy>GRANT ALL PRIVILEGES ON world.* TO 'appuser'@<client_ip>;</copy>
    ```
2.	Using the administrative connection, what are your password settings?

	**mysql>** 
    ```
    <copy>SHOW VARIABLES LIKE 'validate_password%';</copy>
    ```
3.	Try to set unsecure passwords for appuser

	**mysql>** 
    ```
    <copy>alter user 'appuser'@<client_ip> identified by 'appuser';</copy>
    ```
	
	**mysql>** 
    ```
    <copy>alter user 'appuser'@<client_ip> identified by 'Welcome';</copy>
    ```

	**mysql>** 
    ```
    <copy>alter user 'appuser'@<client_ip>identified by 'We1!';</copy>
    ```
4.	Expire the password for appuser

	**mysql>** 
    ```
    <copy>alter user 'appuser'@<client_ip> PASSWORD EXPIRE;</copy>
    ```
5.	Close and reopen connection to mysql-advanced and try to submit a command. What changed?

	**shell>** 
    ```
    <copy>mysql –u appuser -p -h <server_ip> -P 3307</copy>
    ```

	**mysql>** 
    ```
    <copy>SHOW DATABASES;</copy>
    ```

	**mysql>** 
    ```
    <copy>alter user 'appuser'@<client_ip> identified by 'Welcome1!'</copy>
    ```
## Learn More

*(optional - include links to docs, white papers, blogs, etc)*

* [URL text 1](http://docs.oracle.com)
* [URL text 2](http://docs.oracle.com)

## Acknowledgements
* **Author** - Perside Foster, MySQL Engineering
* **Contributors** -  Marco Carlessi, MySQL Engineering
* **Last Updated By/Date** - <Perside Foster, October 2021
