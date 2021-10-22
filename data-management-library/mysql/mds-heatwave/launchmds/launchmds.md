# Getting Started with MySQL Database Service and HeatWave
![INTRO](./images/00_mds_heatwave_2.png " ") 


## Introduction

In this hands-on workshop, you will be introduced to MySQL Database Service (MDS), a powerful union between MySQL Enterprise Edition and Oracle Cloud Infrastructure. You will learn how to create and use MySQL Database Service with HeatWave in a secure Oracle Cloud Infrastructure environment.

Estimated Lab Time: 90 minutes


### Objectives

In this lab, you will be guided through the following tasks:

- Create and configure a Virtual Cloud Network (VCN) 
- Create the MySQL Database Service with HeatWave
- Create Client Linux Virtual Machine and install MySQL Shell
- Connect and use MySQL HeatWave
    * Create Airportdb Database and Import Data into MySQL
    * Add HeatWave Cluster to MySQL
    * Load Airportdb Data into HeatWave
    * Run Queries in HeatWave
- Connect to MySQL Heatwave using Workbench


### Prerequisites

- An Oracle Trial or Paid Cloud Account
- Some Experience with MySQL Shell

## **TASK 1:** Create Virtual Cloud Network

1. Navigation Menu > Networking > Virtual Cloud Networks
    ![VCN](./images/03vcn01.png " ")

2. Click 'Start VCN Wizard'
    ![VCN](./images/03vcn02.png " ")

3. Select 'Create VCN with Internet Connectivity'

    Click on 'Start VCN Wizard' 
    ![VCN](./images/03vcn03.png " ")

4. Create a VCN with Internet Connectivity 

    On Basic Information, complete the following fields:

 VCN Name: 
     ````
    <copy>MDS-VCN</copy>
    ````
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

9. On MDS-VCN page under 'Subnets in (root) Compartment', click on '**Private Subnet-MDS-VCN**' 
     ![VCN](./images/03vcn07.png " ")

10.	On Private Subnet-MDS-VCN page under 'Security Lists',  click on '**Security List for Private Subnet-MDS-VCN**'
    ![VCN](./images/03vcn08.png " ")

11.	On Security List for Private Subnet-MDS-VCN page under 'Ingress Rules', click on '**Add Ingress Rules**' 
    ![VCN](./images/03vcn09.png " ")

12.	On Add Ingress Rules page under Ingress Rule 1
 
 Add an Ingress Rule with Source CIDR 
    ````
    <copy>0.0.0.0/0</copy>
    ````
 Destination Port Range 
     ````
    <copy>3306,33060</copy>
     ````
Description 
     ````
    <copy>MySQL Port Access</copy>
     ````
 Click 'Add Ingress Rule'
    ![VCN](./images/03vcn10.png " ")

14.	On Security List for Private Subnet-MDS_VCN page, the new Ingress Rules will be shown under the Ingress Rules List
    ![VCN](./images/03vcn11.png " ")

## **TASK 2:** Create a MySQL DB System - HeatWave.

1. Navigation Menu > Databases > MySQL > DB Systems
    ![MDS](./images/04mysql01.png " ")

2. Click 'Create MySQL DB System'
    ![MDS](./images/04mysql02.png" ")

3. Create MySQL DB System dialog complete the fields in each section

    - Provide basic information for the DB System
    - Setup your required DB System
    - Create Administrator credentials
    - Configure Networking
    - Configure placement
    - Configure hardware
    - Exlude Backups
   

4. Provide basic information for the DB System:

 Select Compartment **(root)**

 Enter Name
     ````
    <copy>MDS-HW</copy>
    ````
 Enter Description 
    ````
    <copy>MySQL Database Service HeatWave instance</copy>
    ````
 
 Select **HeatWave** to specify a HeatWave DB System
    ![MDS](./images/04mysql03-3.png " ")

