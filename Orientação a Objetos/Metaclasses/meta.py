"""
EM PYTHON TUDO È UM OBJETO: Incluindo classes, metaclasses
são as "classes" que criam classes
type é uma METACLASSE!!!
"""


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        #  Fazer com que o método 'b_fala' dê erro até que seja criado na classe B
        # if 'b_fala' not in namespace:
        #     print(f'Oi, você precisa criar o método b_fala em {name}')
        # else:
        #     if not callable(namespace['b_fala']):
        #         print(f'b_fala precisa ser um método, não atributo em {name}')

        #  Para que Atributo não seja sobrescrito por outra classe
        if 'attr_classe' in namespace:
            print(f'{name} tentou sobrescrever o atributo')
            del namespace['attr_classe']

        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    #  def fala(self):
    #      self.b_fala()
    attr_classe = 'valor A'


class B(A):
    # def b_fala(self):
    #     print('Oi')
    attr_classe = 'valor B'


class C(B):

    attr_classe = 'valor B'


c = C()
print(c.attr_classe)


# TYPE para criar classes
class Pai:
    nome = 'Diego'


D = type('D', #  nome da classe
         (Pai,),  # de quem ela é herda/TUPLA - por isso a virgula
         {
              #  atributo
             'attr': 'Olá, Mundo!'
         }
)

d = D()
print(d.nome)
