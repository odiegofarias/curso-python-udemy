"""
public, protected, private
_   -> Recomendável que não seja acessado
__  -> Recomendável FORTEMENTE que não seja acessado
"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    # acessar os valores do método
    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'] [id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Diego')
bd.inserir_cliente(2, 'Mirela')
bd.inserir_cliente(3, 'Jennifer')
bd.apaga_cliente(2)
bd.lista_clientes()
#  Não é possivel acessar dessa forma
#  print(bd.__dados)
#  para ver
print(bd._BaseDeDados__dados)
print(bd.dados)