import pandas as pd
import pymongo
from pymongo import MongoClient

df = pd.read_csv('Inpatient_Rehabilitation_Facility-General_Information_Sep2024 - Inpatient_Rehabilitation_Facility-General_Information_Sep2024.csv')

client = pymongo.MongoClient()
db = client['stats']
collection = db['Rehabilitation Facility']                             

collection.insert_many(pd.to_dict('records'))

db_base = pd.DataFrame(list(collection.find))

print(db_base)
print(collection)





