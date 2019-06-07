import peewee, os

db = peewee.SqliteDatabase('Animal.db')

class Animal(peewee.Model):
    nome_dono = peewee.CharField()
    tipo_animal = peewee.CharField()
    raca = peewee.CharField()
    class Meta:
        database = db
    def mostrar_animal(self):
        animal1 = Animal("Carlos", "Lacoste", "Poodle")
        return self.tipo_animal+","+self.raca+" de "+self.nomedono

class Cliente(peewee.Model):
    nome = peewee.CharField()
    email = peewee.CharField()
    telefone = peewee.IntegerField()
    id = peewee.IntegerField()
    nome_login = peewee.CharField()
    senha = peewee.CharField()
    class Meta:
        database = db

class Consulta(peewee.Model):
    data = peewee.DateField()
    servico = peewee.CharField()
    horario = peewee.CharField()
    cliente = peewee.ForeignKeyField(Cliente)
    animal = peewee.ForeignKeyField(Animal)
    confirma = peewee.CharField()
    class Meta:
        database = db

class Comentario(peewee.Model):
    nome = peewee.CharField()
    email = peewee.CharField()
    mensagem = peewee.CharField()
    class Meta:
        database = db

class Produto(peewee.Model):
    nomep = peewee.CharField()
    quantidade = peewee.IntegerField()
    codigo = peewee.IntegerField()
    descricao = peewee.CharField()
    class Meta:
        database = db

class Reserva(peewee.Model):
    data_reserva = peewee.CharField()
    cliente = peewee.ForeignKeyField(Cliente)
    produto = peewee.ForeignKeyField(Produto)
    quantidade = peewee.IntegerField()
    id = peewee.CharField()
    confirmacao = peewee.CharField()
    class Meta:
        database = db

if __name__ == "__main__":
    a = mostrar_animal(self)
    print (a)
