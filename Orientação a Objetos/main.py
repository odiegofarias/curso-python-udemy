from pessoa import Pessoa

#  instanciar
p1 = Pessoa('Diego', 28)
p1.comer('maçã')
p1.falar('POO')
p1.parar_comer()
p1.falar('POO')
p1.comer('banana')
p1.parar_falar()
p1.falar('POO')
p1.parar_falar()

print('\n\n')

p2 = Pessoa('João', 32)
p1.falar('POO')
p2.falar('Filmes')

print('\n\n')

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

