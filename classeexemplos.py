class Carro():
    def __init__(self, marca = ""):
        self.marca = marca 

class Funcionario():
    def __init__(self, nome = ""):
        self.nome = nome 

    def dirigir(self, carro):
        print(self.nome+" esta dirigindo um "+carro.marca)

carro = Carro("Civic")
funcionario = Funcionario("Camila")
funcionario.dirigir(carro)
