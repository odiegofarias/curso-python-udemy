import sqlite3


#   Conexão persistente = Salvar os dados
conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'nome TEXT,'
#                'peso REAL'
#                ')')

# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)',
#                ('Diego', 80.5))
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
#                {'nome': 'João', 'peso': 93.7})
# cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)',
#                {'id': None, 'nome': 'Daniel', 'peso': 113})
#
# conexao.commit()

#   Trocar usuário de dentro do banco de dados
# cursor.execute('UPDATE clientes SET nome=? WHERE id= ?',
#                ('Anderson', 2))

#   Apagar do banco de dados os ID 4
# cursor.execute('DELETE FROM clientes WHERE id=:id', {'id': 4})
# conexao.commit()
# cursor.execute('SELECT * FROM clientes')

#   Selecionar nome e peso ONDE peso é maior do que 90
cursor.execute('SELECT nome, peso FROM clientes WHERE peso > :peso',
               {'peso': 80.4})

for linha in cursor.fetchall():
    nome, peso = linha

    print(nome, peso)

cursor.close()
conexao.close()
