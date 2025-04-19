#Create a collection called "customers":
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

mycol = mydb["customers"]
#Check if Collection Exists
#Return a list of all collections in your database
print(mydb.list_collection_names())
#Or you can check a specific collection by name:
collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")
