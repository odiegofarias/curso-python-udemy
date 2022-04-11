def remover_caracteres(cnpj):
    cnpj = cnpj.replace('.', '')
    cnpj = cnpj.replace('/', '')
    cnpj = cnpj.replace('-', '')
    return cnpj


#  Usando expressões regulares
#  import re
# def remover_caracteres(cnpj):
#     return re.sub(r'[^0-9]', '', cnpj) #  Diferente de 0 a 9, substituir por NADA, variavel
