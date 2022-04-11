from remover_caracter import remover_caracteres


peso1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
peso2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
cnpj_referencia = remover_caracteres('03.361.252/0001-34')


#  Para cada item da lista, transforme em inteiro
cnpj = list(map(int, cnpj_referencia[0:12]))


#  Fazendo a multiplicação de cada número das listas
lista_metodo1 = [cnpj * peso1 for cnpj, peso1 in zip(cnpj, peso1)]   #  list Comprehension


# Fazendo a soma de todos os números gerados a partir da multiplicação
val_anterior = 0
for item in lista_metodo1:
    val_anterior += item
formula = 11 - (val_anterior % 11)
cnpj.append(formula)


# Fazendo a multiplicação da lista do peso2 com o número gerado pelo metodo 1
lista_metodo2 = [cnpj_int * peso2 for cnpj_int, peso2 in zip(cnpj, peso2)]

#  Resetando o valor de val_anterior
val_anterior = 0

#  Iterando a lista com o método 2
for item in lista_metodo2:
    val_anterior += item


#  Aplicando a formula 2 ao valor obtido no val_anterior
formula2 = 11 - (val_anterior % 11)


#  Verificando o ultimo digito.
if formula2 > 9:
    cnpj.append(0)
else:
    cnpj.append(formula2)
cnpj_referencia = list(cnpj_referencia)
print(cnpj)
cnpj_referencia = list(map(int, cnpj_referencia))
print(cnpj_referencia)

if cnpj_referencia == cnpj:
    print('CNPJ Válido.')
else:
    print('CNPJ Inválido.')






