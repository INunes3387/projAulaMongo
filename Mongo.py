import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["aula5DB"]
mycol = mydb["customers"]

mydict = {"nome": "Nunes", "email": "Nunes@teste.com", "telefone": "16 9999 7777"}

x = mycol.insert_one(mydict)

print(x.inserted_id)