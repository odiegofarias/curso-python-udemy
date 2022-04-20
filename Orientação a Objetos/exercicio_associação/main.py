from classes import Carro
from classes import Pneus
from classes import Corrida


carro = Carro('BMW', 'M5')
pneus = Pneus('Goodyear', 'Para chuva')
corrida = Corrida()
print(carro.marca, carro.modelo)


#  Acessando métodos de outra classe
carro.finalidade = pneus
carro.finalidade.correr()

#  Acessando atributos de outra classe
print(carro.finalidade.marca, carro.finalidade.modelo)

# carro.finalidade = corrida
# carro.finalidade.correr()


