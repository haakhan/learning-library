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
CONFIG_FILENAME = "/home/<USERNAME>/.oci/config" # TODO: Update USERNAME
SERVICE_ENDPOINT="https://anomalydetection.aiservice.us-ashburn-1.oci.oraclecloud.com" # Need to Update propery if different
NAMESPACE = "idehhejtnbtc" # Need to Update propery if different
BUCKET_NAME = "anomaly-detection-bucket" # Need to Update propery if different
training_file_name="demo-training-data.csv" # Need to Update propery if different

compartment_id = "ocid1.tenancy.oc1..aaaaaaaasuvbdyacvuwg7p5zdccy564al2bnlizwdabjoebpefmvksqve3na" #Compartment of the project, Need to Update propery if different
config = from_file(CONFIG_FILENAME)

ad_client = AnomalyDetectionClient(
    config,
    service_endpoint=SERVICE_ENDPOINT)  # /20210101

# PROJECT
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

# LIST CALL
list_proj = ad_client.list_projects(compartment_id=compartment_id)
print("----LISTING----")
print(list_proj.data)
time.sleep(5)


# DATA ASSET
print("-*-*-*-DATA ASSET-*-*-*-")
# CREATE CALL
dDetails = DataSourceDetails(data_source_type="ORACLE_OBJECT_STORAGE")

dObjDeatils = DataSourceDetailsObjectStorage(
    namespace=NAMESPACE,
    bucket_name=BUCKET_NAME,
    object_name=training_file_name,
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
da_id = create_res.data.id

# READ CALL
get_da = ad_client.get_data_asset(data_asset_id=da_id)
print("----READING----")
print(get_da.data)

# LIST CALL
list_da = ad_client.list_data_assets(
    compartment_id=compartment_id, project_id=project_id
)
print("----LISTING----")
print(list_da.data)
time.sleep(5)

# MODEL
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
model_id = create_res.data.id

# READ CALL
get_model = ad_client.get_model(model_id=model_id)
print("----READING----")
print(get_model.data)
time.sleep(10)
while get_model.data.lifecycle_state == Model.LIFECYCLE_STATE_CREATING:
    get_model = ad_client.get_model(model_id=model_id)
    time.sleep(60)
    print(get_model.data.lifecycle_state)
print(get_model.data)

# LIST CALL
list_model = ad_client.list_models(compartment_id=compartment_id, project_id=project_id)
print("----LISTING----")
print(list_model.data)
time.sleep(10)


# DETECT
print("-*-*-*-DETECT-*-*-*-")
signalNames = ["temperature_1", "temperature_2", "temperature_3", "temperature_4", "temperature_5", "pressure_1", "pressure_2", "pressure_3", "pressure_4", "pressure_5"]

payloadData = []
for i in range(10):
    timestamp = datetime.strptime(f"2020-07-13T20:4{i}:46Z", "%Y-%m-%dT%H:%M:%SZ")
    values = [ 3*i, 0.04713*(i-2)**2, 1.0, 0.5479, 1.291, 0.8059, 1.393, 0.0293, 0.1541, 0.2611]
    dItem = DataItem(timestamp=timestamp, values=values)
    payloadData.append(dItem)

inline = InlineDetectAnomaliesRequest( model_id=model_id, request_type="INLINE", signal_names=signalNames, data=payloadData)

detect_res = ad_client.detect_anomalies(detect_anomalies_details=inline)
print("----DETECTING----")
print(detect_res.data)


# DELETE MODEL
delete_model = ad_client.delete_model(model_id=model_id)
print("----DELETING MODEL----")
print(delete_model.data)
time.sleep(60)

# DELETE DATA ASSET
delete_da = ad_client.delete_data_asset(data_asset_id=da_id)
print("----DELETING DATA ASSET----")
print(delete_da.data)
time.sleep(10)

# DELETE PROJECT
print("----DELETING PROJECT----")
delete_project = ad_client.delete_project(project_id=project_id)
print(delete_project.data)
