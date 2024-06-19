from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///clientes_contas.db', echo=True)
Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    
    def __repr__(self):
        return f'<Cliente(nome={self.nome}, idade={self.idade})>'

class Conta(Base):
    __tablename__ = 'contas'

    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    saldo = Column(Integer)

    cliente = relationship('Cliente', back_populates='contas')

    def __repr__(self):
        return f'<Conta(cliente_id={self.cliente_id}, saldo={self.saldo})>'

Cliente.contas = relationship('Conta', order_by=Conta.id, back_populates='cliente')

def inicializar_banco_relacional():
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    cliente1 = Cliente(nome='João', idade=30)
    cliente2 = Cliente(nome='Maria', idade=25)
    
    conta1 = Conta(cliente=cliente1, saldo=1500)
    conta2 = Conta(cliente=cliente2, saldo=3000)
    
    session.add_all([cliente1, cliente2, conta1, conta2])
    session.commit()
    session.close()
