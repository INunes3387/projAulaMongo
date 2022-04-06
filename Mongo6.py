import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address" : "Apple st 652"}
new_value = { "$set" : { "name" : "Amy Amarelo"}}

mycol.update_one(myquery,new_value)

for x in mycol.find(myquery):
    print(x)