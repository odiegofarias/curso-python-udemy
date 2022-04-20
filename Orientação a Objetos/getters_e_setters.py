#  Getter - Obtem
#  Setter - Configura
#  Proteção para atributos


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    #  Getter NOME
    @property
    def nome(self):
        return self._nome

    #  Setter NOME
    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()

    #  Getter Preço
    @property
    def preco(self):
        #  Por convenção utiliza o _ antes do atributo
        return self._preco

    #  Setter Preço
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor


p1 = Produto('CAMISETA', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('CANECA', 'R$15')
p2.desconto(10)
print(p2.nome, p2.preco)