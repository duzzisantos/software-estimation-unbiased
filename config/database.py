from pymongo import MongoClient
import os

connection_string = os.environ[
    "PYMONGO_CONNECTION_URL"
]  # Gains access to this env variable
mongo_client = MongoClient(connection_string)

database = mongo_client.software_estimation_bias
