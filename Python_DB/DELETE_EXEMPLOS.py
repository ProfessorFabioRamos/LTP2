import sqlite3
conexao = sqlite3.connect('empresa.db')
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS pedidos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    valor REAL CHECK(valor>0),
    status TEXT CHECK (status IN ('pendente','concluido','cancelado'))
)
""")

cursor.execute("""INSERT INTO pedidos (cliente_id,valor,status) VALUES
    (45, 45.33, 'concluido'),
    (45, 78.96, 'pendente'),
    (23, 56.25, 'pendente'),
    (23, 78.21, 'cancelado'),
    (14, 75.12, 'concluido'),
    (87, 12.33,'cancelado')
""")

# DELETA COM BASE NO ID
#cursor.execute("DELETE FROM pedidos WHERE id = 3")
# DELETA COM BASE EM UM CRITÉRIO
#cursor.execute("DELETE FROM pedidos WHERE status = 'cancelado'")
# DELETA COM BASE EM UM CRITÉRIO NUMÉRICO
#cursor.execute("DELETE FROM pedidos WHERE valor < 70")
# DELETA TODOS OS REGISTROS
#cursor.execute("DELETE FROM pedidos")
# RESETA O CONTATODOR DO AUTOINCREMETO PARA A TABELA "pedidos"
#cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'pedidos'")

conexao.commit()
#RESETA IDs
#cursor.execute("VACUUM;")
conexao.close()
