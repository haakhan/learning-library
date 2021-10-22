# SODA in Oracle Autonomous JSON Database (AJD) using Python

## Introduction

Oracle Autonomous JSON Database (AJD) is a new service in Autonomous Database family for JSON-centric development. Autonomous JSON Database is built for developers who are looking for an easy to use, cost-effective JSON database with native Document API support. Autonomous JSON Database provides all the core capabilities of a document store along with high performance, simple elasticity, full ACID support and complete SQL functionality. Autonomous JSON Database is available only on Shared Infrastructure. Also, customers can one-click upgrade from Autonomous JSON Database (AJD) to full featured Autonomous Transaction Processing Database (ATP) any time.

Estimated Lab Time: 60 minutes

### Objectives
In this lab, you will:
* Create Python application
* Use SODA for Python with Oracle Autonomous JSON Database
* Insert JSON documents in MongoDB and AJD using REST calls
* Retrieve JSON documents from MongoDB and AJD
* Migrate JSON documents from MongoDB to AJD

### Prerequisites
* OCI resources (Introduction)
* MongoDB Cloud Atlas (Introduction)

## Task 1: Create Python application for MongoDB document store

1. Connect to **[Your Initials]-ClientVM** Compute instance using SSH, if not connected, as user **opc**.
    * For **Mac/Linux**: Use -L option to forward any connection to port **3389** on the local machine to port **3389** on your Compute node. Open a Microsoft Remote Desktop connection to **localhost**.
    * For **Windows**: Create a SSH tunnel from source port **5001** to **localhost:3389**. Open a Microsoft Remote Desktop connection to **localhost:5001**.

2. Use the substitute user command to start a session as **oracle** user. 

    ````
    sudo su - oracle
    ````

    >**Note** : This step is not required if you prefer to use the Remote Desktop connection for this lab.

3. Create a new folder under `/home/oracle` as the location of our new Python application.

    ````
    mkdir python-simple-project

    cd python-simple-project
    ````

4. Create two files for our new Python application.

    ````
    touch simple-app.py

    touch requirements.pip
    ````

5. Create a Python virtual environment for development, and activate it.

    ````
    pip3 install --user virtualenv

    virtualenv .

    . bin/activate
    ````

6. Use a text editor, **vim** on command line or **gEdit** on Remote Desktop, to add the following lines in requirements.pip:

    ````
    Flask
    pymongo
    dnspython
    ````

7. Start developing the document store application. Here are the main sections, just look at the code, do not copy or execute anything now. The first section imports the required modules for the application.

    ````
    import os
    import json
    import pymongo
    from flask import Flask
    from flask import request
    app = Flask(__name__)
    ````

8. Using **os** module we can retrieve the connection details for MongoDB from the operating system environment variables.

    ````
    usr = os.environ['MONGO_DB_USER']
    pwd = os.environ['MONGO_DB_PASS']
    dbn = os.environ['MONGO_DB_NAME']
    ````

9. This section builds the connection string, defines the connection, and the collection used by the application. Use the information from Introduction STEP 5.6 to build your MongoDB connection string.

    ````
    client = pymongo.MongoClient("mongodb+srv://" + usr + ":" + pwd + "@cluster_name.dsbwl.mongodb.net/" + dbn + "?retryWrites=true&w=majority")
    db = client[dbn]
    collection = db['SimpleCollection']
    ````

10. Use the `route()` decorator to tell Flask what URL should trigger our function called `insert_mongo_doc` that is used to insert new JSON documents in the document store.

    ````
    @app.route("/", methods=['POST'])
    def insert_mongo_doc():
        req_data = request.get_json()
        collection.insert_one(req_data).inserted_id
        return ('', 204)
    ````

11. Define another function called `get_mongo_doc` to retrieve JSON documents from the MongoDB document store.

    ````
    @app.route('/')
    def get_mongo_doc():
        documents = collection.find()
        response = []
        for document in documents:
            document['_id'] = str(document['_id'])
            response.append(document)
        return json.dumps(response)
    ````

12. When Python interpreter reads our source file, it defines a special variable called `__name__`. This is the main program module, so it will see that `__name__` variable is set to `'__main__'` value, and it calls the `app.run()` method to run our Flask application.

    ````
    if __name__ == '__main__':
        app.run(host= '0.0.0.0')
    ````

