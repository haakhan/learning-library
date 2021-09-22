d#Lab 3: Train Anomaly Detection Model And Detect

## Introduction

In this session, we will show you how to train an anomaly detection model, and make predictions with new data.

***Estimated Lab Time***: 30 minutes

### Objectives

In this lab, you will:
- Learn to train an anomaly detection model with created data asset
- Learn to verify the trained model performance
- Upload testing data to check detection result

### Prerequisites
- A Free tier or paid tenancy account in OCI
- Understand basic model terminology FAP - False Alarm Probability


## Task 1: Create a Model

Creating a model is requiring the 3 actions to kick off training the AD model.

* Select the proper compartment and data asset that we just created.
* Set training parameters
* Train a model

Select the proper compartment(e.g, the compartment matching your name or company name), and then the project you have created.
![](../images/selectCompartmentModelTrain.png " ")

Once the project ad_demo is selected, it will navigate the User to Created Anomaly Detection Project, then click "Create and Train Model".
![](../images/5_create_a_new_model.png " ")

The data asset created in previous lab session should be pop up in the drop down menu. Click "Next" button.
![](../images/choose_an_existing_dataset.png " ")

This takes us to "Train Model" form with parameter selections.

We can specify FAP(false alarm probability) and Train Fraction Ratio. The default values for these are 0.01 and 0.7 (implying 70%) respectively.

###FAP (False Alarm Probability)

FAP stands for False Alarm Probability, which is basically the likelihood (percentage) of a timestamp is flagged as anomaly in the clean (anomaly-free) training data. It is calculated at every signal level and then averaged across all signals as the final achieved FAP by our model.  

A model with high FAP means the likelihood of an anomaly flagged by AD service to be a false alarm is high. If this is not desired, depending on the sensitivity requirements of a user, user can specify it to be low.

Typically, FAP can be set to be around the same level of percentage of anomalies in real business scenarios, and a value 0.01 or 1% is relatively appropriate for many scenarios. Also, be aware that if specifying a lower target FAP, the model needs more time to train, and may not achieve to the target FAP.

###How to calculate FAP

![](../images/fap-formula.png " ")

**FAP = sum(number of anomalies in each signal) / (number of signals * number of timestamps)**

As can be inferred from the formula, the more the number of false alarms allowed for the model to learn, the higher FAP will be.

###Train Fraction Ratio
Train Fraction Ratio specifies the ratio of the whole training data used for our algorithm to learn the pattern and train the model. The rest (1-ratio) of training data will be used for our algorithm to evaluate and report model performance (e.g., FAP). The default value 0.7 or 70% specifies the model to use 70% of the data for training, and the rest 30% is used to produce model performance.

In this demo data set, the default value for FAP and Train Fraction Ratio are appropriate, we will leave them as is.
![](../images/create_and_train_model.png " ")

Click Submit. For this demo dataset, it takes **10-15 minutes** to finish training a model.
![](../images/model_creation.png " ")

Once the model is trained successfully, it is automatically ready for detecting anomalies from new data. User can either use the cloud Console (next step) or the endpoint to send new testing data.

## Task 2: Detect Anomaly with new Data

### Upload to UI

To start the  process of anomaly detection select "Detect Anomalies" on the Model listing page.
![](../images/click-detect-anomalies.png " ")

Select a file from local filesystem or drag and drop the desired file.
![](../images/detect-anomaly-upload-data-form.png " ")

**Note: The detection data can have up to 100 timestamps, and requires at least 3 signals(excluding timestamp column) to generate any anomalies.**

Once the test file is uploaded, now click Detect button.

The detection result will return immediately, and you have the option to select the column to see related anomalies.

Use the drop wizard to select a column to see anomalies.
![](../images/select_column_drop.png " ")

Lets select temperature_3 to see where the model has detected an anomaly.

**Explanation of the Graph**

Each signal in your detection data can be selected to show a separate graph.

In the graph, horizontal axis represents the timestamp, and the vertical axis represents sensor values.

The BLACK curve is the actual data you provided, GREEN curve is the value estimated by our model.