6. Create Administrator Credentials

 Enter Username
    ````
    <copy>admin</copy>
    ````
 Enter Password
    ````
    <copy>Welcome#12345</copy>
    ````   
 Confirm Password
    ````
    <copy>Welcome#12345</copy>
    ````
    ![MDS](./images/04mysql04.png " ")

7. On Configure networking, keep the default values

    Virtual Cloud Network: **MDS-VCN**
    
    Subnet: **Private Subnet-MDS-VCN (Regional)**

    ![MDS](./images/04mysql05.png " ")

8. On Configure placement under 'Availability Domain'
   
    Select AD-3

    Do not check 'Choose a Fault Domain' for this DB System. 

    ![MDS](./images/04mysql06-3.png" ")

9. On Configure hardware, keep default shape as **MySQL.HeatWave.VM.Standard.E3**

    Data Storage Size (GB) Keep default value:  **1024**
    ![MDS](./images/04mysql07-3.png" ")

19. On Configure Backups, disable 'Enable Automatic Backup'

20. Click on 'Show Advanced Options' 

    Select 'Networking' tab

    Enter Hostname 
       ````
    <copy>mdshw</copy>
    ````
    ![MDS](./images/04mysql08-3.png" ")
    
    Click the '**Create**'
    ![MDS](./images/04mysql09-3.png" ")

11. The New MySQL DB System will be ready to use after a few minutes 

    The state will be shown as 'Creating' during the creation
    ![MDS](./images/04mysql10-3.png" ")

12. The state 'Active' indicates that the DB System is ready to use 

    On MDS-HW Page, check the MySQL Endpoint (Private IP Address) 

    ![MDS](./images/04mysql11-3.png" ")


## **TASK 3:** Create Client Virtual Machine

1. You will need a client machine to connect to your brand new MySQL database. To launch a Linux Compute instance, go to Navigation Menu > Compute > Instances
    ![COMPUTE](./images/05compute01.png " ")

2. On Instances in **(root)** Compartment, click on 'Create Instance'
    ![COMPUTE](./images/05compute02_00.png " ")

3. On Create Compute Instance 

 Enter Name
    ````
    <copy>MDS-Client</copy>
    ````   
4. Make sure **(root)** compartment is selected 

5. On Placement, keep the selected Availability Domain

6. On Image and Shape, keep the selected Image, Oracle Linux 7.9 

    And, keep the selected Instance Shape, VM.Standard.E2.1.Micro

      ![COMPUTE](./images/05compute03.png " ")  

7. On Networking, make sure '**MDS-VCN**' is selected

    'Assign a public IP address' should be set to Yes 
   
  ![COMPUTE](./images/05compute04.png " ")

