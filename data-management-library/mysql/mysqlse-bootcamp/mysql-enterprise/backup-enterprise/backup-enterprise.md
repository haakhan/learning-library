# MYSQL BACKUP - ENTERPRISE BACKUP

## Introduction

6b) MySQL Enterprise Backup
Objective: explore how mysqlbackup works
Server: serverB

*Describe the lab in one or two sentences, for example:* This lab walks you through the steps to ...

Estimated Lab Time: -- minutes

### Objectives

In this lab, you will:
* Install Enterprise Backup
* Use backup

### Prerequisites 

This lab assumes you have:
* An Oracle account
* All previous labs successfully completed

**Server:** serverB

**Notes:**
- We work now with mysql-advanced instance. [ student###-serverB:3307 ]

**References:**
- https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/mysqlbackup.tasks.html
- https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/mysqlbackup.privileges.html

## Task 1: Install Enterprise Backup

1.	MySQL Enterprise Backup is now available inside MySQL Enterprise Distributions like a tool, so you don’t have to install it.

2.	Create directories to store backups

    **shell>** 
    ```
    <copy>sudo mkdir -p /backupdir/full</copy>
    ```
    **shell>** 
    ```
    <copy>sudo mkdir /backupdir/compressed</copy>
    ```
    **shell>** 
    ```
    <copy>sudo chown -R mysqluser:mysqlgrp /backupdir</copy>
    ```
    **shell>** 
    ```
    <copy>sudo chmod 770 -R /backupdir</copy>
    ```
3.	Create a user in mysql-advanced with grants options for backup. To simplify user creations we have a script with minimal grants for this user (see the manual for additional privileges required for specific features like TTS, SBT integration, encrypted). You can also have a look on the privileges opening the file /workshop/support/mysqlbackup_user_grants.sql

    **shell>** 
    ```
    <copy>mysql -uroot -p -h127.0.0.1 -P3307</copy>
    ```
    **mysql>** 
    ```
    <copy>CREATE USER 'mysqlbackup'@'%' IDENTIFIED BY 'Welcome1!';</copy>
    ```
    **mysql>** 
    ```
    <copy>source /workshop/support/mysqlbackup_user_grants.sql;</copy>
    ```
    **mysql>** 
    ```
    <copy>exit</copy>
    ```
4.	Create a full backup (be careful with copy&paste!). 

    **shell>** 
    ```
    <copy>sudo /mysql/mysql-latest/bin/mysqlbackup --port=3307 --host=127.0.0.1 --protocol=tcp --user=mysqlbackup --password --backup-dir=/backupdir/full backup-and-apply-log</copy>
    ```
5.	Create a second backup with compression (be careful with copy&paste!)

    **shell>** 

    ```
    <copy>sudo /mysql/mysql-latest/bin/mysqlbackup --port=3307 --host=127.0.0.1 --protocol=tcp --user=mysqlbackup --password --backup-dir=/backupdir/compressed --compress backup-and-apply-log</copy>
    ```
6.	Because these backups are created with sudo, change the permissions

    **shell>** 
    ```
    <copy>sudo chown -R mysqluser:mysqlgrp /backupdir/full</copy>
    ```
    **shell>** 
    <copy>sudo chown -R mysqluser:mysqlgrp /backupdir/compressed
    ```</copy>
    ```
7.	Have a look of the content of the backup folders

    **shell>** 
    ```
    <copy>cd /backupdir/full</copy>
    ```
    **shell>** 
    ```
    <copy>ls -l</copy>
    ```
    **shell>** 
    ```
    <copy>cd /backupdir/compressed/copy>
    ```
    **shell>** 
    ```
    <copy>ls -l</copy>
    ```
8.	Check the size of the two backups, the one uncompressed and the one compressed

    **shell>** 
    ```
    <copy>cd /backupdir</copy>
    ```
    **shell>** d
    ```
    <copy>u -sh *</copy>
    ```
## Task 2: Use backup
1.	Restore
    a.	Stop the server

    **shell>** 
    ```
    <copy>sudo systemctl stop mysqld-advanced	</copy>
    ```
    b.	(destroy time!) empty datadir and binary log dir

    **shell>** 
    ```
    <copy>sudo rm -rf /mysql/binlog/* /mysql/data/*</copy>
    ```
    c.	Restore the backup (be careful with copy&paste!)

    **shell>** 
    ```
    <copy>sudo /mysql/mysql-latest/bin/mysqlbackup --defaults-file=/mysql/etc/my.cnf --backup-dir=/backupdir/full/ --datadir=/mysql/data --log-bin=/mysql/binlog/binlog copy-back</copy>
    ```
    d.	Set ownership

    **shell>** 
    ```
    <copy>sudo chown -R mysqluser:mysqlgrp /mysql/data /mysql/binlog</copy>
    ```
    **shell>** 
    ```
    <copy>sudo chmod -R 750 /mysql/data /mysql/binlog</copy>
    ```

    e.	Start the server

    **shell>** 
    ```
    <copy>sudo systemctl start mysqld-advanced</copy>
    ```
    a.	verify that content is still there

    **shell>** 
    ```
    <copy>mysql -uroot -p -h127.0.0.1 -P3307</copy>
    ```
    **mysql>** 
    ```
    <copy>SHOW DATABASES;</copy>
    ```

## Learn More

*(optional - include links to docs, white papers, blogs, etc)*

* [URL text 1](http://docs.oracle.com)
* [URL text 2](http://docs.oracle.com)

## Acknowledgements
* **Author** - Perside Foster, MySQL Engineering
* **Contributors** -  Marco Carlessi, MySQL Engineering
* **Last Updated By/Date** - <Perside Foster, October 2021
