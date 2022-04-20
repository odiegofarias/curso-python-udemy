from classes import Cliente


cliente1 = Cliente('Diego', 27)
cliente1.insere_endereco('Recife', 'PE')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()

cliente2 = Cliente('Mirela', 21)
cliente2.insere_endereco('São Paulo', 'SP')
cliente2.insere_endereco('Belo Horizonte', 'MG')
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente2
print()

cliente3 = Cliente('Jennifer', 27)
cliente3.insere_endereco('Salvador', 'BA')
cliente3.insere_endereco('Rio das Ostras', 'RJ')
print(cliente3.nome)
cliente3.lista_enderecos()
del cliente3
print()

print('####################GARBAGE COLECTOR10###################')