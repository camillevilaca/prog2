import peewee, os

db = peewee.SqliteDatabase("animalia.db")

class Animal(peewee.Model):
    nomedono = peewee.CharField()
    tipo_animal = peewee.CharField()
    raca = peewee.CharField()

    class Meta:
        database = db
    
    def __str__ (self):
        return self.tipo_animal+","+ self.raca + "de" + self.nomedono
        