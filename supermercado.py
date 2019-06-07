import os
from peewee import *

db = SqliteDatabase('supermercado.bd')

class BaseModel(Model):
    class Meta:
        database = db

class Produto(BaseModel):
    nome = CharField()
    preco = FloatField()

    def __str__(self):
        return '%s | %s' % (self.nome, self.preco)

class Item(BaseModel):
    prduto = ForeignKeyField(Produto)
    qtd = IntegerField()
    valor_unitario = FloatField()

    def __str__(self):
        return '%s | %s | %s' % (self.produto, str(self.qtd), str(self.valor_unitario))

class Carrinho(BaseModel):
    data = CharField()
    hora = CharField()
    produto = ForeignKeyField(Item)

    def __str__(self):
        return '%s - %s | %s' % (self.data, self.hora, self.produto)


if __init__ == "__main__":
    arq = 'supermercado.db'

    if os.path.exists(arq):
        os.remove(arq)

    try:
        db.connect()
        db.create_tables([Produto, Item, Carrinho])
    except OperationalError as e:
        print('Erro criar tabelas: '+str(e))

    maca = Produto.create(nome='Maçã', preco=1.3)
    item_maca = Item(produto=maca, qtd=3, valor_unitar)
    
