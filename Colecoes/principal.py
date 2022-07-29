import pymongo
import pandas as pd
myclient = pymongo.MongoClient("mongodb+srv://bd2:bd2senha@cluster0.lwjkt.mongodb.net/?retryWrites=true&w=majority")
mydb = myclient["petshop"]
mycol_pet = mydb["pet"]
mycol_tutor = mydb["tutor"]

def main():

        print("----------------------------------------------")
        print("-------------------- MENU --------------------")
        print("----------------------------------------------")
        print("1 -> Retorna dados completos do pet por nome")
        print("2 -> Retorna dados completos do tutor por nome")
        print("3 -> Busca tutor de acordo com o pet")
        print("4 -> Busca pet de acordo com o tutor")
        print("5 -> Insira os dados do pet em nosso banco de dados")
        print("6 -> Insira os dados do tutor em nosso banco de dados")
        print("----------------------------------------------")
        print("----------------------------------------------")

        menu = int(input("Digite o número do menu -> "))
      
      
        if(menu == 1):
        
            nome = str(input("Digite o nome do pet -> "))
            agenda = []
            myquery = { "nome":  {"$regex": nome} }
            cursor = mycol_pet.find(myquery)
          
            for i in cursor:
        
             i = pd.Series({"Nome:": i['nome'], 'Raça:': i['raca'], 'Peso:': i['peso'], 'Idade:': i['idade']})
             print(i)  
            main()
        elif(menu == 2):
            nome = str(input("Digite o nome do tutor -> "))
            myquery = { "nome":  {"$regex": nome} }
            cursor = mycol_tutor.find(myquery)
            for i in cursor:
                print(i)
            main()
        elif(menu == 3):
            nome = str(input("Digite o nome do pet -> "))
            pipeline = [{
                "$lookup": {
                    "from": "tutor",
                    "localField": "ID_Tutor",
                    "foreignField": "_id",
                    "as": "join_Tutor"
                }
            }
            ,{"$unwind": "$join_Tutor"}
            ,{"$match": {"nome": nome}}
            ,{'$project': {'nome_pet': "$nome", 'raca': "$raca", 'peso': "$peso", 'idade': "$idade",'nome_tutor':"$join_Tutor.nome", 'telefone': "$join_Tutor.telefone", 'cpf': "$join_Tutor.cpf", 'endereco': "$join_Tutor.endereco" }}
            ]
            doc = mycol_pet.aggregate(pipeline)
            for i in doc:
                print(i)
            main()
        elif(menu == 4):
            nome = str(input("Digite o nome do tutor -> "))
            pipeline = [{
                "$lookup": {
                    "from": "pet",
                    "localField": "_id",
                    "foreignField": "ID_Tutor",
                    "as": "join_pet"
                }
            }
            ,{"$unwind": "$join_pet"}
            ,{"$match": {"nome": nome}}
            ,{'$project': {'nome do pet': "$join_pet.nome", 'raca': "$join_pet.raca", 'peso': "join_pet.$peso", 'idade': "$join_pet.idade" }}
            ]
            doc = mycol_tutor.aggregate(pipeline)
            for i in doc:
                print(i)
            main()
        elif(menu == 5):
            nome = str(input("Digite o nome do pet -> "))
            raca = str(input("Digite a raca do pet -> "))
            peso = int(input("Digite o peso do pet -> "))
            idade = int(input("Digite a idade do pet -> "))
            mydict = { "nome": nome, "raca": raca, "peso": peso, "idade": idade }
            
            x = mycol_pet.insert_one(mydict)
            main()
        elif(menu == 6):
            nome = str(input("Digite o nome do tutor -> "))
            telefone = str(input("Digite o telefone do tutor -> "))
            cpf = int(input("Digite o cpf do tutor -> "))
            endereco = str(input("Digite o endereco do tutor -> "))
            mydict = { "nome": nome, "telefone": telefone, "cpf": cpf, "endereco":endereco }
            
            x = mycol_tutor.insert_one(mydict)
            main()
        
        else: 
            print("Opção inválida, por favor digite uma das opções a cima!")
    
 
main()


#formatar para sair arrumado
#tirar os ID
#Retornar por parte do nome
#Para alinhar as colunas à esquerda no dataframe do pandas, usamos a função dataframe. style. set_properties() .
