# Lab 1b: Load Initial Data

## Introduction

Load the initial set of data into the Autonomous Data Warehouse and Load data into object storage

Estimated Lab Time: 15 minutes

### Objectives

In this lab, you will:
* Load from OCI Object Storage a data set into ADW as part of the data lake

> **Note:** While this lab uses ADW, the steps are identical for loading data into an ATP database.

Estimated Time:10 minutes

### About Product

In this lab, we will learn more about the Autonomous Database's built-in Data Load tool - see the [documentation](https://docs.oracle.com/en/cloud/paas/autonomous-database/adbsa/data-load.html#GUID-E810061A-42B3-485F-92B8-3B872D790D85) for more information.

## Task 1: Configure the Object Storage Connections

In this step, you will set up access to the two buckets on Oracle Object Store that contain data that we want to load - the landing area, and the 'gold' area.

1. In your ADW database's details page, click the Tools tab. Click **Open Database Actions**

	  ![Click Tools, then Database Actions](images/launchdbactions.png " ")

2. On the login screen, enter the username ADMIN, then click the blue **Next** button.

3. Enter the password for the ADMIN user you entered when creating the database.

4. Under **Data Tools**, click **DATA LOAD**

    ![Click DATA LOAD](images/dataload.png " ")

5. In the **Explore and Connect** section, click **CLOUD LOCATIONS** to set up the connection from your Autonomous Database to OCI Object Storage.

    ![Click CLOUD LOCATIONS](images/cloudlocations.png " ")

6. To add access to the Moviestream landing area, click **+Add Cloud Storage** in the top right of your screen.

    In the **Name** field, enter 'MovieStreamLanding'

    > **Note:** Take care not to use spaces in the name.

    Leave the Cloud Store selected as **Oracle**.

    Copy and paste the following URI into the URI + Bucket field:

    ```
    <copy>
    https://objectstorage.us-ashburn-1.oraclecloud.com/n/c4u04/b/moviestream_landing/o
    </copy>
    ```

    Select **No Credential** as this is a public bucket.

    Click the **Test** button to test the connection. Then click **Create**.

7. The page now invites us to load data from this area. In this case, we want to set up access to an additional cloud location first. Click **Data Load** in the top left of your screen to go back to the main Data Load page.

    ![Click Data Load](images/todataload.png " ")

8. In the **Explore and Connect** section, click **CLOUD LOCATIONS**, then to add access to the Moviestream gold area, click **+Add Cloud Storage**.

- In the **Name** field, enter 'MovieStreamGold'

    > **Note:** Take care not to use spaces in the name.

- Leave the Cloud Store selected as **Oracle**
- Copy and paste the following URI into the URI + Bucket field:

    ```
    <copy>
    https://objectstorage.us-ashburn-1.oraclecloud.com/n/c4u04/b/moviestream_gold/o
    </copy>
    ```

- Select **No Credential** as this is a public bucket.
- Click the **Test** button to test the connection. Then click **Create**.

    We now have two cloud storage locations set up.

    ![Cloud Storage Locations](images/cloudstoragelocations.png " ")

## Task 2: Load Data from Files in Object Storage Using Data Tools

In this step, we will perform some simple data loading tasks, to load in CSV files from Object Storage into tables in our Autonomous Database.

1. To load or link data from our newly configured cloud storage, click the **Data Load** link in the top left of your screen.

    ![Click Data Load](images/backtodataload.png " ")

2. Under **What do you want to do with your data?** select **LOAD DATA**, and under **Where is your data?** select **CLOUD STORAGE**, then click **Next**.

    ![Select Load Data, then Cloud Storage](images/loadfromstorage.png " ")

3. From the MOVIESTREAMGOLD location, drag the **customer_contact** folder over to the right hand pane. Note that a dialog box appears asking if we want to load all the files in this folder to a single target table. In this case, we only have a single file, but we do want to load this into a single table. Click **OK**.

4. Next, drag the **genre** folder over to the right hand pane. Again, click **OK** to load all files into a single table.


5. Click the pencil icon for the **customer_contact** task to view the settings for this load task.

    ![View settings for customer_contact load task](images/cc_viewsettings.png " ")

6. Here we can see the list of columns and data types that will be created from the csv file. They all look correct, so click **Close** to close the settings viewer.

7. Click the pencil icon for the **genre** task to view its settings. This should show just two columns to be created - **GENRE_ID** and **NAME**. Click **Close** to close the settings viewer.

8. Now click the Play button to run the data load job.

    ![Run the data load job](images/rundataload.png " ")

    The job should take about 20 seconds to run.

9. Check that both data load cards have green tick marks in them, indicating that the data load tasks have completed successfully.

    ![Check the job is completed](images/loadcompleted.png " ")

10. Now, to load some more data from the MovieStream landing area, click the **Data Load** link in the top left of your screen.

    ![Click Data Load](images/backtodataload.png " ")

11. Under **What do you want to do with your data?** select **LOAD DATA**, and under **Where is your data?** select **CLOUD STORAGE**, then click **Next**

12. This time, select **MOVIESTREAMLANDING** in the top left of your screen.

    ![Click Data Load](images/selectlanding.png " ")

13. From the MOVIESTREAMLANDING location, drag the **customer_extension** folder over to the right hand pane and click **OK** to load all objects into one table.

14. Drag the **customer_segment** folder over to the right hand pane and click **OK**.

15. Drag the **pizza_location** folder over to the right hand pane and click **OK**.

16. Click the Play button to run the data load job.

    ![Run the data load job](images/runload2.png " ")

    The job should take about 20 seconds to run.

17. Check that all three data load cards have green tick marks in them, indicating that the data load tasks have completed successfully.

    ![Check the job is completed](images/loadcompleted2.png " ")

18. Click the **Done** button in the bottom right of the screen.

This completes the Data Load lab. We now have a full set of structured tables loaded into the Autonomous Database from the MovieStream Data Lake, with suitable constraints set up on the tables to avoid errors in attempting to load duplicate rows or invalid data. We will be working with these tables in later labs.

You may now [proceed to the next lab](#next).

## Acknowledgements

* **Author** - Michelle Malcher, Database Product Management
* **Contributors** -  Niay Panchal, Mike Matthew and Marty Gubar, Autonomous Database Product Management
* **Last Updated By/Date** - Michelle Malcher, Database Product Management, September 2021