13. Putting together all these sections, here is the code we have to write in our simple-app.py application file:

    ````
    import os
    import json
    import pymongo
    from flask import Flask
    from flask import request
    app = Flask(__name__)

    usr = os.environ['MONGO_DB_USER']
    pwd = os.environ['MONGO_DB_PASS']
    dbn = os.environ['MONGO_DB_NAME']

    client = pymongo.MongoClient("mongodb+srv://" + usr + ":" + pwd + "@cluster0.dsbwl.mongodb.net/" + dbn + "?retryWrites=true&w=majority")
    db = client[dbn]
    collection = db['SimpleCollection']

    @app.route("/", methods=['POST'])
    def insert_mongo_doc():
        req_data = request.get_json()
        collection.insert_one(req_data).inserted_id
        return ('', 204)

    @app.route('/')
    def get_mongo_doc():
        documents = collection.find()
        response = []
        for document in documents:
            document['_id'] = str(document['_id'])
            response.append(document)
        return json.dumps(response)

    if __name__ == '__main__':
        app.run(host= '0.0.0.0')
    ````

## Task 2: Run the Python application and check results

1. Export operating system required environment variables.

    ````
    export MONGO_DB_USER=mongoUser

    export MONGO_DB_PASS=DBlearnPTS#21_

    export MONGO_DB_NAME=SimpleDatabase
    ````

2. Use **pip** package installer for Python to install the required packages we specified in requirements.pip file.

    ````
    pip3 install -r requirements.pip
    ````

3. Run the application.

    ````
    python3.6 simple-app.py
    ````

4. If you followed the steps correctly, you should see this output in the terminal:

    ````
    * Serving Flask app "simple-app" (lazy loading)
    * Environment: production
      WARNING: This is a development server. Do not use it in a production deployment.
      Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
    ````

5. It means your Python Flask application is running, and the base URL is `http://0.0.0.0:5000/`. With the proper Security List and Linux firewall configuration, there are two ways of accessing this URL:

    * From the same ClientVM using `http://localhost:5000/`;
    * From any other computer using `http://[ClientVM Public IP Address]:5000/`.

6. At this point, there are no documents in your collection, and you will receive an empty list if you try to connect to your Flask application.

    ````
    []
    ````

7. Insert a JSON document in your MongoDB document store, from the ClientVM. You will need to open a new Terminal window, or another SSH connection, because the first one is locked until you stop the application with CTRL+C, as specified. However, you cannot stop the application now because you are communicating with it via REST calls.

    ````
    curl --request POST \
      --url http://localhost:5000/ \
      --header 'content-type: application/json' \
      --data '{
     "company":"Company One",
     "address": {
         "street": "22 Rue du Grenier Saint-Lazare",
         "city": "Paris",
         "country": "France"
     },
     "industry":"Financial Services",
     "employees":54234
    }'
    ````

8. Refresh the browser that you used to open your Python Flask application. You should see this first document in your collection.

9. Insert another JSON document. If you want to insert JSON documents from your laptop (or another Linux computer with Internet access and a CURL client), you have to use the ClientVM Public IP Address in the URL.

    ````
    curl --request POST \
      --url http://[ClientVM Public IP Address]:5000/ \
      --header 'content-type: application/json' \
      --data '{
     "company":"Company Two",
     "address": {
         "street": "Calle Extramuros 74",
         "city": "Madrid",
         "country": "Spain"
     },
     "industry":"Retail",
     "employees":12345
    }'
    ````

10. Use your laptop web browser to access `http://[ClientVM Public IP Address]:5000/` and verify both documents have been inserted. 

11. Verify also on MongoDB Cloud interface, in your Cluster, user **Collections**. 

12. Press CTRL+C in the terminal where the application is running, to stop it.


## Task 3: Improve Python application adding Oracle AJD document store

Wallet files, along with the database user ID and password, provide access to data in your Autonomous Database. Store wallet files in a secure location. Share wallet files only with authorized users.

The client credentials Wallet_AJD-NAME.zip that you download contains the following files:

