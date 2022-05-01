from livro import LivroDB, converter_inteiro, nonetype


livro = LivroDB('livros.db')

print('1 - Inserir\n2 - Editar\n3 - Excluir\n4 - Listar\n5 - Buscar')
menu = converter_inteiro(input('Entre com a opção correspondente: '))
nonetype(menu)

match menu:
    case 1:
        nome = input('Informe o nome do livro: ')
        desc = input('Informe o autor do livro: ')
        lido = input('Informe se o livro foi lido (s = SIM, n = NÂO): ')
        livro.inserir(nome, desc, lido)

        livro.fechar()

    case 2:
        livro.listar()
        identificador = converter_inteiro(input('Informe o identificador da chave: '))

        chave = input('Informe a chave que quer editar: ')
        novo_valor_chave = input(f'Informe o novo conteúdo da chave {chave}: ')
        livro.editar(chave, novo_valor_chave, identificador)

        livro.fechar()

    case 3:
        livro.listar()
        identificador = converter_inteiro(input('Selecione o ID do livro que queira excluir: '))
        livro.excluir(identificador)

        livro.fechar()

    case 4:
        livro.listar()

        livro.fechar()

    case 5:
        chave = input('Informe a chave que quer buscar: ')
        nome_busca = input('Informe o nome que quer buscar: ')
        livro.buscar(chave, nome_busca)

        livro.fechar()






