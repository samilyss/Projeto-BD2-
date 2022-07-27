import pymongo
myclient = pymongo.MongoClient(
    "mongodb+srv://bd2:bd2senha@cluster0.lwjkt.mongodb.net/?retryWrites=true&w=majority")
mydb = myclient["petshop"]
mycol_pet = mydb["pet"]


#myquery = { "nome": "Dory" }
#mydoc = mycol.find(myquery)

# for x in mydoc:
# print(x)


result = mycol_pet.aggregate([
{
     '$lookup': {
     'from': 'tutor',
    'localField': 'ID_Tutor',
 'foreignField': '_id',
 'as': 'joinedResult'
}
}
])

for x in result:
 print(x)
myquery = { "nome": { "$regex": "^S" } }

mydoc = mycol_pet.find(myquery)


# resultado = mydb.pet.aggregate([
#     {
#         '$lookup':
#         {
#             'from': "tutor",

#             'pipeline': [
#                 {'$match': {'nome': "Sushi"}},
#                 {'$project': {'_id': "62cf041725b33fe9f6aad10e", 'tutor': {'nome':"$nome", 'endereco': "$endereco" }}},
#                 {'$replaceRoot': {'newRoot': "$nome"}}
#             ],
#             'as': "teste"
#         }
#     }

# ])
# for x in resultado:
#     print(x)
