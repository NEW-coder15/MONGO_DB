#Creating a Database
import pymongo
#Create a database called "mydatabase"
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
print(myclient.list_database_names())
#Return a list of your system's databases:
dblist = myclient.list_database_names()
#Or you can check a specific database by name:
#Check if "mydatabase" exists:
if "mydatabase" in dblist:
  print("The database exists.")