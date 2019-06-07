class Consulta(peewee.Model):
    data = peewee.CharField()
    servico = peewee.CharField()
    horario = peewee.CharField()
    animal = peewee.ForeignKeyField(Animal)
    confirma = peewee.CharField()
    myID = peewee.CharField()
    
    class Meta:
        database = db

    def __str__(self):
        return self.servico+", ID da consulta: " + self.myID+"| animal: " +str(self.animal)

if __name__=="__main__":
    arq = "animalia.db"
    if  os.path.exists (arq):
        os.remove(arq)

    try:
        db.connect()
        db.create_tables([Animal, Consulta])
    
    except peewee.OperationalError as e:
        print("erro ao criar tabelas: " + str(e))

    print("TESTE DO ANIMAL")

    al = Animal(nomedono = "Ricardo", tipo_animal = "C", raca = "Rusky")
    print(al)

    print("TESTE DA CONSULTA")
    cl = Consulta(data = "19/09/2018", servico = "Consulta de rotina", horario = "14:00", animal = al, confirma = "N", myID = "c9dsadsa8dasdga9"
    print(cl)

