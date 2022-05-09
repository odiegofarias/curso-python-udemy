import sqlite3


def converter_inteiro(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        pass


def nonetype(valor):
    if valor is None or valor > 5:
        print('Entrada incorreta. Tente novamente.')


class LivroDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, autor, lido):
        consulta = 'INSERT OR IGNORE INTO livros (nome, autor, lido) VALUES' \
                   '(?, ?, ?)'
        self.cursor.execute(consulta, (nome, autor, lido))
        self.conn.commit()

    def editar(self, chave, novo_valor, id):
        consulta = f'UPDATE OR IGNORE livros SET {chave}=:{chave} WHERE id=:id'
        self.cursor.execute(consulta, {f'{chave}': f'{novo_valor}',
                                       'id': id})
        self.conn.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM livros WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM livros LIMIT 100')

        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, chave, valor):
        consulta = f'SELECT * FROM livros WHERE {chave} LIKE ?'
        #   Busca qualquer nome que ternha o VALOR no nome
        self.cursor.execute(consulta, (f'%{valor}%',))

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()
