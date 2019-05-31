import peewee,os
db = peewee.SqliteDatabase("animalia.db")

class Animal(peewee.Model):
    nomedono = peewee.CharField()
    tipo.animal = peewee.CharField()
    raca = peewee.CharField()
    class Meta:
        database = db
    def __str__ (self):
        return self.tipo.animal+","+self.raca+"de"+self.nomedono

class Consulta(peewee.Model):
    data = peewee.CharField()
    servico = peewee.CharField()
    horario = peewee.CharField()
    cliente = peewee.ForeignKeyField(Cliente)
    animal = peewee.ForeignKeyField(Animal)
    confirma = peewee.CharField()
    myID = peewee.CharField()
    class Meta:
        database = db
    def __str__ (self):
        return self.servico+"em"+self.data+":"+self.horario=", confirmado:"+self.confirma+", ID da consulta:"+self.myID+"| animal: "+str(self.animal)
    
class Cliente(peewee.Model):
    nome = peewee.CharField()
    email = peewee.CharField()
    ID = peewee.IntegerField()
    nomelogin = peewee.CharField()
    senha = peewee.CharField()
    class Meta:
        database = db
    def __str__ (self):
        return self.nome+","+self.email+"Seu Login é: "+self.nome.login+"ID do cliente:"+self.ID

if __name__=='__main__':
    arq = "animalia.db"
    if os.path.exists(arq):
        os.remove(arq)
    try:
        db.connect()
        db.create_tables ([Animal,Consulta,Cliente])
    except peewee.OperationalError as e:
        print ("erro: "+str(e))