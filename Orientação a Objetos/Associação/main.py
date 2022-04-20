from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Diego')
caneta = Caneta('BIC')
maquina_de_escrever = MaquinaDeEscrever()

#  Associações
escritor.ferramenta = maquina_de_escrever
escritor.ferramenta.escrever()

#  Outros Exemplos
# del escritor
# print(caneta.marca)
# maquina_de_escrever.escrever()