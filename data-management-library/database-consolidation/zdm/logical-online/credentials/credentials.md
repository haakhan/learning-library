# Token Authentication, Credentials and Object Storage Configuration

## Introduction
In this lab, you will be:
  * Creating an authentication token for your Oracle Cloud Infrastructure (OCI) user profile.
  * Creating an object storage bucket.
  * Logging into your migration target autonomous database and creating the credential file you will need to connect to your OCI user.
  * Creating movedata\_user in the autonomous database.

Estimate Lab Time: 15 minutes

## **Task 1: Create Authentication Token**
1. Go to your OCI profile by selecting the icon in the top right and clicking user.
    ![Dashboard Profile](./images/dashboard-profile.png)

2. Under Resources in the bottom left select Auth Tokens and click generate token.
    ![Authentication Token](./images/auth-token.png)

3. Set a description and click generate token and make sure to write down the token displayed as you cannot get access to it again. If you lose the token you will need to generate a new one.
    ![Token Description](./images/token-desc.png)

## **Task 2: Create an Object Storage Bucket**

1. You will need an object storage bucket for your data during the migration as an intermediary point before being transferred to your target autonomous database. In your OCI Dashboard: select the hamburger menu, Storage -> Buckets.
    ![Bucket Path](./images/bucket-path.png)

2. Select 'Create Bucket'.
    ![Create Bucket](./images/create-bucket.png)

3. Fill in the details. We will be using the name ZDMBucket. Make sure Default Storage Tier is 'Standard' and Encryption is 'Encrypt using Oracle managed keys'. Other than these 3 fields, leave the rest blank and click 'Create'.
    ![Bucket Form](./images/bucket-form.png)

4. On the Details page the two most important pieces of information for us are the bucket name and namespace which we will need later.
    ![Bucket Page](./images/bucket-page.png)

## **Task 3: Log Into SQL on the Autonomous Database**

1. In your OCI Dashboard: select the hamburger menu, Oracle Database -> Autonomous Database.
    ![Autonomous Menu](./images/menu-auton.png)

2. Select the target database.
    ![Select Autonomous](./images/select-auton.png)

3. In the database menu go to __Tools__ -> __Open Database Actions__.
    ![Database Action](./images/db-action.png)

4. A new tab will open requesting for credentials. Fill in ADMIN for the username and the password will be `WELcome##1234` unless you set it as something different.

5. Select SQL
    ![Select SQL](./images/select-sql.png)


## **Task 4: Run Credential Script**
1. In the script below replace `<oci_user>`, `<oci_tenancy>`, `<api_private_key>`, and `<fingerprint>` with their respective information and paste it into SQL.

    `<oci_user>`, `<oci_tenancy>`, and `<fingerprint>` are in the Configuration File Preview under API Keys in your OCI user profile from the previous labs.

    ![Viewing Configuration File Preview](./images/view-config-prev.png)

    ![Configuration Preview](./images/config-prev.png)

    `<api_private_key>` is your API private key from the Host Environment lab. To view it again, in CloudShell type the following as 'zdmuser':

    ```
    <copy>
    cd /u01/app/zdmhome/.oci
    cat oci_api_key.pem
    </copy>
    ```

    SQL Script. When pasting the API private key only paste the contents, don't include "Begin RSA Private Key" and "End RSA Private Key"

    ```
    <copy>
    begin
    DBMS_CLOUD.CREATE_CREDENTIAL (
    'CredentialZDM',
    '<oci_user>',
    '<oci_tenancy>',
    '<api_private_key>',
    '<fingerprint>');
    end;
    /
    </copy>
    ```

2. Select 'Run Script'.
    ![Credential Script](./images/cred-script.png)

## **Task 5: Unlock GG User**

1. Delete the existing script by clicking on the __Trash Can__ icon.
    ![Credential Script](./images/delete-script.png)

2. Paste the following script. When executed, this script will unlock the pre-created ggadmin user from the Target Autonomous Database.

    ```
    <copy>
    alter user ggadmin identified by WELcome##1234 account unlock;
    </copy>
    ```
    ![Credential Script](./images/copy-unlock-script.png)

3. Run the script by clicking on the __Run Script__ icon.
    ![Credential Script](./images/run-unlock-script.png)

## Acknowledgements
* **Author** - Zachary Talke, Solutions Engineer, NA Tech Solution Engineering
- **Contributors** - Ricardo Gonzalez, Senior Principal Product Manager, Oracle Cloud Database Migration
* **Contributors** - LiveLabs Team, ZDM Development Team
* **Last Updated By/Date** - Ricardo Gonzalez, August 2021
