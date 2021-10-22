# Graph Studio: Create a graph using PGQL CREATE PROPERTY GRAPH statement

## Introduction

In this lab you will create a graph from the `bank_accounts` and `bank_txns` tables using Graph Studio and the CREATE PROPERTY GRAPH statement.

The following video shows the steps you will execute in this lab.

[](youtube:5g9i9HA_cn0) Graph Studio: Create a graph.

Estimated Time: 15 minutes. 

### Objectives

Learn how to
- use Graph Studio and PGQL DDL (that is, CREATE PROPERTY GRAPH statement) to model and create a graph from existing tables or views.

### Prerequisites

- The following lab requires an Autonomous Database - Shared Infrastructure account. 
- And that the Graph-enabled user exists. That is, a database user with the correct roles and privileges exists.

## Task 1: Connect to your Autonomous Database using Graph Studio

1. If you have the Graph Studio URL then proceed to step 4. 

    Log in to the Oracle Cloud Console, choose the Autonomous Database instance, then Click the Tools tab on the details page menu on the left. 

   ![Oracle Cloud Console](./images/adw-details-tools-graph-studio.png)


2. Click the Graph Studio card to open in a new page or tab in your browser.   
   
   If your tenancy administrator provided you the Graph Studio URL to connect directly then use that instead.


3. Enter your Autonomous Database account credentials (`GRAPHUSER`/`gs_LLwid770#`) into the login screen:

    ![ALT text is not available for this image](./images/adw-graph-studio-login.png " ")

4. Then click the "Sign In" button. You should see the studio home page.   

    ![ALT text is not available for this image](./images/gs-graphuser-home-page.png " ") 

    Graph Studio consists of a set of pages accessed from the menu on the left. 

    The Home icon ![ALT text is not available for this image](images/home.svg " ") takes you to the Home page.  
    The Models icon ![ALT text is not available for this image](images/code-fork.svg " ") takes you to the Models page where you start modeling your existing tables and views as a graph and then create, or instanstiate, a graph.  
    The Graph page ![ALT text is not available for this image](images/radar-chart.svg " ") lists existing graphs for use in notebooks.  
    The Notebook page ![ALT text is not available for this image](images/notebook.svg " ") lists existing notebooks and lets you create a new one.  
    The Jobs page ![ALT text is not available for this image](images/server.svg " ") lists the status of background jobs and lets you view the associated log if any.  


## Task 2: Create a small 2GB execution environment

1. Before creating a graph we will **create an execution environment** for running notebook paragraphs and loading the graph into an in-memory representation.   
   
   Click the pull-down menu under the username `GRAPHUSER` shown in the top right corner of the Graph Studio browser window.  
   Select the `Environment` menu item.  

   ![ALT text is not available for this image](images/ll-user-pulldown-menu.png " ")
2. Enter a **value of 2 (GB)** for the memory size and then click `Create`.  

   ![ALT text is not available for this image](images/ll-create-env-detail.png " ") 
3. The Jobs page will show the status. Meanwhile let's start modeling and creating a graph from the existing tables.  

   ![ALT text is not available for this image](images/ll-create-env-status.png " ")

## Task 3: Create a graph of accounts and transactions from the corresponding tables

1. Click the Models icon to navigate to the start of the modeling workflow.  
   Then Click `Create`.  
   ![ALT text is not available for this image](images/models-create.png " ")  

2. Then select the `BANK_ACCOUNTS` and `BANK_TXNS` tables.   
![ALT text is not available for this image](./images/modeler-select-tables.png " ")

2. Move them to the right, that is, click the first icon on the shuttle control.   

   ![ALT text is not available for this image](./images/modeler-selected-tables.png " ")

3.  Click next to get a suggested model. We will edit and update this model.  

    The suggested model has `BANK_ACCOUNTS` as a vertex and `BANK_TXNS` as an edge.   

  ![ALT text is not available for this image](./images/18-ll-modeler-suggested-model.png " ")    

  We wish to update the default vertex and edge labels and then confirm that the edge has the right direction from source `from_acct_id` to destination `to_acct_id`. 

4.  Click the Source tab to bring up the existing statement and the edit dialog.  
    
    The generated Create Property Graph statement should look similar to the one in the screenshot below.   
    Note the following about that statement:
    - The **edge direction** is wrong. The source is `to_acct_id` instead of `from_acct_id`.
    - There are no Vertex and Edge labels

  ![ALT text is not available for this image](./images/modeler-source-incorrect-ddl.png " ")   

  We will be using vertex and labels in (PGQL) queries in the next lab.  
  The labels can be added and the edge direction swapped using the GUI. However it is simpler update the CREATE PROPERTY GRAPH statement and do both in one step.   

  **Replace** the existing statement with the following one which specifies that `BANK_ACCOUNTS` is a vertex table with label `ACCOUNTS` and `BANK_TXNS` is an edge table with label `TRANSFERS`. And the directed edge is from the source `from_acct_id` to destination `to_acct_id`.  
    ```
    <copy>
    CREATE PROPERTY GRAPH bank_graph
        VERTEX TABLES (
            BANK_ACCOUNTS as ACCOUNTS 
            KEY (ACCT_ID) 
            LABEL ACCOUNTS
            PROPERTIES (ACCT_ID, NAME)
        )
        EDGE TABLES (
            BANK_TXNS 
            KEY (FROM_ACCT_ID, TO_ACCT_ID, AMOUNT)
            SOURCE KEY (FROM_ACCT_ID) REFERENCES ACCOUNTS
            DESTINATION KEY (TO_ACCT_ID) REFERENCES ACCOUNTS
            LABEL TRANSFERS
            PROPERTIES (FROM_ACCT_ID, TO_ACCT_ID, DESCRIPTION, AMOUNT)
        )
    </copy>
    ```

   ![ALT text is not available for this image](images/correct-ddl-save.png " " )  

   **Important:** Click the **Save** (floppy disk icon) to commit the changes. 

5. Then click the Designer tab to confirm that the model now has a vertex table and an edge table.  
  ![ALT text is not available for this image](./images/20-modeler-fix-txn-label.png " ")  

6. Click `Next` and then click `Create Graph` to move on to the next step in the flow.   

   Enter `bank_graph` as the graph name.  
   That graph name is used throughout the next lab.  
   Do not enter a different name because then the queries and code snippets in the next lab will fail.  
   
   Enter a model name (for example, `bank_graph_model`), and other optional information.  
   ![ALT text is not available for this image](./images/modeler-create-graph-dialog.png " ")

7. Graph Studio modeler will now save the metadata and start a job to create the graph.  
   The Jobs page shows the status of this job. 

   ![ALT text is not available for this image](./images/23-jobs-create-graph.png " ")  

   You can then interactively query and visualize the graph in a notebook after it's loaded into memory.


Please **proceed to the next lab** to do so.

## Acknowledgements
* **Author** - Jayant Sharma, Product Management
* **Contributors** -  Jayant Sharma, Product Management
* **Last Updated By/Date** - Jayant Sharma, September 2021
  
