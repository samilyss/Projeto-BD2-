import pymongo

def pegar_banco():
    cliente = pymongo.MongoClient("mongodb+srv://bd2:bd2senha@cluster0.lwjkt.mongodb.net/?retryWrites=true&w=majority")
    meu_banco = cliente["petshop"]
    return meu_banco

def inserir_exemplo_pet():
    meu_banco = pegar_banco()
    colecao_pet = meu_banco["pet"]

    mydict = { "nome": "Bella", "raca": "Dalmata", "peso": "20kg", "idade": "8 anos" }
    x = colecao_pet.insert_one(mydict)
    mydict = { "nome": "Lilica", "raca": "Poodle", "peso": "10kg", "idade": "11 anos" }
    x = colecao_pet.insert_one(mydict)
    mydict = { "nome": "Bob", "raca": "Yorkshire", "peso": "5kg", "idade": "3 anos" }
    x = colecao_pet.insert_one(mydict)
    mydict = { "nome": "Max", "raca": "Bull Terrier", "peso": "15kg", "idade": "5 anos" }
    x = colecao_pet.insert_one(mydict)
    mydict = { "nome": "Dory", "raca": "Buldogue Inglês", "peso": "10kg", "idade": "4 anos" }
    x = colecao_pet.insert_one(mydict)
    mydict = { "nome": "Simba", "raca": "Golden Retriever", "peso": "15kg", "idade": "5 anos" }
    x = colecao_pet.insert_one(mydict)
    mydict = { "nome": "Pity", "raca": "Labrador Retriever", "peso": "12kg", "idade": "6 anos" }
    x = colecao_pet.insert_one(mydict)
    mydict = { "nome": "Nina", "raca": "Vira-Lata", "peso": "5kg", "idade": "3 anos" }
    x = colecao_pet.insert_one(mydict)
    mydict = { "nome": "Tom", "raca": "Siamês", "peso": "7kg", "idade": "10 anos" }
    x = colecao_pet.insert_one(mydict)
    mydict = { "nome": "Sushi", "raca": "Sphynx", "peso": "4kg", "idade": "6 anos" }
    x = colecao_pet.insert_one(mydict)

def inserir_exemplo_tutor():
    meu_banco = pegar_banco()
    colecao_pet = meu_banco["tutor"]
    
    mydict = { "nome": "Alane", "telefone": "991162490", "cpf": "12269976436", "cep": "50740-545" }
    x = colecao_pet.insert_one(mydict)
    mydict = { "nome": "Milena", "telefone": "983056594", "cpf": "09289217430", "cep": "50740-592" }
    x = colecao_pet.insert_one(mydict)
    mydict = { "nome": "Samily", "telefone": "986810071", "cpf": "13112214412", "cep": "50740-521" }
    x = colecao_pet.insert_one(mydict)
    mydict = { "nome": "Camile", "telefone": "996137484", "cpf": "13751402489", "cep": "51030040" }
    x = colecao_pet.insert_one(mydict)
    mydict = { "nome": "João", "telefone": "999999999", "cpf": "11987264371", "cep": "51030050" }
    x = colecao_pet.insert_one(mydict)
    mydict = { "nome": "Lucas", "telefone": "955543643", "cpf": "11987264770", "cep": "60030044" }
    x = colecao_pet.insert_one(mydict)