* cwallet.sso - Oracle auto-login wallet
* ewallet.p12 - PKCS #12 wallet file associated with the auto-login wallet
* sqlnet.ora - SQL*Net profile configuration file that includes the wallet location and TNSNAMES naming method
* tnsnames.ora - SQL*Net configuration file that contains network service names mapped to connect descriptors for the local naming method
* Java Key Store (JKS) files - Key store files for use with JDBC Thin Connections

1. Open  your Oracle Cloud Login URL using the Firefox browser on the ClientVM and navigate to Oracle Database > Autonomous Database. Click on your AJD instance, **DB Connection**, and download Instance Wallet using **Download Wallet** button.

2. Provide a password (use the same as for RD connection - DBlearnPTS#21_), and Save File.

3. If you use the Firefox browser on the Remote Desktop connection, it will be downloaded in folder `/home/oracle/Downloads/`. Create a new folder to place wallet files.

    ````
    ls /home/oracle/Downloads/
    
    mkdir /home/oracle/Wallet_[Your Initials]AJD

    unzip /home/oracle/Downloads/Wallet_[Your Initials]AJD.zip -d /home/oracle/Wallet_[Your Initials]AJD/
    ````

4. Edit **sqlnet.ora** file in **Wallet_[Your Initials]AJD** folder, and set the value of `DIRECTORY` to `${TNS_ADMIN}`.

    ````
    WALLET_LOCATION = (SOURCE = (METHOD = file) (METHOD_DATA = (DIRECTORY="${TNS_ADMIN}")))
    SSL_SERVER_DN_MATCH=yes
    ````

5. Set the TNS_ADMIN environment variable to the directory where the unzipped credentials files.

    ````
    export TNS_ADMIN=/home/oracle/Wallet_[Your Initials]AJD
    ````

6. Add another line to **requirements.pip** file. **cx_Oracle** is a Python extension module that enables access to Oracle Database.

    ````
    cx_Oracle
    ````

7. Install the packages listed in requirements.pip file. If some are already installed, **pip** package installer will skip them.

    ````
    pip3 install -r requirements.pip
    ````

8. Get AJD service names for your instance from **tnsnames.ora** file.

    ````
    cat /home/oracle/Wallet_[Your Initials]AJD/tnsnames.ora
    ````

9. Verify the connectivity using SQL*Plus, using the TP service. If the connection works, exit.

    ````
    sqlplus demo/DBlearnPTS#21_@[ajd-name]_tp

    exit
    ````

10. Edit **simple-app.py** file, add the lines needed by this simple Python application to connect to Oracle AJD document store, and perform the same tasks it performed on MongoDB. 
    * In the header section we need to import cx_Oracle module. 
    * Second, it will retrieve the connection details for Oracle AJD from the operating system environment variables. 
    * Then it builds the connection string, defines the connection, and the collection used by the application, for Oracle AJD. Both MongoDB collection and Oracle AJD collection have the same name, **SimpleCollection**. 
    * Next code is added to define the two functions used to insert new JSON documents, and to retrieve JSON documents from the AJD document store. 
    * Notice the small change in the URL used, `base-URL/m/` for MongoDB and `base-URL/o/` for Oracle AJD. 

11. With all these changes, your **simple-app.py** now has the following contents:

    ````
    # imports the required modules
    import os
    import json
    import pymongo
    import cx_Oracle
    from flask import Flask
    from flask import request
    app = Flask(__name__)

    # retrieve MongoDB connection info from os environment variables
    m_usr = os.environ['MONGO_DB_USER']
    m_pwd = os.environ['MONGO_DB_PASS']
    m_dbn = os.environ['MONGO_DB_NAME']

    # retrieve Oracle connection info from os environment variables
    o_usr = os.environ['ORCL_DB_USER']
    o_pwd = os.environ['ORCL_DB_PASS']
    o_srv = os.environ['ORCL_DB_SERV']

    # create MongoDB connection, and set collection used by application
    client = pymongo.MongoClient("mongodb+srv://" + m_usr + ":" + m_pwd + "@cluster0.dsbwl.mongodb.net/" + m_dbn + "?retryWrites=true&w=majority")
    mdb = client[m_dbn]
    mcollection = mdb['SimpleCollection']

    # create Oracle connection, and set collection used by application
    conn_string = o_usr + '/' + o_pwd + '@' + o_srv
    connection = cx_Oracle.connect(conn_string)
    connection.autocommit = True
    soda = connection.getSodaDatabase()
    ocollection = soda.createCollection("SimpleCollection")

    # function used to insert JSON documents in MongoDB
    @app.route("/m/", methods=['POST'])
    def insert_mongo_doc():
        req_data = request.get_json()
        mcollection.insert_one(req_data).inserted_id
        return ('', 204)

    # function used to retrieve JSON documents from MongoDB
    @app.route('/m/')
    def get_mongo_doc():
        documents = mcollection.find()
        response = []
        for document in documents:
            document['_id'] = str(document['_id'])
            response.append(document)
        return json.dumps(response)

    # function used to insert JSON documents in Oracle
    @app.route("/o/", methods=['POST'])
    def insert_orcl_doc():
        req_data = request.get_json()
        ocollection.insertOne(req_data)
        return ('', 204)

    # function used to retrieve JSON documents from Oracle
    @app.route('/o/')
    def get_orcl_doc():
        documents = ocollection.find().getDocuments()
        response = []
        for document in documents:
            content = document.getContent()
            content['key'] = str(document.key)
            response.append(content)
        return json.dumps(response)

    # main program module
    if __name__ == '__main__':
        app.run(host= '0.0.0.0')
    ````

    >**Note** : Simple Oracle Document Access (SODA) is a set of NoSQL-style APIs that let you use collections of JSON documents in Autonomous Database, and deliver the experience of a NoSQL document-store with the Oracle RDBMS, offering the same development experience as pure-play document stores.

12. Create a bash script called **variables.sh**, and add the following lines. 
    * Specify the correct name of your AJD wallet folder. 
    * Replace `[ajd-name]_tp` with the name of your AJD instance service in lowercase, that you retrieved from **tnsnames.ora** file.

    ````
    #!/bin/bash
    export MONGO_DB_PASS=DBlearnPTS#21_
    export MONGO_DB_USER=mongoUser
    export MONGO_DB_NAME=SimpleDatabase
    export TNS_ADMIN=/home/oracle/Wallet_[Your Initials]AJD
    export ORCL_DB_USER=demo
    export ORCL_DB_PASS=DBlearnPTS#21_
    export ORCL_DB_SERV=[ajd-name]_tp
    ````

13. Make this script executable.

    ````
    chmod a+x variables.sh
    ````


## Task 4: Run the application with MongoDB and Oracle AJD support

1. Run the script, with the dot and the space in front of it, to set the necessary values for all environment variables, required for our application.

    ````
    . variables.sh
    ````

2. Run the application.

    ````
    python3.6 simple-app.py
    ````

3. Insert a JSON document into MongoDB, from a Linux computer with Internet access and CURL, any REST client you may have on your computer, or the ClientVM compute node.

    ````
    curl --request POST \
      --url http://[ClientVM Public IP Address]:5000/m/ \
      --header 'content-type: application/json' \
      --data '{
     "company":"Company Three",
     "address": {
         "street": "3A Evergreen St, Ballyphehane",
         "city": "Cork",
         "country": "Ireland"
     },
     "industry":"Manufacturing",
     "employees":98765
    }'
    ````

