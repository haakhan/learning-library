# Select and manipulate data using the transparency layer

## Introduction

This lab shows how to use the transparency layer classes to work with data and to perform exploratory analysis of the data.

Estimated Lab Time: 30 minutes

### About data selection and manipulation
The transparency layer classes allow you to convert select Python objects to Oracle Autonomous Database objects and also call a range of familiar Python functions that are overloaded to call the corresponding SQL on tables in the
database.
The Oracle Machine Learning for Python (OML4Py) transparency layer supports functions that interact with database data and enables you to:
* Load Python `pandas.DataFrame` objects to Oracle Database to create database tables
* Access and manipulate database tables and views through the use of proxy objects
* Overload Python functions, translating their functionality into SQL
* Leverage proxy objects for database data
* Use familiar Python syntax to manipulate database data

### Objectives

In this lab, you will learn how to:
  * Use the `oml.push` function to create a temporary table
  * Work with table rows and columns using proxy objects
  * Work with `pandas.DataFrame` objects
  * Use the `append`, `concat` and `merge` functions to manipulate data
  * Use the `split` and `KFold` functions to partition the data
  * Use the `crosstab` and `pivot_table` functions on an OML DataFrame proxy
  * Use the `oml.boxplot` and `oml.hist` functions to create plots 
  * Manage and explore data using OML4Py Transparency Layer functions
  * Use `cx_Oracle` functions to submit SQL queries from Python

## Access the notebook for this Lab

1. Go back to the main notebooks listing by clicking on the "hamburger" menu (the three lines) on the upper left of the screen, and then select **Notebooks**.

 ![Oracle Machine Learning Notebooks menu](images/go-back-to-notebooks.png " ")

2. Click the **Lab 2 notebook name** to view it.
   <if type="freetier">
   ![Open Lab 2 notebook ft](images/click-on-lab2-ft.png " ") </if>
   <if type="livelabs">
   ![Open Lab 2 notebook ll](images/click-on-lab2-ll.png " ") </if>

  OML Notebooks will create a session and make the notebook available for editing.

  You can optionally click the **Run all paragraphs** (![](images/run-all-paragraphs.png =20x*)) icon, and then click **OK** to confirm to refresh the content with your data, or just scroll down and read the pre-recorded results.  
   
  ![Lab 2 main screen](images/lab2-main.png " ")

> **NOTE:** If you had problems downloading and extracting the ZIP file for the labs, please [**CLICK HERE** to download the lab2\_select\_manipulate\_data.json notebook file](./../notebooks/lab2_select_manipulate_data.json?download=1). Download the notebook file for this lab to your local machine and then import it like illustrated in **Lab 1, Task 2**.

## Task 1: Import libraries and create Oracle Machine Learning dataFrame proxy object
Follow the flow of the notebook by scrolling to view and run each paragraph of this lab.

Scroll down to the beginning of Task 1.

  ![Lab 2 Task 1 screen](images/lab2-task1.png " ")

## Task 2: Select table columns using proxy object CUST_DF
Follow the flow of the notebook by scrolling to view and run each paragraph of this lab.

Scroll down to the beginning of Task 2.

  ![Lab 2 Task 2 screen](images/lab2-task2.png " ")

## Task 3: Select table rows using proxy object CUST_DF
Follow the flow of the notebook by scrolling to view and run each paragraph of this lab.

Scroll down to the beginning of Task 3.

  ![Lab 2 Task 3 screen](images/lab2-task3.png " ")

## Task 4: Use OML DataFrame proxy objects
Follow the flow of the notebook by scrolling to view and run each paragraph of this lab.

Scroll down to the beginning of Task 4.

  ![Lab 2 Task 4 screen](images/lab2-task4.png " ")

## Task 5: Use the split and kfold functions
Follow the flow of the notebook by scrolling to view and run each paragraph of this lab.

Scroll down to the beginning of Task 5.

  ![Lab 2 Task 5 screen](images/lab2-task5.png " ")

## Task 6: Use the crosstab and pivot_table functions on a dataFrame proxy object
Follow the flow of the notebook by scrolling to view and run each paragraph of this lab.

Scroll down to the beginning of Task 6.

  ![Lab 2 Task 6 screen](images/lab2-task6.png " ")

## Task 7: Use the oml.boxplot and oml.hist functions
Follow the flow of the notebook by scrolling to view and run each paragraph of this lab.

Scroll down to the beginning of Task 7.

  ![Lab 2 Task 7 screen](images/lab2-task7.png " ")

## Task 8: Manage and explore data using transparency layer functions
Follow the flow of the notebook by scrolling to view and run each paragraph of this lab.

Scroll down to the beginning of Task 8.

  ![Lab 2 Task 8 screen](images/lab2-task8.png " ")

## Task 9: Use cx_Oracle functions
Follow the flow of the notebook by scrolling to view and run each paragraph of this lab.

Scroll down to the beginning of Task 9.

  ![Lab 2 Task 9 screen](images/lab2-task9.png " ")  

You can now *proceed to the next lab*.

## Learn More

* [Transparency Layer Functions](https://docs.oracle.com/en/database/oracle/machine-learning/oml4py/1/mlpug/oml4py-advantages.html#GUID-2AD97DE9-B43F-4B0B-8269-C6DFB47576A9)
* [Prepare and Explore Data](https://docs.oracle.com/en/database/oracle/machine-learning/oml4py/1/mlpug/prepare-and-explore-data.html#GUID-10C55FA5-2F98-4B52-9C56-4EA43E62D786)
* [Oracle Machine Learning Notebooks](https://docs.oracle.com/en/database/oracle/machine-learning/oml-notebooks/)

## Acknowledgements
* **Authors** - Marcos Arancibia, Product Manager, Machine Learning; Jie Liu, Data Scientist; Moitreyee Hazarika, Principal User Assistance Developer
* **Contributors** -  Mark Hornick, Senior Director, Data Science and Machine Learning; Sherry LaMonica, Principal Member of Tech Staff, Machine Learning
* **Last Updated By/Date** - Marcos Arancibia and Jie Liu, October 2021
