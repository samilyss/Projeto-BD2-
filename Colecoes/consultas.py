import pymongo
myclient = pymongo.MongoClient("mongodb+srv://bd2:bd2senha@cluster0.lwjkt.mongodb.net/?retryWrites=true&w=majority")
mydb = myclient["petshop"]
mycol_pet = mydb["pet"] 


#myquery = { "nome": "Dory" }
#mydoc = mycol.find(myquery)

#for x in mydoc:
  #print(x)




result = mycol_pet.aggregate([
    {
        '$lookup': {
            'from': 'tutor',
            'localField': 'ID_Tutor',
            'foreignField': 'id',
            'as': 'joinedResult'
        }
    }
])

myquery = { "nome": { "$regex": "^S" } }

mydoc = mycol_pet.find(myquery)

for x in mydoc:
  print(x)