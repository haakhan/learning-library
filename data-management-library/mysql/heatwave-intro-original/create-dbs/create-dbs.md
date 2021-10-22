# CREATE MYSQL DATABASE SYSTEM
![INTRO](./images/00_mds_heatwave_2.png " ") 


## Introduction

In this lab, you will create and configure a MySQL DB System. The creation process will use a provided object storage link to create the airportdb schema and load data into the DB system.    

Estimated Lab Time: 15 minutes

### Objectives

In this lab, you will be guided through the following tasks:


- Create Virtual Cloud Network 
- Create MySQL Database for HeatWave (DB System) instance with sample data (airportdb)

### Prerequisites

- An Oracle Trial or Paid Cloud Account
- Some Experience with MySQL Shell


## Task 1: Create Virtual Cloud Network 

*Note: Green Button users - Your Virtual Cloud Network already exist. Go to Task 2*

1. Navigation Menu   
        Networking  
            Virtual Cloud Networks
    ![VCN](./images/03vcn01.png " ")

2. 'click' **Start VCN Wizard**
    ![VCN](./images/03vcn02.png " ")

3. Select 'Create VCN with Internet Connectivity'

    'click' 'Start VCN Wizard' 
    ![VCN](./images/03vcn03.png " ")

4. Create a VCN with Internet Connectivity 

    On Basic Information, complete the following fields:

 VCN Name: 
     ```
    <copy>MDS-VCN</copy>
    ```
 Compartment: Select  **(root)**

 Your screen should look similar to the following
    ![VCN](./images/03vcn04.png " ")

5. Click 'Next' at the bottom of the screen 

6. Review Oracle Virtual Cloud Network (VCN), Subnets, and Gateways
         
    Click 'Create' to create the VCN
    ![VCN](./images/03vcn04-1.png " ")

7. The Virtual Cloud Network creation is completing 
    ![VCN](./images/03vcn05.png " ")
    
8. Click 'View Virtual Cloud Network' to display the created VCN
    ![VCN](./images/03vcn06.png " ")

9. On MDS-VCN page under 'Subnets in (root) Compartment', 'click'  '**Private Subnet-MDS-VCN**' 
     ![VCN](./images/03vcn07.png " ")

10.	On Private Subnet-MDS-VCN page under 'Security Lists',  'click'  '**Security List for Private Subnet-MDS-VCN**'
    ![VCN](./images/03vcn08.png " ")

11.	On Security List for Private Subnet-MDS-VCN page under 'Ingress Rules', 'click' '**Add Ingress Rules**' 
    ![VCN](./images/03vcn09.png " ")

12.	On Add Ingress Rules page under Ingress Rule 1
 
 Add an Ingress Rule with Source CIDR 
    ```
    <copy>0.0.0.0/0</copy>
    ```
 Destination Port Range 
     ```
    <copy>3306,33060</copy>
     ```
Description 
     ```
    <copy>MySQL Port Access</copy>
     ```
 Click 'Add Ingress Rule'
    ![VCN](./images/03vcn10.png " ")

13.	On Security List for Private Subnet-MDS-VCN page, the new Ingress Rules will be shown under the Ingress Rules List
    ![VCN](./images/03vcn11.png " ")

## Task 2: Create MySQL Database for HeatWave (DB System) instance with sample data (airportdb)

1. Go to Navigation Menu 
         Databases 
         MySQL
         DB Systems
    ![MDS](./images/04mysql01.png " ")

2. Click 'Create MySQL DB System'
    ![MDS](./images/04mysql02.png " ")

3. Create MySQL DB System dialog complete the fields in each section

    - Provide basic information for the DB System
    - Setup your required DB System
    - Create Administrator credentials
    - Configure Networking
    - Configure placement
    - Configure hardware
    - Exclude Backups
    - Advanced Options - Data Import
   
4. Provide basic information for the DB System:

 Select Compartment **(root)**

 Enter Name
     ```
    <copy>MDS-HW</copy>
    ```
 Enter Description 
    ```
    <copy>MySQL Database Service HeatWave instance</copy>
    ```
 
 Select **HeatWave** to specify a HeatWave DB System
    ![MDS](./images/04mysql03-3.png " ")

5. Create Administrator Credentials

 Enter Username
    ```
    <copy>admin</copy>
    ```
    
 Enter Password
    ```
    <copy>Welcome#12345</copy>
    ```   
 Confirm Password
    ```
    <copy>Welcome#12345</copy>
    ```
    ![MDS](./images/04mysql04.png " ")

6. On Configure networking, keep the default values

    Virtual Cloud Network: **MDS-VCN**
    
    Subnet: **Private Subnet-MDS-VCN (Regional)**

    ![MDS](./images/04mysql05.png " ")

7. On Configure placement under 'Availability Domain'
   
    Select AD-3

    Do not check 'Choose a Fault Domain' for this DB System. 

    ![MDS](./images/04mysql06-3.png " ")

8. On Configure hardware, keep default shape as **MySQL.HeatWave.VM.Standard.E3**

    Data Storage Size (GB) Set value to:  **100**
    
    ```
    <copy>100</copy>
    ``` 
    ![MDS](./images/04mysql07-3-100.png" ")

9. On Configure Backups, disable 'Enable Automatic Backup'

    ![MDS](./images/04mysql08.png " ")

10. 'click' on Show Advanced Options 

11. Select Data Import tab. 
12. To enter the PAR Source URL, use one of the folloing links depending on your Tenancy Region

    **US(Ashburn) Region**:
        ![MDS](./images/region-ashburn.png =50%x*)
    
    Copy and paste the following *Asburn link*  to PAR Source URL: 
  
    ```
    <copy> https://objectstorage.us-ashburn-1.oraclecloud.com/p/RpoC9Zza6bcxIAWkNXFVKD0dsmRQJRMvNthgzbr3TUnO9pTYpEhoSFP7_6RNZ1lv/n/mysqlpm/b/airportdb-bucket/o/airportdb/@.manifest.json  </copy>
    ```   
        
    **UK South(London) Region**
        ![MDS](./images/region-london.png =50%x*)
    
    Copy and paste the following *London link*  to PAR Source URL: 
  
    ```
    <copy> https://objectstorage.uk-london-1.oraclecloud.com/p/wF_0GlwqPaz-0YLaoXhQ2R_L2ev45F3yuhzA9fID4KS-wB4_GsDuYRV_svAS_d7d/n/idazzjlcjqzj/b/airportdb-bucket/o/airportdb/@.manifest.json </copy>
    ```   
  
    Your PAR Source URL entry should look like this:
    ![MDS](./images/04mysql08-2.png " ")

13. Review **Create MySQL DB System**  Screen 

    ![MDS](./images/04mysql09-3.png " ")

    
    Click the '**Create**' button

14. The New MySQL DB System will be ready to use after a few minutes 

    The state will be shown as 'Creating' during the creation
    ![MDS](./images/04mysql10-3.png" ")

15. The state 'Active' indicates that the DB System is ready for use 

    On MDS-HW Page, check the MySQL Endpoint (Private IP Address) 

    ![MDS](./images/04mysql11-3.png" ")

You may now [proceed to the next lab](#next).

## Acknowledgements
* **Author** - Perside Foster, MySQL Solution Engineering 
* **Contributors** - Mandy Pang, MySQL Principal Product Manager,  Priscila Galvao, MySQL Solution Engineering, Nick Mader, MySQL Global Channel Enablement & Strategy Manager, Frédéric Descamps, MySQL Community Manager
* **Last Updated By/Date** - Perside Foster, MySQL Solution Engineering, September 2021
