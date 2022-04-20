from classes import Produto, CarrinhoDeCompras


carrinho = CarrinhoDeCompras()

while True:
    nome_produto = input('Informe o nome do produto: ')
    if nome_produto == 'exit':
        print('Saindo...')
        break
    preco_produto = float(input('Informe o valor do produto: '))
    produto = Produto(nome_produto, preco_produto)
    carrinho.inserir_produto(produto)


carrinho.lista_produtos()
print(f'Total no carrinho: R$ {carrinho.soma_total()}')
