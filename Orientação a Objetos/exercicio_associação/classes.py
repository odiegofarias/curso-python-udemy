class Carro:
    def __init__(self, marca, modelo, acelerando=False, parando=False):
        self.__marca = marca
        self.__modelo = modelo
        self.acelerando = acelerando
        self.parando = parando
        self.__finalidade = None

    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo

    def acelerar(self):
        print('O carro está acelerando')
        if self.acelerando:
            print('O carro já está acelerando.')
            return

        self.acelerando = True

    @property
    def finalidade(self):
        return self.__finalidade

    @finalidade.setter
    def finalidade(self, finalidade):
        self.__finalidade = finalidade


class Pneus:
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo

    def correr(self):
        print(f'Estou correndo com pneus')


class Corrida:
    def correr(self):
        print('Corrida')