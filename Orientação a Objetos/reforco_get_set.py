#  Setter = Configurando valor (=)
#  Getter = Obter um valor (.)

class Pessoa:
    def __init__(self, nome):
        self._nome = nome

    @property  # atributo
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def sobrenome(self):
        return 'Farias'


p1 = Pessoa('Diego')
print(p1.nome)
print(p1.sobrenome)
