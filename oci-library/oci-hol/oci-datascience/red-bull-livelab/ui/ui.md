# UI Access 

## Introduction

This lab explains the steps to deploy the UI access, that aready exists in your jupyter notebook to predict first 5 drivers for a given race. So this lab is just to explain what these files and their functions are doing to and for our model.      

Estimated Time: 60 minutes

### Objectives

In this lab, you will:
* Deploy UI Access to predict first 5 drivers for a given race

### Prerequisites

* An Oracle Free Tier, Always Free, Paid or LiveLabs Cloud Account


## **Task 1**: Deploy UI Access to predict first 5 drivers in a given race

Navigate to the ``` /redbull-analytics-hol/beginners/web ``` directory in your Jupyter Notebook session. Below we have provided a step-by-step explaination for deploying UI Access to predict first 5 drivers in a given race

1. In the ``` predictor.py ```, we first load the trained model and the dataset that we saved in the previous labs. 

  ![Image alt text](images/picture1.png)


2. After loading the data, we have created a prediction method using python. Within the function we are making a call to 'predict', which is function of scikit-learn library. 

  ![Image alt text](images/picture8.png)

  ![Image alt text](images/picture9.png)

3. Before executing or compiling anything, it's always a good idea to test, and that's what we're doing next. In the ``` testpredictor.py```, we’re feeding some input (testing with Silverstone results) to determine if it meets our expectations with respect to its output. 

  ![Image alt text](images/picture2.png)

4. In the ``` app.py ``` , you can see, in this first call out, we see the predictor being called and then, in the second callout, we see an if function creating a server port to call the predictor itself.

  And it's important to note that the second call-out is executed first, which, after opening a server port, calls the predictor. 

  ![Image alt text](images/picture3.png)

5. Let’s go back to the launcher/dashboard by clicking ```File > New > Launcher```, then click on the terminal icon you see called out in this screenshot. 

  ![Image alt text](images/picture3.png)

6. Running the `start` terminal command in the callout here launches the webserver.If you need to stop the server for any reason, use the stop command you see in the call out. There aren’t many use cases where this would be useful during this lab, but it’s good to know.


  Execute next command to start:

    ```
    <copy>
    ./launchapp.sh start
    </copy>
    ```

  To stop:

    ```
    <copy>
    ./launchapp.sh stop
    </copy>
    ```

  ![Image alt text](images/picture5.png)

7. Now you can test using your VM IP: http://<xxxx.xxx.xxx.xxx>:8080/ . 

  Choose which track and weather you’d like to see reflected in your top 5 driver results. Ideally, your choices will determine the five drivers which will be listed after clicking Predict.

  Note that the XXXX you see in the title of this slide is the same IP you’ve used to access your Jupyter notebook. We’re just changing the 8001 to 8080 in a tab.

  ![Image alt text](images/picture6.png)

8. Here’s what you should see on your end after clicking the Predict button
  
  ![Image alt text](images/picture7.png)


Congratulations! You have completed this workshop!


## Acknowledgements
* **Author** - Ignacio Martinez, Principal Advanced Support Engineer
* **Last Updated By/Date** - Samrat Khosla, Advanced Data Services, September 2021

## Need Help?
Please submit feedback or ask for help using our [LiveLabs Support Forum](https://community.oracle.com/tech/developers/categories/livelabsdiscussions). Please click the **Log In** button and login using your Oracle Account. Click the **Ask A Question** button to the left to start a *New Discussion* or *Ask a Question*.  Please include your workshop name and lab name.  You can also include screenshots and attach files.  Engage directly with the author of the workshop.

If you do not have an Oracle Account, click [here](https://profile.oracle.com/myprofile/account/create-account.jspx) to create one.
