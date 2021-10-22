# Lakehouse: Putting it Together for Analytics

## Introduction

The Data Lake is really all of the pieces working together to ingest data in many different forms from APIs, database, file formats and locations. The catalog documents the metadata and business value of the data with classifying data with business meaning and where the data is found. Data integrations allows for ETL processes and loading of new data assets along with the OCI Data Flows to process and filter new data and store as new data assets. Then the querying of the data whether or not using SQL to pull from the data lake or other reporting tools, the data assets in the data lake can now be consumed for business reporting and analytics.

### Objectives

In this lab, you will:
* Query the data values
* Validate that new data is being loaded
* Review the components of the Data Lake

Estimated Time:15 minutes

## Task 1: SQL Queries

Navigate from the main menu to Autonomous Data Warehouse. Select the lakehousedb. If the database is not listed, double check the compartment is set to lakehouse1.

![Database](./images/databaselisting.png " ")

Click on the database and then proced to click on the Tools Tab and click on Open Database Actions.

![Database Actions](./images/dbactions.png " ")

Click on SQL to execute the query to create the table.

![SQL](./images/SQL_queries.png " ")

You can just simply query the MOVIE_GENRE table to view data, or create the following view to see the additional data along with the join to the MOVIE_GENRE entity.

```
<copy>
CREATE or REPLACE VIEW MOVIE_VW as
SELECT
    ENTERED_TIME,
    PRICE,
    CUSTID,LAST_NAME, COUNTRY,
    GENREID,NAME,
    MOVIEID,
    ACTIVITY,
    RECOMMENDED
FROM
    ADMIN.MOVIE_GENRE, customer_contact,GENRE
    where genre_id=genreid and custid=cust_id;
</copy>
```
This view will demonstrate the combination for the customer, country and if they would recommend the movie and can be grouped by genre and other activities.

A simple select statement can be done to just see the data based on this view and other joins are possible.

```
<copy>
SELECT * FROM MOVIE_VW;
</copy>
```
![SQL](./images/SQL_output.png " ")


## Task 2: OCI Data Catalog - View of the Data Lake

You have updated data, added new tables and views into the database. Let's take another look at the OCI Data Catalog to see that it captured the changes and the new entities.

Navigate to the menu Cloud Menu. Click on Analytics & AI and click on Data Catalog under the Data Lake header.

Click on DataCatalogLakehouse1 from the Data Catalogs. Verify compartment if you do not see it listed.

![SQL](./images/Current_Catalog.png " ")

Click on Data Assets and click on Harvest using the dropdown menu for the database Data Asset. This harvesting for the Data Catalog should be scheduled to automatically pull the entity informaiton into the Data Asset, but for now in the lab you can run this manually.

Now if you go back to the Home Tab fro the Data Catalog, you will discover that there are now 8 Data Entities are being kept up to data in the Data Catalog.

![New Entities](./images/new_entities.png " ")

Click on Entities just to verify that all of the tables and views are now here.

![Entities List](./images/final_catalog.png " ")

## Task 3: View of the Oracle Data Lakehouse

The Oracle Data Lakehouse uses the tools under the main menu of ANalytics & AI. The Data Lake header contains the services needed to create integrations, catalog and data flows to build the lakehouse. The configuration that was setup in the beginning allows for consistent security through out the different pieces of the data lake environment which also grants least privilege for administration, developers and consumers of the data lake.

Take a quick view at the steps that you went through to create the lakehouse that ended with a view or queries to be utilized in further analysis.

![Data Lake Overview](images/data_lake_overview.png " ")

## Next Steps
Congratulations! You have now completed the Oracle Cloud Lakehouse LiveLab. You have seen how to populate and manage the Data Lake, and the next steps are pulling together some analytics on the data and using these tools with the Data Lake Assets.

Be sure to check out the labs on Oracle Machine Learning and how the Lakehouse fits into the Movie Stream story lab along with several other labs on analytics and ADW.

## Acknowledgements

* **Author** - Michelle Malcher, Database Product Management, Massimo Castelli, Senior Director Product Management
* **Last Updated By/Date** - Michelle Malcher, Database Product Management, September 2021
