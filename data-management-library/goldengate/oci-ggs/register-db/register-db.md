# Register databases

## Introduction

This lab walks you through the steps to create database registrations.

Estimated time: 2 minutes

### About Database Registrations
Database Registrations capture source and target credential information. A database registration also enables networking between the OCI GoldenGate service tenancy virtual cloud network (VCN) and your tenancy VCN using a private endpoint.

### Objectives
In this lab, you will register source and target Oracle Autonomous databases for Oracle GoldenGate deployments to use for the duration of this lab.

### Prerequisites
This lab assumes that you completed all preceding labs.

## Task 1: Register the source database

First, follow the steps below to register the source Oracle Autonomous Transaction Processing \(ATP\) Database.

1.  Use the Oracle Cloud Console breadcrumb to navigate back to the GoldenGate page.

    ![Click GoldenGate](images/01-01-breadcrumb.png " ")

2.  Click **Registered Databases**.

    ![Click Registered Databases](images/01-02-ggs-registerdb.png " ")

3.  Click **Register Database**.

    ![Click Register Database](images/01-03-ggs-registerdb.png " ")

4.  In the Register Database panel, for Name and Alias, enter **SourceATP**.

5.  From the Compartment dropdown, select a compartment.

6.  Click **Select Database**.

7.  From the Database Type dropdown, select **Autonomous Database**.

8.  For **Autonomous Database in &lt;compartment-name&gt;**, click **Change Compartment**, select the compartment you created your ATP instance, and then select **SourceATP** from the dropdown. Some fields are autopopulated based on your selection.

9.  Enter the database's password in the Password field, and then click **Register**.

    ![Source Database details](images/01_01_12_regSourceDB.png)

    The database registration becomes Active after a few minutes.

## Task 2: Unlock the GGADMIN user and check support mode for the source database

Oracle Autonomous Databases come with a GGADMIN user that is locked by default. The following steps guide you through how to unlock the GGADMIN user.

1.  From the Oracle Cloud Console **Navigation Menu** (hamburger icon), click **Oracle Database**, and then select **Autonomous Transaction Processing**.

	![](https://raw.githubusercontent.com/oracle/learning-library/master/common/images/console/database-atp.png " ")

2.  From the list of databases, select **SourceATP**.

    ![](images/02-02.png " ")

3.  On the SourceATP Database Details page, click **Tools**, and then click **Open Database Actions**.

    ![](images/02-03-db-tools.png " ")

4.  Sign in to Database Actions using the ADMIN user details from Lab 1: Set Up the Environment. If you're running this lab as a workshop, copy the ADMIN password provided with your lab environment details.

5.  Under **Administration**, click **Database Users**.

    ![](images/02-05.png " ")

6.  From the list of users, locate **GGADMIN**, and then click the ellipsis (three dots) icon and select **Edit**.

    ![GGADMIN user](images/02-06-locked.png)

7.  In the Edit User panel, deselect **Account is Locked**, enter the password you gave the ggadmin user in the database registration steps above, and then click **Apply Changes**.

    ![Edit user](images/02-07-edit.png)

    Note that the user icon changes from a padlock to a checkmark.

8.  From the navigation menu (hamburger icon), click **SQL**.

9.  In the worksheet, enter the following, and then click **Run Statement**:

    ```
    <copy>set pagesize 50
alter session set container=pdbeast;
column object_name format a40
column support_mode format a8 heading 'Support|Mode'
select * from DBA_GOLDENGATE_SUPPORT_MODE where owner = 'SRC_OCIGGLL';
    </copy>
    ```

    The Script Output panel displays six tables whose Support_Mode is **FULL**.

    ![](images/02-09b.png " ")

You can leave the source database SQL window open for use in a later lab.

## Task 3: Register the target database and unlock the GGADMIN user

Now, follow the steps below to register the target Autonomous Data Warehouse \(ADW\) instance.

1.  Use the Oracle Cloud Console navigation menu to navigate back to GoldenGate.

1.  Click **Registered Databases** and then **Register Database**.

    ![](images/03-02.png)

2.  In the Register Database panel, enter **TargetADW** for Name and Alias.

3.  From the **Compartment** dropdown, select a compartment.

4.  Click **Select Database**.

5.  For **Autonomous Database in &lt;compartment-name&gt;**, click **Change Compartment**, select the compartment you created your ADW instance, and then select **TargetADW** from the dropdown. Some fields are autopopulated based on your selection.

6.  Enter the database's password in the Password field, and then click **Register**.

    ![Target Database details](images/02_10-ggs-regDB_target.png)

    The source and target databases appear in the list of Registered Databases. The database registration becomes Active after a few minutes.

7.  Repeat the instructions under Task 2 to unlock the GGADMIN user on the TargetADW database.

You may now **proceed to the next lab**.

## Learn more

* [Managing Database Registrations](https://docs.oracle.com/en/cloud/paas/goldengate-service/using/database-registrations.html)

## Acknowledgements
* **Author** - Jenny Chan, Consulting User Assistance Developer, Database User Assistance
* **Contributors** -  Denis Gray, Database Product Management
* **Last Updated By/Date** - Jenny Chan, October 2021
