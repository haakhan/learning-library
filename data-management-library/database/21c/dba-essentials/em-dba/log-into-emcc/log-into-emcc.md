# Log in to Oracle EMCC

## Introduction

This lab shows how to log in to Oracle Enterprise Manager Cloud Control (Oracle EMCC) and access the homepage. 

Estimated Time: 5 minutes

### Objectives

Log in to Oracle EMCC and select a personal homepage.

### Prerequisites

Oracle EMCC 13.5 installed with Oracle Database 19c as the repository.

## Task 1: Log in to Oracle EMCC

From Oracle EMCC, you can do various activities, such as view details of your Oracle Database, monitor the database, and perform administrative tasks.

1. Log in to your host as *oracle*, the user who can perform database administration.

2. Open a web browser and enter the URL for Oracle EMCC.  

    <!-- Replace 0.0.0.0 and enter the actual IP address of the host machine. -->

   <TBD> [https://0.0.0.0:7803/em](https://0.0.0.0:7803/em)  

   **Note:** If you get a security certificate warning, you can safely ignore the error. Depending on your web browser, click *Advanced* or *More Information* and continue to the login page.

   ![Oracle EMCC Login URL](images/emcc-001-login-url.png)

    > **URL Syntax**  
    > The Oracle EMCC URL comprises the IP address of the host and the port number - `https://ipaddress:portnumber/em`.  
    For this lab, the host IP address for Oracle EMCC is <TBD> *0.0.0.0* and the port number is *7803*. 

   <!--To view your hostname, open a terminal window and run the command *hostname*. -->

3. Enter the login credentials for Oracle EMCC.  
   **Username** - *sysman* (not case sensitive)  
   **Password** - *welcome1*
   
   ![Oracle EMCC Login Page](images/emcc-002-login-page.png)

4. The first time you log in to Oracle EMCC, the web browser displays a License Agreement. Click **I Accept** to confirm your compliance and continue to log in.

   ![License Agreement](images/emcc-003-license.png)
   
   Henceforth, the License Agreement does not appear on subsequent logins.

5. Oracle EMCC opens and displays the Welcome page. You can select a different homepage from the given options and change the default homepage.  

   Your personal homepage will appear from the next login onwards.

   ![Oracle EMCC Welcome page](images/emcc-004-homepage.png)
   
Congratulations! You have successfully logged in to Oracle EMCC. You can explore Oracle EMCC and perform administrative tasks for your Oracle Database.

You may now **proceed to the next lab**.

## Acknowledgements

- **Author** - Manish Garodia, Principal User Assistance - Developer, Database Technologies

- **Contributors** - Suresh Rajan, Kurt Engeleiter, Prakash Jashnani, Subhash Chandra 

- **Last Updated By/Date** - Manish Garodia, October 2021