4. Insert another JSON document into MongoDB.

    ````
    curl --request POST \
      --url http://[ClientVM Public IP Address]:5000/m/ \
      --header 'content-type: application/json' \
      --data '{
     "company":"Company Four",
     "address": {
         "street": "aleje Mikołaja Kopernika 32",
         "city": "Piotrków Trybunalski",
         "country": "Poland"
     },
     "industry":"Manufacturing",
     "employees":44444
    }'
    ````

5. Insert a JSON document into Oracle AJD, from a Linux computer with Internet access and CURL, any REST client you may have on your computer, or the ClientVM compute node.

    ````
    curl --request POST \
      --url http://[ClientVM Public IP Address]:5000/o/ \
      --header 'content-type: application/json' \
      --data '{
     "company":"Company Five",
     "address": {
         "street": "6435 Avondale Dr",
         "city": "Nichols Hills",
         "country": "United States"
     },
     "industry":"Retail",
     "employees":5550
    }'
    ````

6. Insert another JSON document into Oracle AJD.

    ````
    curl --request POST \
      --url http://[ClientVM Public IP Address]:5000/o/ \
      --header 'content-type: application/json' \
      --data '{
     "company":"Company Six",
     "address": {
         "street": "15 1 Ave W",
         "city": "Lafleche",
         "country": "Canada"
     },
     "industry":"Health Sciences",
     "employees":123123
    }'
    ````