8. If you have not already created your SSH key, perform 'Lab 1: Create Local SSH Key'.  When you are done return to the next line (TASK 5: #9) .

9. On Add SSH keys, upload your own public key. 
  
    ![COMPUTE](./images/05compute05.png " ")

10. Click '**Create**' to finish creating your Compute Instance. 

    ![COMPUTE](./images/05compute06.png " ")

11. The New Virtual Machine will be ready to use after a few minutes. The state will be shown as 'Provisioning' during the creation
    ![COMPUTE](./images/05compute07.png " ")

12.	The state 'Runing' indicates that the Virtual Machine is ready to use. 

    On the **MDS_Client** Instance page under 'Instance Access', **Copy and save the Public IP Address** 
    ![COMPUTE](./images/05compute08.png " ")


## **TASK 4:** Connect to MySQL Database - HeatWave

HeatWave is an add-on to MySQL Database Service. It provides a highly performant and scalable in-memory analytic processing engine optimized for Oracle Cloud Infrastructure. Customers can run HeatWave on data stored in the MySQL database without requiring ETL and without any change to the application. Applications simply access HeatWave via standard MySQL protocols, and the typical administration actions are automated, integrated and accessible via the OCI Web Console, REST API, CLI, or DevOps tools. HeatWave queries achieve orders of magnitude acceleration over the MySQL database.

1. Linux ad Mac users  use Terminal 

   Windows 10 users use Powershell


2.  From a terminal or powershell window on your local system. Connect to the Compute Instance with the SSH command. 

    Indicate the location of the private key you created earlier with **MDS-Client**. 
    
    Enter the username **opc** and the Public **IP Address**.

    Note: The **MDS-Client**  shows the  Public IP Address as mentioned on TASK 5: #11
    
    (Example: **ssh -i ~/.ssh/id_rsa opc@132.145.170...**) 


    ````
    <copy>ssh -i ~/.ssh/id_rsa opc@<your_compute_instance_ip></copy>
    ````


    ![Connect](./images/06connect01.png " ")

    **Install MySQL Shell on the Compute Instance**

3. You will need a MySQL client tool to connect to your new MySQL DB System from your client machine.

    Install MySQL Shell with the following command (enter y for each question)

    **[opc@…]$**

     ````
    <copy>sudo yum install –y mysql-shell</copy>
    ````
    ![Connect](./images/06connect02.png " ")

   **Connect to MySQL Database Service**

4. From your Compute instance, connect to MDS-HW MySQL using the MySQL Shell client tool. 
   
   The endpoint (IP Address) can be found in the MDS-HW MySQL DB System Details page, under the "Endpoint" "Private IP Address". 

    ![Connect](./images/06connect03.png " ")

5.  Use the following command to connect to MySQL using the MySQL Shell client tool. Be sure to add the MDS-HW private IP address at the end of the cammand. Also enter the admin user password

    (Example  **mysqlsh -uadmin -p -h10.0.1..**)

 **[opc@...]$**

    ````
    <copy>mysqlsh -uadmin -p -h 10.0.1....</copy>
    ````
    ![Connect](./images/06connect04.png " ")

6. On MySQL Shell, switch to SQL mode  to try out some SQL commands 

 Enter the following command at the prompt:
     ````
    <copy>\SQL</copy>
    ````
 To display a list of databases, Enter the following command at the prompt:
      ````
    <copy>SHOW DATABASES;</copy>
    ````  
     
 To display the database version, current_date, and user enter the following command at the prompt:
      ````
    <copy>SELECT VERSION(), CURRENT_DATE, USER();</copy>
    ````  
 To display MysQL user and host from user table enter the following command at the prompt:
       ````
    <copy>SELECT USER, HOST FROM mysql.user;</copy>
      ````
 Type the following command to exit MySQL:
      ````
    <copy>\q</copy>
    ````   

  **Final Sceen Shot**
    ![Connect](./images/06connect05.png " ")

## **TASK 5:**  Create airportdb schema and load data using MySQL Shell

**Be sure to complete TASK 8 before doing TASK 9**

1. If you are not already connected to MDS-Client then do so now

    ````
    <copy>ssh -i ~/.ssh/id_rsa opc@<your_compute_instance_ip></copy>
    ````
2. Download the airportdb sample database and unpack it. (6 minutes)

    ````
    <copy>wget https://downloads.mysql.com/docs/airport-db.zip</copy>
    ````

    ````
    <copy>unzip airport-db.zip</copy>
    ````
3. List the  airport-db directory to view the unxipped data files

    ````
    <copy>ls /home/opc/airport-db</copy>
    ````
    ![Connect](./images/09import01.png " ")

4. Start MySQL Shell and connect to the MDS-HW

    ````
    <copy>mysqlsh -uadmin -p -h 10.0.1....</copy>
    ````
5. Load the airportdb database into into MDS-HW using the  MySQL Shell Dump Loading Utility (6 minutes)   

    ````
    <copy>util.loadDump("airport-db", {threads: 16, deferTableIndexes: "all", ignoreVersion: true})</copy>
    ````
6. Display the count of all records per table in airportdb 

    ````
    <copy>\sql</copy>
    ````

    ````
    <copy>SELECT table_name, table_rows FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'airportdb';</copy>
    ````
    ![Connect](./images/09import02.png " ")

7.	Exit MySQL Shell

    ````
    <copy>\q</copy>
    ````
## **TASK 6:**  Add a HeatWave Cluster to MDS-HW MySQL Database System

1. You will create a HeatWave cluster comprise of a MySQL DB System node and two or more HeatWave nodes. The MySQL DB System node includes a plugin that is responsible for cluster management, loading data into the HeatWave cluster, query scheduling, and returning query result.

    ![Connect](./images/10addheat00.png " ")

2. Open the navigation menu  Databases > MySQL > DB Systems
3. Choose the root Compartment. A list of DB Systems is displayed. 
    ![Connect](./images/10addheat01.png " ")
4. In the list of DB Systems, click on the **MDS-HW** Ssystem. click the “More Action” -> “Add HeatWave Cluster”.
    ![Connect](./images/10addheat02.png " ")
6. On the “Add HeatWave Cluster” dialog, select “MySQL.HeatWave.VM.Standard.E3” shape

6. Click “Estimate Node Count” button
    ![Connect](./images/10addheat03.png " ")
7. On the “Estimate Node Count” page, click “Generate Estimate”. This will trigger the auto
provisioning advisor to sample the data stored in InnoDB and based on machine learning
algorithm, it will predict the number of nodes needed.
    ![Connect](./images/10addheat04.png " ")

8. Once the estimations are calculated, it shows list of database schemas in MySQL node. If
you expand the schema and select different tables, you will see the estimated memory
required in the Summary box, There is s Load Command (analytics_load) generated in the text box window, which will change based on the selection of databases/tables

9. Select the airportdb schema and click “Apply Node Count Estimate” to apply the node count
    ![Connect](./images/10addheat05.png " ")

10. Click “Add HeatWave Cluster” to create the HeatWave cluster
    ![Connect](./images/10addheat06.png " ")
11. HeatWave creation will take about 10 minutes. From the DB display page scroll down to the Resources section. Click on the **HeatWave** link. Your completed HeatWave Cluster Information section will look like this:
    ![Connect](./images/10addheat07.png " ")

## **TASK 7:**  Load airportdb Data into HeatWave Cluster
1. If not already connected with SSH, on Command Line, connect to the Compute instance using SSH

    (Example: **ssh -i ~/.ssh/id_rsa opc@&132.145.170..**)

2. On command Line, connect to MySQL using the MySQL Shell client tool

    (Example  **mysqlsh -uadmin -p -h10.0.1..**)

    ````
    <copy>mysqlsh -uadmin -p -h 10.0.1....</copy>
    ````

3. Change the MySQL Shell execution mode to SQL and run the following Auto Parallel Load command to load the airportdb tables into HeatWave.

    ````
    <copy>\SQL</copy>
    ````

    ````
    <copy>CALL sys.heatwave_load(JSON_ARRAY('airportdb'), NULL);</copy>
    ````
4. The compled load cluster screen should look like this:

    ![Connect](./images/11loadcluster01.png " ")

5.	Verify that the tables are loaded in the HeatWave cluster. Loaded tables have an AVAIL_RPDGSTABSTATE load status.

    ````
    <copy>USE performance_schema;</copy>
    ````
    ````
    <copy>SELECT NAME, LOAD_STATUS FROM rpd_tables,rpd_table_id WHERE rpd_tables.ID = rpd_table_id.ID;</copy>
    ````
    ![Connect](./images/11loadcluster02.png " ")

## **TASK 8:**  Run Queries in HeatWave

1. If not already connected with SSH, on Command Line, connect to the Compute instance using SSH

    (Example: **ssh -i ~/.ssh/id_rsa opc@&132.145.170..**)

2. On command Line, connect to MySQL using the MySQL Shell client tool

    (Example  **mysqlsh -uadmin -p -h10.0.1..**)

3. Change the MySQL Shell execution mode to SQL. Enter the following command at the prompt:
    ````
    <copy>\SQL</copy>
    ````

4.	Change to the airport database.  Enter the following command at the prompt:
    ````
    <copy>USE airportdb;</copy>
    ````
    ![Connect](./images/12hwqueries01.png " ")

 5. Turn on `use_secondary_engine` variable to use HeatWave
     ````
    <copy>SET SESSION use_secondary_engine=ON;</copy>
    ````
    
6. Query a - Find per-company average age of passengers from Switzerland, Italy and France

 7. Before Runing a query, use EXPLAIN to verify that the query can be offloaded to the HeatWave cluster. For example:

    ````
    <copy>EXPLAIN SELECT
    airline.airlinename,
    AVG(datediff(departure,birthdate)/365.25) as avg_age,
    count(*) as nb_people
FROM
    booking, flight, airline, passengerdetails
WHERE
    booking.flight_id=flight.flight_id AND
    airline.airline_id=flight.airline_id AND
    booking.passenger_id=passengerdetails.passenger_id AND
    country IN ("SWITZERLAND", "FRANCE", "ITALY")
GROUP BY
    airline.airlinename
ORDER BY
    airline.airlinename, avg_age
LIMIT 10;</copy>
    ````
    ![Connect](./images/12hwqueries02.png " ")

8. After verifying that the query can be offloaded, run the query and note the execution time. Enter the following command at the prompt:
     ````
    <copy>SELECT
    airline.airlinename,
    AVG(datediff(departure,birthdate)/365.25) as avg_age,
    count(*) as nb_people
FROM
    booking, flight, airline, passengerdetails
WHERE
    booking.flight_id=flight.flight_id AND
    airline.airline_id=flight.airline_id AND
    booking.passenger_id=passengerdetails.passenger_id AND
    country IN ("SWITZERLAND", "FRANCE", "ITALY")
GROUP BY
    airline.airlinename
ORDER BY
    airline.airlinename, avg_age
LIMIT 10;
</copy>
    ````
     ![Connect](./images/12hwqueries03.png " ")

 9. To compare the HeatWave execution time with MySQL DB System execution time, disable the `use_secondary_engine` variable to see how long it takes to run the same query on the MySQL DB System. For example:

 Enter the following command at the prompt:
     ````
    <copy>SET SESSION use_secondary_engine=OFF;</copy>
    ````

 10. Enter the following command at the prompt:
     ````
    <copy>SELECT
    airline.airlinename,
    AVG(datediff(departure,birthdate)/365.25) as avg_age,
    count(*) as nb_people
FROM
    booking, flight, airline, passengerdetails
WHERE
    booking.flight_id=flight.flight_id AND
    airline.airline_id=flight.airline_id AND
    booking.passenger_id=passengerdetails.passenger_id AND
    country IN ("SWITZERLAND", "FRANCE", "ITALY")
GROUP BY
    airline.airlinename
ORDER BY
    airline.airlinename, avg_age
LIMIT 10;</copy>
    ````
    ![Connect](./images/12hwqueries04.png " ")

 11. To see if `use_secondary_engine` is enabled (=ON)

 Enter the following command at the prompt:
     ````
    <copy>SHOW VARIABLES LIKE 'use_secondary_engine%';</copy>
    ````
 12. Runing additional queries. Remember to turn on and off the `use_secondary_engine`  to compare the execution time. 
   
    (Example  **SET SESSION `use_secondary_engine`=On;**) 

    (Example  **SET SESSION `use_secondary_engine`=Off;**)      

 13. Enter the following command at the prompt
     ````
    <copy>SET SESSION use_secondary_engine=ON;</copy>
    ````
 14. Query b -  Find top 10 companies selling the biggest amount of tickets for planes taking off from US airports.	Run Pricing Summary Report Query:

    ````
    <copy> SELECT
    airline.airlinename,
    SUM(booking.price) as price_tickets,
    count(*) as nb_tickets
FROM
    booking, flight, airline, airport_geo
WHERE
    booking.flight_id=flight.flight_id AND
    airline.airline_id=flight.airline_id AND
    flight.from=airport_geo.airport_id AND
    airport_geo.country = "UNITED STATES"
GROUP BY
    airline.airlinename
ORDER BY
    nb_tickets desc, airline.airlinename
LIMIT 10;
    </copy>
    ````
15. Enter the following command at the prompt:
     ````
    <copy>SET SESSION use_secondary_engine=OFF;</copy>
    ````
    Run Query b again:

    ````
    <copy> SELECT
    airline.airlinename,
    SUM(booking.price) as price_tickets,
    count(*) as nb_tickets
FROM
    booking, flight, airline, airport_geo
WHERE
    booking.flight_id=flight.flight_id AND
    airline.airline_id=flight.airline_id AND
    flight.from=airport_geo.airport_id AND
    airport_geo.country = "UNITED STATES"
GROUP BY
    airline.airlinename
ORDER BY
    nb_tickets desc, airline.airlinename
LIMIT 10;
    </copy>
    ````
16. Uery c - Give me the number of bookings that Neil Armstrong and Buzz Aldrin made for a price of > $400.00

    ````
    <copy>SET SESSION use_secondary_engine=ON;</copy>
    ````

    ````
    <copy>select firstname, lastname, count(booking.passenger_id) as count_bookings from passenger, booking   where booking.passenger_id = passenger.passenger_id  and passenger.lastname = 'Aldrin' or (passenger.firstname = 'Neil' and passenger.lastname = 'Armstrong') and booking.price > 400.00 group by firstname, lastname;</copy>
    ````
    ````
    <copy>SET SESSION use_secondary_engine=OFF;</copy>
    ````
    
    ````
    <copy>select firstname, lastname, count(booking.passenger_id) as count_bookings from passenger, booking   where booking.passenger_id = passenger.passenger_id  and passenger.lastname = 'Aldrin' or (passenger.firstname = 'Neil' and passenger.lastname = 'Armstrong') and booking.price > 400.00 group by firstname, lastname;</copy>
    ````

17. Keep HeatWave processing enabled

    ````
    <copy>SET SESSION use_secondary_engine=ON;</copy>
    ````
## **TASK 9:**  Connect to HeatWave using Workbench
1. At this point, you can also use MySQL Workbench from your local machine to connect to the MySQL endpoint using your new Compute instance as a jump box

2. In your pre-installed MySQL Workbench, configure a connection using the method "Standard TCP/IP over SSH" and use the credentials of the Compute instance for SSH

    **MySQL Workbench Configuration for MDS HeatWAve**
    ![MDS](./images/13workbench01.png " ") 
   
    **MySQL Workbench Use  for MDS HeatWAve**
    ![MDS](./images/13workbench02.png " ") 


## Learn More

* [Oracle Cloud Infrastructure MySQL Database Service Documentation ](https://docs.cloud.oracle.com/en-us/iaas/mysql-database)
* [MySQL Database Documentation](https://www.mysql.com)
## Acknowledgements
* **Author** -   Perside Foster, MySQL Solution Engineer,  
* **Contributors** -  Priscila Galvao, MySQL Solution Engineer, 
Mandy Pang, Principal Product Manager
* **Last Updated By/Date** - Priscila Galvao, MySQL Solution Engineer, August 2021

## Need Help?
Please submit feedback or ask for help using our [MySQL Support Forum](https://community.oracle.com/tech/developers/categories/MySQL). Please click the **Log In** button and login using your Oracle Account. Click the **Ask A Question** button to the left to start a *New Discussion* or *Ask a Question*.  Please include your workshop name and lab name.  You can also include screenshots and attach files.  Engage directly with the author of the workshop.

If you do not have an Oracle Account, click [here](https://profile.oracle.com/myprofile/account/create-account.jspx) to create one.

