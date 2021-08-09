# Lab 4: (Advanced Session) Access Anomaly Detection Service with REST API

## Introduction

Our anomaly detection services also support to use CLI tool `oci` or REST API calls to perform model and data operations.

In this lab session, we will show several code snippets to integrate with our service endpoints.

You do not need to execute those codes, but review them to understand what information and steps are needed to implement your own integration.

*Estimated Lab Time*: 45 minutes

### Objectives:

* Learn how to use REST API to communicate with our anomaly detection service endpoints.

### Prerequisites:
* Familiar with Python programming is required
* Have a Python environment ready in local or use our [Data Science Platform](https://www.oracle.com/data-science/)
* Familiar with local editing tools, such as vi and nano, or editing IDEs, such as VS Code or Sublime
* Install/Update to the most updated version of Python library `oci` (version 2.42.0 or higher)

## REST API Endpoints

Our service supports CRUD (Create, Read, Update, Delete) actions on the four different resource types involved, including Project, Data Asset, and Model.

The following are a few examples of accessing those API endpoints using Python. The complete code file can be [downloaded here](../files/anomaly_detection_rest_api_example.py).


### **STEP 1:** Configuration and Connection

This code snippet showed you how to perform configuration and set up connection before other operations.

```Python
import oci
import time
import json
from datetime import datetime

from oci.config import from_file
from oci.ai_anomaly_detection.models import *
from oci.ai_anomaly_detection.anomaly_detection_client import AnomalyDetectionClient

from oci.ai_anomaly_detection.models.create_project_details import CreateProjectDetails
from oci.ai_anomaly_detection.models.create_data_asset_details import CreateDataAssetDetails
from oci.ai_anomaly_detection.models.data_source_details import DataSourceDetails
from oci.ai_anomaly_detection.models.data_source_details_object_storage import DataSourceDetailsObjectStorage

from oci.ai_anomaly_detection.models.create_model_details import CreateModelDetails
from oci.ai_anomaly_detection.models.model_training_details import ModelTrainingDetails

from oci.ai_anomaly_detection.models.data_item import DataItem
from oci.ai_anomaly_detection.models.inline_detect_anomalies_request import InlineDetectAnomaliesRequest

# change the following constants accordingly
# ## If using the instance in data science platform, please refer this page https://dzone.com/articles/quick-and-easy-configuration-of-oracle-data-scienc to setup the content of config file
CONFIG_FILENAME = "/Users/home/.oci/config"
SERVICE_ENDPOINT="https://anomalydetection.aiservice.us-phoenix-1.oci.oraclecloud.com"
NAMESPACE = "id5zdxxxxa"
BUCKET_NAME = "my-bucket"

compartment_id = "ocid1.compartment.oc1..<Compartment ID>" #Compartment of the project
config = from_file(CONFIG_FILENAME)

ad_client = AnomalyDetectionClient(
    config,
    service_endpoint=SERVICE_ENDPOINT)  # /20210101
```

### **STEP 2:** Creating a Project

```Python
print("-*-*-*-PROJECT-*-*-*-")

# CREATE CALL
proj_details = CreateProjectDetails(
    display_name="Test Project",
    description="Test Project description",
    compartment_id=compartment_id,
)
create_res = ad_client.create_project(create_project_details=proj_details)
print("----CREATING----")
print(create_res.data)
time.sleep(5)
project_id = create_res.data.id

# GET CALL
get_proj = ad_client.get_project(project_id=project_id)
print("----READING---")
print(get_proj.data)
time.sleep(5)

```

### **STEP 3:** Creating the DataAsset

```Python
print("-*-*-*-DATA ASSET-*-*-*-")
# CREATE CALL
dDetails = DataSourceDetails(data_source_type="ORACLE_OBJECT_STORAGE")

dObjDeatils = DataSourceDetailsObjectStorage(
    namespace=NAMESPACE,
    bucket_name=BUCKET_NAME,
    object_name="training_ata.json",
)

da_details = CreateDataAssetDetails(
    display_name="Test DataAsset",
    description="description DataAsset",
    compartment_id=compartment_id,
    project_id=project_id,
    data_source_details=dObjDeatils,
)
create_res = ad_client.create_data_asset(create_data_asset_details=da_details)
print("----CREATING----")
print(create_res.data)
time.sleep(5)
da_id = create_res.data.id

# READ CALL
get_da = ad_client.get_data_asset(data_asset_id=da_id)
print("----READING----")
print(get_da.data)
time.sleep(5)
```

### **STEP 4:** Creating the Train Model
```Python
print("-*-*-*-MODEL-*-*-*-")
# CREATE CALL
dataAssetIds = [da_id]
mTrainDetails = ModelTrainingDetails(
    target_fap=0.02, training_fraction=0.7, data_asset_ids=dataAssetIds
)
mDetails = CreateModelDetails(
    display_name="DisplayNameModel",
    description="description Model",
    compartment_id=compartment_id,
    project_id=project_id,
    model_training_details=mTrainDetails,
)

create_res = ad_client.create_model(create_model_details=mDetails)
print("----CREATING----")
print(create_res.data)
time.sleep(60)
model_id = create_res.data.id

# READ CALL
get_model = ad_client.get_model(model_id=model_id)
print("----READING----")
print(get_model.data)
time.sleep(60)
while get_model.data.lifecycle_state == Model.LIFECYCLE_STATE_CREATING:
    get_model = ad_client.get_model(model_id=model_id)
    time.sleep(60)
    print(get_model.data.lifecycle_state)

```

### **STEP 5:** Detection with the Model
```Python
print("-*-*-*-DETECT-*-*-*-")
signalNames = [
    "sensor1",
    "sensor2",
    "sensor3",
    "sensor4",
    "sensor5",
    "sensor6",
    "sensor7",
    "sensor8",
    "sensor9",
    "sensor10",
    "sensor11",
]
timestamp = datetime.strptime("2020-07-13T20:44:46Z", "%Y-%m-%dT%H:%M:%SZ")
values = [
    1.0,
    0.4713,
    1.0,
    0.5479,
    1.291,
    0.8059,
    1.393,
    0.0293,
    0.1541,
    0.2611,
    0.4098,
]
dItem = DataItem(timestamp=timestamp, values=values)
inlineData = [dItem] #multiple items can be added here
inline = InlineDetectAnomaliesRequest(
    model_id=model_id, request_type="INLINE", signal_names=signalNames, data=inlineData
)

detect_res = ad_client.detect_anomalies(detect_anomalies_details=inline)
print("----DETECTING----")
print(detect_res.data)
```

Congratulations on completing this lab!

[Proceed to the next section](#next).

## Acknowledgements
* **Authors**
    * Jason Ding - Principal Data Scientist - Oracle AI Services
    * Haad Khan - Senior Data Scientist - Oracle AI Services
* **Last Updated By/Date**
    * Jason Ding - Principal Data Scientist, July 2021
