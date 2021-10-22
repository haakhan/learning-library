# Connect Oracle GoldenGate to Autonomous Data Warehouse

## Introduction

For the purposes of this workshop, Oracle Autonomous Data Warehouse (ADW) serves as the source database for your Oracle GoldenGate Marketplace deployment. This lab walks you through the steps to connect your Oracle GoldenGate Marketplace deployment to ADW.

Estimated time: 15 minutes

### Objectives

In this lab, you will:
* Download the ADW credentials
* Upload the ADW credentials to the Oracle GoldenGate Marketplace compute instance
* Add the ADW credentials in the Oracle GoldenGate Administration Server

### Prerequisites

Follow the instructions for [Connecting to a Linux Instance ](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/accessinginstance.htm#linux) to enter your private key for the Oracle GoldenGate Marketplace Compute instance.

## Task 1: Download the Target ADW Client Credentials

1.  In the OCI Console breadcrumb, click **Autonomous Database**, and then select **TargetADW** from the list of databases.

2.  On the Target ADW Autonomous Database Details page, click **DB Connection**.

    ![](images/02-01.png " ")

2.  In the DB Connection panel, click **Download Wallet**.

    ![](images/02-02.png " ")

3.  In the Download Client Credentials (Wallet) dialog, enter the Target ADW Admin password twice, and then click **Download**.

4.  Close the DB Connection panel.

## Task 2: Upload the Target ADW Credentials to Oracle GoldenGate

1.  In the OCI Console, open the navigation menu (hamburger icon), click **Compute**, and then click **Instances**.

    ![](images/02-01-compute.png " ")

2.  Under **List Scope**, ensure that the correct **Compartment** is selected for your workshop. You can find your compartment information in the Workshop Details of this LiveLab.

3.  Select **Oracle GoldenGate 21.1.0.0.1 Microservices Edition for Oracle**.

    ![](images/02-03-compute-instances.png " ")

4.  On the Instance Details page, under **Instance Access**, copy the **Public IP Address**.

    ![](images/02-04.png " ")

5.  Using a secure FTP client of your choosing, open a connection to the Oracle GoldenGate Marketplace instance using its Public IP Address.

    ```
    <copy>sftp -i <private-SSH-key> opc@<ip-address></copy>
    ```

6.  Upload the wallet\_ATP.zip to /home/opc.

    ```
    <copy>put <local-path>/Wallet_ADW.zip</copy>
    ```

7.  SSH to the compute instance.

    ```
    <copy>ssh -i <private-SSH-key> opc@<ip-address></copy>
    ```

8.  Upload the wallet\_ADW.zip and then extract its contents to a new directory, such as **wallet\_ADW**.

    ```
    <copy>mkdir wallet_ADW
unzip Wallet_ADW.zip -d wallet_ADW</copy>
    ```

## Task 3: Add the Target ADW Credential in the Oracle GoldenGate Administration Server

1.  Launch the OCI GoldenGate Deployment Console.

2.  Open the navigation menu (hamburger icon) and then click **Configuration**.

    ![](images/03-02.png " ")

3.  Copy the TargetADW connection string in the User ID column, and then paste it into a text editor.

    ![](images/03-03.png " ")

4.  Edit the TargetADW connection string, replacing the value for **MY\_WALLET\_DIRECTORY** with the location where you unzipped the wallet_ADW.zip. For example, **/home/opc/wallet\_ADW**.

    ![](images/04-04.png " ")

5.  In a new browser tab or window, use the Public IP and port 443 (**https://&lt;public-ip&gt;:443**) to open the Service Manager.

6.  Log in to the Service Manager using **oggadmin** credentials found in **/home/opc/ogg-credentials.json**.

7.  In the Service Manager, under **Services**, click the port number associated with the Administration Server. The Administration Server opens in a new browser tab. If you're prompted to log in again, use the same oggadmin credentials.

    ![](images/04-03.png " ")

8.  In the Administration Server, open the navigation menu (hamburger icon), and then select **Configuration**.

    ![](images/04-07.png " ")

9.  Click **Add Credential**.

    ![](images/03-09.png " ")

10. Enter the following information, and then click **Submit**:

    * For **Credential Domain**, enter **OracleGoldenGate**.
    * For **Credential Alias**, enter the ADW database name (low) from /home/opc/wallet\_ADW/tnsnames.ora. For example, **adw&lt;user&gt;\_low**.
    * For **User ID**, paste the ADW connection string from step 4.
    * For **Password**, enter the ggadmin password created when you registered the Target Database.

    ![](images/04-10.png " ")

In this lab, you created a connection from the Oracle GoldenGate Marketplace instance to the target ADW database. You may now **proceed to the next lab**.

## Acknowledgements

* **Author** - Jenny Chan, Consulting User Assistance Developer, Database User Assistance
* **Contributors** -  Julien Testut, Database Product Management
* **Last Updated By/Date** - Jenny Chan, September 2021
