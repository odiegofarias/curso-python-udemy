import pymysql.cursors
from contextlib import contextmanager

#   CRUD - Create, Read, Update, Delete


@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        yield conexao
    finally:
        conexao.close()


#   Insere 1 registro na BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES' \
#               '(%s, %s, %s, %s)'
#         cursor.execute(sql, ('Diego', 'Farias', 27, 82))
#         conexao.commit()


#   Insere vários registros na BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES' \
#               '(%s, %s, %s, %s)'
#         dados = [
#             ('MURIEL', 'SOUZA', '19', '55'),
#             ('ROSE', 'SOUZA', '19', '55'),
#             ('JOSÉ', 'SOUZA', '19', '55'),
#         ]
#
#         cursor.executemany(sql, dados)
#         conexao.commit()


#   Deleta 1 registro da BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id = %s'
#         cursor.execute(sql, (6,))
#         conexao.commit()


#   Deleta quantidade determinada de REGISTROS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
#         cursor.execute(sql, (7, 8, 9))
#         conexao.commit()


#   Deleta registros entre um range
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
#         cursor.execute(sql, (10, 12))
#         conexao.commit()


#   Atualiza 1 registro na base de dados
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
#         cursor.execute(sql, ('JOANA', 5))
#         conexao.commit()


#   Seleciona os dados da BASE DE DADOS
with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes LIMIT 100')
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)


