#Update Collection
#You can update a record, or document as it is called in MongoDB, by using the update_one() method.

#The first parameter of the update_one() method is a query object defining which document to update.
#Change the address from "Valley 345" to "Canyon 123":

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

mycol.update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycol.find():
  print(x)
#Update Many
#To update all documents that meets the criteria of the query, use the update_many() method.

#Example
#Update all documents where the address starts with the letter "S":

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }

x = mycol.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")