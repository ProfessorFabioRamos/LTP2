import sqlite3
conexao = sqlite3.connect("Empresa.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes(
    id INTEGER PRIMARY KEY,
    nome TEXT
    )
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS pedidos(
    id INTEGER PRIMARY KEY,
    cliente_id INTEGER,
    valor REAL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
    )
""")

# cursor.execute("INSERT INTO clientes(nome) VALUES('Eddy'),('Martha'),('Mark')")
# cursor.execute("""INSERT INTO pedidos(cliente_id, valor) VALUES
#                (1,200.50),
#                (1,150.00),
#                (2,300.00),
#                (4,40.50)
# """)

# JOIN COM INNER -> REGISTROS QUE CASAM NAS DUAS TABELAS
# cursor.execute("""
#     SELECT clientes.nome, pedidos.valor
#     FROM pedidos
#     INNER JOIN clientes ON pedidos.cliente_id = clientes.id
# """)

# JOIN COM LEFT -> TODOS OS REGISTROS DA TABELA DA ESQUERDA MESMO 
# QUE NÃO TENHAM VALOR NA DIREITA
# cursor.execute("""
#     SELECT clientes.nome, pedidos.valor
#     FROM pedidos
#     LEFT JOIN clientes ON pedidos.cliente_id = clientes.id
# """)

# JOIN COM RIGHT -> TODOS OS REGISTROS DA TABELA DA DIREITA MESMO 
# QUE NÃO TENHAM VALOR NA ESQUERDA
cursor.execute("""
    SELECT clientes.nome, pedidos.valor
    FROM pedidos
    RIGHT JOIN clientes ON pedidos.cliente_id = clientes.id
""")

for i in cursor.fetchall():
    print(i)

conexao.commit()
conexao.close()
