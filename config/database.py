from pymongo import MongoClient
from pymongo.server_api import ServerApi
import certifi

import os
from dotenv import load_dotenv

load_dotenv()


## Establish server connection with MongoDB
connection_string = os.getenv("MONGO_URL")
mongo_client = MongoClient(
    connection_string,
    server_api=ServerApi("1"),
    tlsCAFile=certifi.where(),
)


database = mongo_client.software_estimation_bias

## Define all collections
collection_name = database["software_work_log"]
training_result = database["training_result"]

# Send a ping to confirm a successful connection
try:
    mongo_client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
