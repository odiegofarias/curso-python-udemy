from abc import ABC, abstractmethod
from cliente import Cliente


class Conta(ABC, Cliente):
    def __init__(self, saldo, nome, idade, agencia, conta):
        super().__init__(self, nome, idade, agencia, conta)
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (float, int)):
            raise ValueError ('Entre com um valor numérico, por favor.')

        self.saldo += valor
        self.detalhes_cliente()

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor > self.saldo:
            print('Saldo indisponível')
            return

        self.saldo -= valor
        self.detalhes_cliente()


class ContaCorrente(Conta):
    def __init__(self, saldo, agencia, nome, idade, conta, limite=100):
        Conta.__init__(self, saldo, nome, idade, agencia, conta)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if valor > self.saldo + self.limite:
            print('Saldo indisponível')
            return

        self.saldo -= valor
        self.detalhes_cliente()

