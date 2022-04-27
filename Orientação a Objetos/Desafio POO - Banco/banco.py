"""
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
"""


class Banco:
    def __init__(self, agencia=6942, conta=248946):
        self._agencia = agencia
        self._conta = conta

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta