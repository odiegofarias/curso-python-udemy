lista = [1, 2, 3]
#  _ Qualquer valor ou se for no CASE, um caso coringa.
match lista:
    case [] | [_]:
        print('Um ou nenhum número.')
    case [1, *resto]:
        #  Vai colocar o restante dos números em outra lista
        print(f'O primeiro número é 1 e o {resto=}')
    #   case [1|2, _, _]:     | OU
    #   print('Começa com 1 ou 2')

#   Usando nomes
print()

#   cor = (255, 255, 255)
cor = (255, 255, 255, 255)
match cor:
    case r, g ,b: #  len(3)
        print(f'{r=}, {g=}, {b=}')
    case r, g, b, a: #   len(4)
        print(f'{r=}, {g=}, {b=}, {a=}')

print()


def movimento(acao: str):
    match acao.split():
        case ['pular']:
            return 'Pulando'
        #  as é usado para nomear e dar contexto as coisas
        case 'mover', 'direita' | 'esquerda' as direcao:
            return f'Movendo para {direcao}'


print(movimento('mover esquerda'))
