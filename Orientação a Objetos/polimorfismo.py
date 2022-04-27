from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def fala(self, msg): pass


class B(A):
    def fala(self, msg):
        print(f'B está falando de {msg}')


class C(A):
    def fala(self, msg):
        print(f'C está falando de {msg}')

        
b = B()
c = C()

b.fala('Um Assunto')
c.fala('Outro assunto')

