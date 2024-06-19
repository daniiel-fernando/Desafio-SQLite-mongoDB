from sqlite_setup import inicializar_banco_relacional
from mongodb_setup import inicializar_banco_nosql
from pymongo import MongoClient

if __name__ == "__main__":
    inicializar_banco_relacional()
    inicializar_banco_nosql()
    
    # Exemplo de recuperação de dados do MongoDB
    client = MongoClient('mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    colecao = client['banco']['clientes']
    
    resultado = colecao.find({'nome': 'João'})
    for documento in resultado:
        print(documento)
    
    client.close()
