import pymongo
myclient = pymongo.MongoClient("mongodb+srv://bd2:bd2senha@cluster0.lwjkt.mongodb.net/?retryWrites=true&w=majority")
mydb = myclient["petshop"]
mycol = mydb["pet"]

myquery = { "nome": "Dory" }
mydoc = mycol.find(myquery)