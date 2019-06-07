from item import Item
from produto import Produto
class Carrinho:
    def __init__(self, itens):
        self.itens = []

if __name__ == "__main__":

    arroz = Produto("arroz", 12.99)
    leite = Produto("leite", 1.99)
    item1 = Item(arroz, 2)
    item2 = Item(leite, 5)
    carrinho = Carrinho([item1, item2])
