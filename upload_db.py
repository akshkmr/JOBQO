import json
from pymongo import MongoClient

CONNECTION_STRING = "mongodb+srv://cryptoduh:arya0792@jobqo-usud6.mongodb.net/test?retryWrites=true&w=majority"
client = MongoClient(CONNECTION_STRING)

content = client['jobqo_db']['job_record']

with open('business.json', encoding='utf-8-sig') as f:
    file_data = json.load(f)

content.insert_many(file_data)

client.close()
