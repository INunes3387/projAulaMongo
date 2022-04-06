import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

#sort("name", 1) #ascending
#sort("name", -1) #descending

mydoc = mycol.find().sort("name", 1)

#LISTAS TODAS AS COLUNAS
for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }).sort("name", 1):
  print(x)
