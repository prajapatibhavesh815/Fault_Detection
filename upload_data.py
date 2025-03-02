from pymongo.mongo_client import MongoClient
import pandas as pd
import json
#uri

uri ="mongodb+srv://bhavesh256:bhavesh815@cluster0.xvx7b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
#create a new client and connect to server

client = MongoClient(uri)
DATABASE_NAME = "bhavesh256"
COLLECTION_NAME = "waferfault"
df = pd.read_csv(r"D:\Bhavesh\ML_project\spam_detection_project\notebooks\wafer_23012020_041211.csv")
df.head()
df = df.drop("Unnamed: 0",axis=1)
json_record = list(json.loads(df.T.to_json()).values())
json_record
#uploading json data to mongodb
client [DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