The WHITE background means no anomaly detected, or the RED background means data in that range is detected as anomalies by the model.

You can move your mouse over the graph, the actual value & estimated value at a certain timestamp will show at the upper right corner of the graph.

You can also use the sliding bar under the graph to zoom in/out in different timestamp period.

![](../images/anomaly-result-graph.png " ")


The part of the signal where the model has determined to be an anomaly is highlighted. There is also an option to download the anomaly detection result.

Click the "Download JSON" button, it will download a file named anomalies.json, with the following content after pretty formatting.
 ```json
 [{
   "timestamp": "2019-01-07T21:19:03.000+00:00",
   "anomalies": [{
     "signalName": "temperature_3",
     "actualValue": -0.8625880297394809,
     "estimatedValue": -0.40735966098386517,
     "anomalyScore": 0.23270559637271968
   }],
   "score": 0.12367179620228679
 }, {
   "timestamp": "2019-01-07T21:20:04.000+00:00",
   "anomalies": [{
     "signalName": "temperature_3",
     "actualValue": -0.7527052658335041,
     "estimatedValue": -0.45714061275889295,
     "anomalyScore": 0.21966789093143743
   }],
   "score": 0.0989041369235408
 }, {
   "timestamp": "2019-01-07T21:21:10.000+00:00",
   "anomalies": [{
     "signalName": "temperature_3",
     "actualValue": -1.1998935176672367,
     "estimatedValue": -0.7756912038154168,
     "anomalyScore": 0.26406621620477416
   }],
   "score": 0.06643724287008367
 }, {
   "timestamp": "2019-01-07T21:22:02.000+00:00",
   "anomalies": [{
     "signalName": "temperature_3",
     "actualValue": -1.3438788332165472,
     "estimatedValue": -0.8973406381122574,
     "anomalyScore": 0.3178367245061653
   }],
   "score": 0.10060062430811696
 }, {
   "timestamp": "2019-01-07T21:23:09.000+00:00",
   "anomalies": [{
     "signalName": "temperature_3",
     "actualValue": -1.531234044477103,
     "estimatedValue": -0.7945619436412229,
     "anomalyScore": 0.5268952447085182
   }],
   "score": 0.18285700889800244
 }, {
   "timestamp": "2019-01-07T21:24:10.000+00:00",
   "anomalies": [{
     "signalName": "temperature_2",
     "actualValue": -0.9668546827677871,
     "estimatedValue": -0.9898144398935632,
     "anomalyScore": 0.13353981208433033
   }, {
     "signalName": "temperature_3",
     "actualValue": -1.6861941415631714,
     "estimatedValue": -0.8351588084445144,
     "anomalyScore": 0.6584086664068389
   }],
   "score": 0.19941364706874515
 }, {
   "timestamp": "2019-01-07T21:25:09.000+00:00",
   "anomalies": [{
     "signalName": "temperature_2",
     "actualValue": -0.5951845543726701,
     "estimatedValue": -1.1562167767228424,
     "anomalyScore": 0.2566200809168075
   }, {
     "signalName": "temperature_3",
     "actualValue": -1.9286121501292226,
     "estimatedValue": -1.0988042656257369,
     "anomalyScore": 0.6412993937354782
   }],
   "score": 0.1318281407161905
 }, {
   "timestamp": "2019-01-07T21:26:02.000+00:00",
   "anomalies": [{
     "signalName": "temperature_2",
     "actualValue": -1.1004140146576293,
     "estimatedValue": -0.8399905431509357,
     "anomalyScore": 0.20434224027323616
   }, {
     "signalName": "temperature_3",
     "actualValue": -2.171597377067204,
     "estimatedValue": -0.7686263854714259,
     "anomalyScore": 0.8666666666666667
   }],
   "score": 0.16131002973093184
 }, {
   "timestamp": "2019-01-07T21:27:02.000+00:00",
   "anomalies": [{
     "signalName": "temperature_2",
     "actualValue": -1.0437079075522782,
     "estimatedValue": -1.3931094916482583,
     "anomalyScore": 0.22559568052246254
   }, {
     "signalName": "temperature_3",
     "actualValue": -2.253762405930675,
     "estimatedValue": -1.2674366589407788,
     "anomalyScore": 0.7331619784919033
   }],
   "score": 0.16258810629677692
 }, {
   "timestamp": "2019-01-07T21:28:10.000+00:00",
   "anomalies": [{
     "signalName": "temperature_2",
     "actualValue": -0.7588250424377889,
     "estimatedValue": -1.4646242171662824,
     "anomalyScore": 0.37289835746358085
   }, {
     "signalName": "temperature_3",
     "actualValue": -2.3941492028804823,
     "estimatedValue": -1.2787368233952692,
     "anomalyScore": 0.8222222222222222
   }],
   "score": 0.1972854863645834
 }, {
   "timestamp": "2019-01-07T21:29:06.000+00:00",
   "anomalies": [{
     "signalName": "temperature_2",
     "actualValue": -0.6622950856002755,
     "estimatedValue": -1.4561090941002748,
     "anomalyScore": 0.42459661526568854
   }, {
     "signalName": "temperature_3",
     "actualValue": -2.5713350176048646,
     "estimatedValue": -1.3907125794113901,
     "anomalyScore": 0.7777777777777777
   }],
   "score": 0.16848421825823875
 }, {
   "timestamp": "2019-01-07T21:30:09.000+00:00",
   "anomalies": [{
     "signalName": "temperature_2",
     "actualValue": -2.86873032051319,
     "estimatedValue": -2.4782767417030342,
     "anomalyScore": 0.23749225035438012
   }, {
     "signalName": "temperature_3",
     "actualValue": -2.969391704072731,
     "estimatedValue": -2.2806596377911346,
     "anomalyScore": 0.40523888583837586
   }],
   "score": 0.1534819303667209
 }, {
   "timestamp": "2019-01-07T21:31:07.000+00:00",
   "anomalies": [{
     "signalName": "temperature_2",
     "actualValue": -2.9787643449781758,
     "estimatedValue": -1.1170899307184783,
     "anomalyScore": 0.7333333333333334
   }, {
     "signalName": "temperature_3",
     "actualValue": -2.8692496787296853,
     "estimatedValue": -0.9000745817440916,
     "anomalyScore": 0.7333333333333334
   }],
   "score": 0.3369268392426508
 }, {
   "timestamp": "2019-01-07T21:32:07.000+00:00",
   "anomalies": [{
     "signalName": "temperature_2",
     "actualValue": -2.9570048862871823,
     "estimatedValue": -1.3654440523945692,
     "anomalyScore": 0.6888888888888889
   }, {
     "signalName": "temperature_3",
     "actualValue": -2.6463618772188724,
     "estimatedValue": -1.1883816883039726,
     "anomalyScore": 0.6888888888888889
   }],
   "score": 0.2686851434684033
 }, {
   "timestamp": "2019-01-07T21:54:02.000+00:00",
   "anomalies": [{
     "signalName": "temperature_2",
     "actualValue": -0.1818702987807544,
     "estimatedValue": -0.4691383645427929,
     "anomalyScore": 0.16565661789020897
   }, {
     "signalName": "temperature_3",
     "actualValue": -0.1306604163645831,
     "estimatedValue": -0.3138576614295444,
     "anomalyScore": 0.14942660787873982
   }],
   "score": 0.15368220380590533
 }, {
   "timestamp": "2019-01-07T21:55:04.000+00:00",
   "anomalies": [{
     "signalName": "temperature_2",
     "actualValue": 0.1349151809026957,
     "estimatedValue": -0.6085697630370077,
     "anomalyScore": 0.39429135802181275
   }, {
     "signalName": "temperature_3",
     "actualValue": -0.24356808593710755,
     "estimatedValue": -0.5223729574244276,
     "anomalyScore": 0.2150518857603401
   }],
   "score": 0.0985249963703123
 }, {
   "timestamp": "2019-01-07T21:56:03.000+00:00",
   "anomalies": [{
     "signalName": "temperature_2",
     "actualValue": 0.16483956815126233,
     "estimatedValue": -0.32509987688322484,
     "anomalyScore": 0.2717989360265986
   }, {
     "signalName": "temperature_3",
     "actualValue": -0.23763427036555224,
     "estimatedValue": -0.2774910607215978,
     "anomalyScore": 0.17853952554160085
   }],
   "score": 0.07954747826189455
 }, {
   "timestamp": "2019-01-07T21:57:03.000+00:00",
   "anomalies": [{
     "signalName": "temperature_2",
     "actualValue": -0.09141636894896348,
     "estimatedValue": -0.41699979565020895,
     "anomalyScore": 0.21929854449743627
   }, {
     "signalName": "temperature_3",
     "actualValue": -0.3350101010434371,
     "estimatedValue": -0.2638139378814619,
     "anomalyScore": 0.18020841264061527
   }],
   "score": 0.0995334598102556
 }, {
   "timestamp": "2019-01-07T21:58:05.000+00:00",
   "anomalies": [{
     "signalName": "temperature_2",
     "actualValue": 0.05849590414812823,
     "estimatedValue": 0.5415503864712192,
     "anomalyScore": 0.2691750044410969
   }, {
     "signalName": "temperature_3",
     "actualValue": -0.11342634283328369,
     "estimatedValue": 0.6531658032084877,
     "anomalyScore": 0.45957406988592636
   }],
   "score": 0.16142905562442755
 }, {
   "timestamp": "2019-01-07T21:59:03.000+00:00",
   "anomalies": [{
     "signalName": "temperature_2",
     "actualValue": 0.047311577628485355,
     "estimatedValue": 0.36794552695756766,
     "anomalyScore": 0.21804575310810348
   }, {
     "signalName": "temperature_3",
     "actualValue": 0.009396930473847816,
     "estimatedValue": 0.48351007663274465,
     "anomalyScore": 0.2855658087584068
   }],
   "score": 0.12984418140360993
 }, {
   "timestamp": "2019-01-07T22:00:03.000+00:00",
   "anomalies": [{
     "signalName": "temperature_2",
     "actualValue": 0.07145888335246428,
     "estimatedValue": -0.3322094060091485,
     "anomalyScore": 0.2416026646344621
   }, {
     "signalName": "temperature_3",
     "actualValue": 0.14430348115098618,
     "estimatedValue": -0.18709759915017965,
     "anomalyScore": 0.23044184337101734
   }],
   "score": 0.12591767911574275
 }, {
   "timestamp": "2019-01-07T22:01:03.000+00:00",
   "anomalies": [{
     "signalName": "temperature_2",
     "actualValue": 3.029309810148419,
     "estimatedValue": 0.6060950893421414,
     "anomalyScore": 0.7333333333333334
   }, {
     "signalName": "temperature_3",
     "actualValue": 2.9807631561178547,
     "estimatedValue": 0.7319274991769643,
     "anomalyScore": 0.7333333333333334
   }],
   "score": 0.3002776483772831
 }, {
   "timestamp": "2019-01-07T22:02:04.000+00:00",
   "anomalies": [{
     "signalName": "temperature_2",
     "actualValue": 3.038691195904264,
     "estimatedValue": 1.153255118155411,
     "anomalyScore": 0.6888888888888889
   }, {
     "signalName": "temperature_3",
     "actualValue": 3.049010279530258,
     "estimatedValue": 1.3548717653499411,
     "anomalyScore": 0.6888888888888889
   }],
   "score": 0.2879873048348054
 }, {
   "timestamp": "2019-01-07T22:04:03.000+00:00",
   "anomalies": [{
     "signalName": "pressure_2",
     "actualValue": 1.6334379720706242,
     "estimatedValue": 0.5014895636574634,
     "anomalyScore": 0.19418185907506935
   }],
   "score": 0.26668738359881805
 }, {
   "timestamp": "2019-01-07T22:05:07.000+00:00",
   "anomalies": [{
     "signalName": "pressure_2",
     "actualValue": 1.4661385443962462,
     "estimatedValue": -0.5285874553724194,
     "anomalyScore": 0.36673491081243204
   }],
   "score": 0.19586214096125326
 }, {
   "timestamp": "2019-01-07T22:06:05.000+00:00",
   "anomalies": [{
     "signalName": "pressure_2",
     "actualValue": 0.0490478171262037,
     "estimatedValue": -1.166326398502374,
     "anomalyScore": 0.29237047060718846
   }],
   "score": 0.15748733995024758
 }, {
   "timestamp": "2019-01-07T22:07:06.000+00:00",
   "anomalies": [{
     "signalName": "pressure_2",
     "actualValue": -3.1899739406153196,
     "estimatedValue": -2.3477034397664784,
     "anomalyScore": 0.2559121418673264
   }],
   "score": 0.0992931513091865
 }, {
   "timestamp": "2019-01-07T22:08:08.000+00:00",
   "anomalies": [{
     "signalName": "pressure_2",
     "actualValue": -0.7961303437489068,
     "estimatedValue": -0.7656199601912739,
     "anomalyScore": 0.22226642933269267
   }],
   "score": 0.08414277993336367
 }, {
   "timestamp": "2019-01-07T22:09:10.000+00:00",
   "anomalies": [{
     "signalName": "pressure_2",
     "actualValue": 0.6997339833791824,
     "estimatedValue": -1.0094694332479333,
     "anomalyScore": 0.36095666644352914
   }],
   "score": 0.10353491354542377
 }, {
   "timestamp": "2019-01-07T22:10:05.000+00:00",
   "anomalies": [{
     "signalName": "pressure_2",
     "actualValue": -0.8644751237229334,
     "estimatedValue": -0.847996814142579,
     "anomalyScore": 0.22223511724488176
   }],
   "score": 0.06724612650883213
 }, {
   "timestamp": "2019-01-07T22:11:03.000+00:00",
   "anomalies": [{
     "signalName": "pressure_2",
     "actualValue": 9.637427929543756,
     "estimatedValue": 2.688328414425639,
     "anomalyScore": 0.7777777777777777
   }],
   "score": 0.128728712934623
 }, {
   "timestamp": "2019-01-07T22:12:02.000+00:00",
   "anomalies": [{
     "signalName": "pressure_2",
     "actualValue": 8.636504808483837,
     "estimatedValue": 2.7912052622701293,
     "anomalyScore": 0.7333333333333334
   }],
   "score": 0.13708244044130122
 }, {
   "timestamp": "2019-01-07T22:13:05.000+00:00",
   "anomalies": [{
     "signalName": "pressure_2",
     "actualValue": 7.592321707893466,
     "estimatedValue": 3.2019284312239957,
     "anomalyScore": 0.6888888888888889
   }],
   "score": 0.2185953801885069
 }]
 ```

The results return an array of anomalies grouped by timestamp. Each timestamp could have anomalies generated by single or multiple signals. Anomaly generated by one signal contains a tuple of signal name, actual value, estimate value, and an anomaly score with in the range of 0 to 1 that indicate the significance of anomaly. Meanwhile, each timestamp also have a normalized score that combines the significance scores across single or multiple alerted signals.

Notice that sometimes the estimated value and actual value have small difference for an signal, but it is still detected as anomalous. This is due to our algorithm using a future-observing consolidation strategy to consider raw anomalies being detected in the next few timestamps.

**Congratulations on completing this lab!**

You now have completed the full cycle of using the training data to create a model and deploy, and also making predictions with testing data.

The next 2 sessions are optional for advanced users, which cover the topic on using REST API to integrate our services and how to prepare the training and testing data from raw data in different scenarios.

[Proceed to the next section](#next).

## Acknowledgements

* **Authors**
    * Jason Ding - Principal Data Scientist - Oracle AI Services
    * Haad Khan - Senior Data Scientist - Oracle AI Services
* **Last Updated By/Date**
    * Jason Ding - Senior Data Scientist, July 2021
