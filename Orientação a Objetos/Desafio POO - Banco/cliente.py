"""
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
"""


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Cliente(Pessoa):
    def __init__(self, nome, idade, agencia, conta):
        super().__init__(nome, idade)
        self._agencia = agencia
        self._conta = conta

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    def detalhes_cliente(self):
        print('Dados do usuário:')
        print(f'Cliente: {self.nome}')
        print(f'Idade: {self.idade} anos')
        print(f'Agencia: {self.agencia}', end=' ')
        print(f'Conta: {self.conta}')


