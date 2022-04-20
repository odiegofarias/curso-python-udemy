from datetime import datetime
from random import randint


class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    #  método
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return

        if self.falando:
            print(f'{self.nome} já está falando sobre.')
            return

        print(f'{self.nome} está falanando sobre {assunto}')
        self.falando = True

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return
            #  Não executa mais nada aqui embaixo

        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            return

        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando.')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade

    #  Método de classe
    # Usar quando o método é relacionado a classe em si
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    #  
    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand


#  Pegando o ano de nascimento e verificando a idade
p1 = Pessoa.por_ano_nascimento('Diego', 1994)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()

#  Pode chamar pela instância também
print(Pessoa.gera_id())
