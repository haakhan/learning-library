# OCI Data Flow in the Data Lake

## Introduction

Data is constantly growing being enhanced, validated and updated. That is why once you have the data assets you need to make sure that processing continues to manage the data assets and provide updated values you data lake.

OCI Data Flows handles these processes by loading new data or updating.

### Objectives

* Learn how to define OCI Data Flow
* Learn how to create an OCI Data Flow App
* Learn how to schedule to automate OCI Data Flow Apps

## Task 1: Define OCI Data Flow

In this step, we are going to use again Quick Actions to click on Create Data Flow and then use the designer to setup the source and target along with any other filters we would like.

![Create Data Flow](./images/create_dataflow.png " ")

By default, at the bottom of the designer,  you want to enter the name for the New Data Flow, DataFlow_UploadGenre, and Select the Project that was created in the last lab.

![Create Data Flow](./images/dataflow1.png " ")

Then click Create. This way you can save as you go along to in order not to lose any changes.

From the toolbar, there are sources, targets, filters, joins and other options. You are going to drag the source icon over to the design area. Then start to fill out the details for the source by clicking on Select, and then choose the ADW asset that was created in the first lab. Select the Default Connection, and in Schema, ADMIN. For the Entiy choose the MOVIE_GENRE table. 

![Create Data Flow](./images/dataflow2.png " ")

Now you are going to drag the Target icon over to the designer area. Target is going to be defined as the Object Storage that was created for the dataflow-warehouse. You can insert, overwrite or merge data with the existing data, and even create a new file or table here. This lab, you are just going to insert data, and choose one file which will overwrite the file each time.

![Create Data Flow](./images/dataflow3.png " ")

Then click on the Data Entity and in the next menu type the name fo the folder **File_output**. Choose JSON file. This will put the file based on the data and joins that you create into the data lake and allow other processes to use the data.

![Create Data Flow](./images/dataflow5.png " ")

Save at this step, since you now have your source and target. Now you need to connect the source to the target. Drag the icon onto the designer area between the source and the target.

![Create Data Flow](./images/dataflow4.png " ")

After Saving the dataflow, click on Validate, and the Snapshot should show 0s for Errors and Warnings.

![Create Data Flow](./images/dataflow6.png " ")

## Task 2: Create an Application for Automation

Now you are going to navigate back to the data integration workspace, and click on Application. Click on create application.

![Create Application](./images/create_app.png " ")

Click on Save and Close. It is just a shell of an application where you can now publish tasks to be scheduled and run through the application.

## Task 3: Create and Schedule OCI Data Flow Apps for Automation

Now you are going to navigate back to the project. Click on Task under Details and click on Create Task and choose Integration Task. This task is going to be included in the application.

![Create Data Flow](./images/integrationtask_a.png " ")

Under Data Flow, you are going to click Select and add the Data Flow that you just finished creating in the previous task. Then click Save and Close.

![Create Data Flow](./images/integrationtask.png " ")

Click on the menu for the task and select Publish to Application.

![Add Task](./images/add_task.png " ")

Choose the application that was just created in Task 2.

![Add Task](./images/publish_to_app.png " ")

After the task has been added you will see run task or schedule, and you can navigate to the application. For regular loads of this data and automation, you are going to want to schedule the job to run. Again to see how this is working now, click on Run.

![Run App](./images/run_app.png " ")

You may now [proceed to the next lab](#next).

## Acknowledgements

* **Author** - Michelle Malcher, Database Product Management, Massimo Castelli, Senior Director Product Management
* **Contributors** - 
* **Last Updated By/Date** - Michelle Malcher, Database Product Management, September 2021
