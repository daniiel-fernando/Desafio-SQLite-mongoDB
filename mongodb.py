from pymongo import MongoClient

client = MongoClient('mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = client['banco']
colecao = db['clientes']

def inicializar_banco_nosql():
    documento1 = {
        'nome': 'João',
        'idade': 30,
        'conta': {'saldo': 1500}
    }
    
    documento2 = {
        'nome': 'Maria',
        'idade': 25,
        'conta': {'saldo': 3000}
    }
    
    colecao.insert_many([documento1, documento2])

if __name__ == "__main__":
    inicializar_banco_nosql()
    
    # Exemplo de recuperação de dados do MongoDB
    resultado = colecao.find({'nome': 'João'})
    for documento in resultado:
        print(documento)
    
    client.close()
