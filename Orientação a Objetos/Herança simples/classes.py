"""
Associação - Usa | Agregação - Tem | Composicação - É dono | Herança - É
"""


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    #  Pertence a TODAS AS CLASSES
    def falar(self):
        print(f'{self.nomeclasse} está falando')


class Cliente(Pessoa):
    #  Pertence somente ao CLIENTE
    def comprar(self):
        print(f'{self.nomeclasse} está comprando')

    def falar(self):
        print('Estou em Cliente.')


class Aluno(Pessoa):
    #  Pertence somente ao ALUNO
    def estudar(self):
        print(f'{self.nomeclasse} está estudando')


class ClienteVip(Cliente):
    #  Sobrescrevendo o método em Pessoa
    # def falar(self):
    #     #  Refere-se à superclasse
    #     # super().falar()
    #     Pessoa.falar(self)
    #     Cliente.falar(self)
    #
    #     print('Estou em cliente VIP')
    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome} está falando.')