import pymongo
from IPython.display import display
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
        
            nome = str(input("Digite o nome do pet ->"))
            myquery = { "nome":  {"$regex": nome} }
            cursor = (mycol_pet.find(myquery))
           
            if (cursor == True):
                 print("\n        Dados de " + nome + "\n")
                 for i in cursor:
        
                    i = pd.Series({"Nome:": i['nome'], 'Raça:': i['raca'], 'Peso:': i['peso'], 'Idade:': i['idade']})
                    print(i)  
                    main()
            else:
                x = int (input(nome + " não está cadastrado(a), deseja cadastrar seu pet? Sim ou não? "))
                if x =="Sim" or "sim":
                     nome = str(input("Digite o nome do pet -> "))
                     raca = str(input("Digite a raca do pet -> "))
                     peso = int(input("Digite o peso do pet -> "))
                     idade = int(input("Digite a idade do pet -> \n"))
                     mydict = { "nome": nome, "raca": raca, "peso": peso, "idade": idade }
                        
                     resultado = mycol_pet.insert_one(mydict)
                     if resultado != 0:
                                        print("\n Os dados foram armazenados com sucesso!")
                     else:
                                        print("\nDados não foram armazenados, por favor tente novamente")
                     main()
           
        elif(menu == 2):
            nome = str(input("Digite o nome do tutor ->"))
            myquery = { "nome":  {"$regex": nome}  }
            cursor = mycol_tutor.find(myquery)
          
            for i in cursor:
             i = pd.Series({"Nome:": i['nome'], 'Telefone:': i['telefone'], 'CPF:': i['cpf'], 'Endereço:': i['endereco']})
             print(i)
            main()

        elif(menu == 3):
            nome = str(input("Digite o nome do pet -> \n"))
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
             i = pd.Series({"Nome:": i['nome_pet'], 'Telefone:': i['telefone'], 'CPF:': i['cpf'], 'Endereço:': i['endereco'], "Nome:": i['nome_tutor'], 'Telefone:': i['telefone'], 'CPF:': i['cpf'], 'Endereço:': i['endereco']})
             print(i)
            main()
        elif(menu == 4):
            nome = str(input("Digite o nome do tutor -> \n"))
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
            ,{'$project': {'nome_pet': "$join_pet.nome", 'raca': "$join_pet.raca", 'peso': "$join_pet.peso", 'idade': "$join_pet.idade" }}
            ]
            doc = mycol_tutor.aggregate(pipeline)
            for i in doc:
             i = pd.Series({"Nome:": i['nome_pet'], 'Raca:': i['raca'], 'Peso:': i['peso'], 'Idade:': i['idade']})
             print(i)
            main()
        elif(menu == 5):
            nome = str(input("Digite o nome do pet -> "))
            raca = str(input("Digite a raca do pet -> "))
            peso = int(input("Digite o peso do pet -> "))
            idade = int(input("Digite a idade do pet -> \n"))
            mydict = { "nome": nome, "raca": raca, "peso": peso, "idade": idade }
            
            resultado = mycol_pet.insert_one(mydict)
            if resultado != 0:
                            print("\n Os dados foram armazenados com sucesso!")
            else:
                            print("\nDados não foram armazenados, por favor tente novamente")
            main()
        elif(menu == 6):
            nome = str(input("Digite o nome do tutor -> "))
            telefone = str(input("Digite o telefone do tutor -> "))
            cpf = int(input("Digite o cpf do tutor -> "))
            endereco = str(input("Digite o endereco do tutor -> \n"))
            mydict = { "nome": nome, "telefone": telefone, "cpf": cpf, "endereco":endereco }
            
            resultado = mycol_tutor.insert_one(mydict)
            if resultado != 0:
                            print("\n Os dados foram armazenados com sucesso!")
            else:
                            print("\nDados não foram armazenados, por favor tente novamente")
            main()
        
        else: 
            print("Opção inválida, por favor digite uma das opções a cima!")
            main()
main()


#formatar para sair arrumado
#tirar os ID
#Retornar por parte do nome
#Para alinhar as colunas à esquerda no dataframe do pandas, usamos a função dataframe. style. set_properties() .