7. Insert two more JSON documents into Oracle AJD, just to have 4 documents in each document store.

    ````
    curl --request POST \
      --url http://[ClientVM Public IP Address]:5000/o/ \
      --header 'content-type: application/json' \
      --data '{
     "company":"Company Seven",
     "address": {
         "street": "Calle Martin Corchado 32",
         "city": "Ponce",
         "country": "Puerto Rico"
     },
     "industry":"Communications",
     "employees":112233
    }'

    curl --request POST \
      --url http://[ClientVM Public IP Address]:5000/o/ \
      --header 'content-type: application/json' \
      --data '{
     "company":"Company Eight",
     "address": {
         "street": "Asa Sul CLS 203 LOJA 06 - Asa Sul",
         "city": "Brasília",
         "country": "Brazil"
     },
     "industry":"Utilities",
     "employees":888
    }'
    ````

8. Use your laptop web browser to access `http://[ClientVM Public IP Address]:5000/m/` to retrieve documents from MongoDB. You can verify also on MongoDB Cloud interface, in your Cluster, user **Collections**. Use 🔄 Refresh button if necessary.

9. Use your laptop web browser to access `http://[ClientVM Public IP Address]:5000/o/` to retrieve documents from Oracle AJD. You can verify also on Database Actions web interface, connected as **demo** user (password DBlearnPTS#21_), using Development > **JSON**. Select SimpleCollection collection, and use the ▶️ Play button to refresh data.

10. Press CTRL+C in the terminal where the application is running, to stop it.

11. Python applications can handle a document store collection with a large number of JSON documents, e.g. millions. Add pagination to the two functions used to retrieve JSON documents, `get_mongo_doc` and `get_orcl_doc`. In both cases, pagination can be implemented using `limit()` and `skip()` commands. 
    * `skip(n)` directive tells our document store to skip '**n**' results.
    * `limit(n)` directive instructs the document store to limit the result length to '**n**' results. 
    * The combination of two will naturally paginate the response.

12. For MongoDB retrieve function, replace the first line with this one (make sure you preserve the same indentation because this is very important in Python):

    ````
    documents = mcollection.find().limit(2).skip(2)
    ````

    * For Oracle AJD retrieve function, replace the first line with this one:

    ````
    documents = ocollection.find().limit(2).skip(2).getDocuments()
    ````

13. Run the application.

    ````
    python3.6 simple-app.py
    ````

14. Refresh your browser where `http://[ClientVM Public IP Address]:5000/m/` and `http://[ClientVM Public IP Address]:5000/o/` are open, to see the changes. Now it shows only the last 2 documents from each collection, as the pagination is hardcoded into the Python functions.


## Task 5: Migrate documents between document stores

As a final step of our lab, we will create a small application that will retrieve documents from MongoDB and insert them in Oracle AJD. This use case will demonstrate that same data we currently have in MongoDB can be stored in and handled by Oracle AJD. JSON documents will receive a new **key** in Oracle AJD, however, they will also keep the original **id** from MongoDB.

1. Create a new file **simple-migrate.py**, with the following Python code. 

    ````
    # imports the required modules
    import os
    import json
    import pymongo
    import cx_Oracle

    # retrieve MongoDB connection info from os environment variables
    m_usr = os.environ['MONGO_DB_USER']
    m_pwd = os.environ['MONGO_DB_PASS']
    m_dbn = os.environ['MONGO_DB_NAME']

    # retrieve Oracle connection info from os environment variables
    o_usr = os.environ['ORCL_DB_USER']
    o_pwd = os.environ['ORCL_DB_PASS']
    o_srv = os.environ['ORCL_DB_SERV']

    # create MongoDB connection, and set collection used by application
    client = pymongo.MongoClient("mongodb+srv://" + m_usr + ":" + m_pwd + "@cluster0.dsbwl.mongodb.net/" + m_dbn + "?retryWrites=true&w=majority")
    mdb = client[m_dbn]
    mcollection = mdb['SimpleCollection']

    # create Oracle connection, and set collection used by application
    conn_string = o_usr + '/' + o_pwd + '@' + o_srv
    connection = cx_Oracle.connect(conn_string)
    connection.autocommit = True
    soda = connection.getSodaDatabase()
    ocollection = soda.createCollection("SimpleCollection")

    # main program module
    if __name__ == '__main__':
        # retrieve documents from MongoDB collection defined by 'mcollection'
        documents = mcollection.find()
        for document in documents:
            document['_id'] = str(document['_id'])
            # insert into Oracle collection defined by 'ocollection'
            doc = ocollection.insertOneAndGet(document)
            key = doc.key
            print('Migrated SODA document key: ', key)
            doc = ocollection.find().key(key).getOne() 
            content = doc.getContent()
            print('Migrated SODA document: ')
            print(content)
    ````

2. Run the migration application.

    ````
    python3.6 simple-migrate.py
    ````

3. All 4 JSON documents from MongoDB are migrated to Oracle JSON.

    ````
    Migrated SODA document key:  54DDE1D90F3F4FEDBF425668B917E167
    Migrated SODA document: 
    {'_id': '61640f6f34d7b9135ab04912', 'company': 'Company One', 'address': {'street': '22 Rue du Grenier Saint-Lazare', 'city': 'Paris', 'country': 'France'}, 'industry': 'Financial Services', 'employees': 54234}
    Migrated SODA document key:  390921C291974F8BBF86ED6D0C59CD7A
    Migrated SODA document: 
    {'_id': '6164112b34d7b9135ab04913', 'company': 'Company Two', 'address': {'street': 'Calle Extramuros 74', 'city': 'Madrid', 'country': 'Spain'}, 'industry': 'Retail', 'employees': 12345}
    Migrated SODA document key:  49B61A4D831B4FABBF3ECCE5F3AA44C2
    Migrated SODA document: 
    {'_id': '616427068dfd7681ee536576', 'company': 'Company Three', 'address': {'street': '3A Evergreen St, Ballyphehane', 'city': 'Cork', 'country': 'Ireland'}, 'industry': 'Manufacturing', 'employees': 98765}
    Migrated SODA document key:  AED9088164734FD3BF01D982571CAC37
    Migrated SODA document: 
    {'_id': '616427338dfd7681ee536577', 'company': 'Company Four', 'address': {'street': 'aleje Mikołaja Kopernika 32', 'city': 'Piotrków Trybunalski', 'country': 'Poland'}, 'industry': 'Manufacturing', 'employees': 44444}
    ````

4. Notice the migrated documents have an extra field `'_id'`, this is the original MongoDB document **id**.

5. Verify the results on Database Actions web interface, connected as **demo** user (password DBlearnPTS#21_), using Development > **JSON**. Select SimpleCollection collection, and use the ▶️ Play button to refresh data. All 8 JSON documents are supposed to be in Oracle AJD now.

6. Press CTRL+C in the terminal where the application is running, to stop it, if it is still running.


## Acknowledgements
* **Author** - Valentin Leonard Tabacaru, PTS
* **Contributors** -  Kay Malcolm, Database Product Management
* **Last Updated By/Date** -  Valentin Leonard Tabacaru, December 2020

## Need Help?
Please submit feedback or ask for help using our [LiveLabs Support Forum](https://community.oracle.com/tech/developers/categories/livelabsdiscussions). Please click the **Log In** button and login using your Oracle Account. Click the **Ask A Question** button to the left to start a *New Discussion* or *Ask a Question*.  Please include your workshop name and lab name.  You can also include screenshots and attach files.  Engage directly with the author of the workshop.

If you do not have an Oracle Account, click [here](https://profile.oracle.com/myprofile/account/create-account.jspx) to create one.
