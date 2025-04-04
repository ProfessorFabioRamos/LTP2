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

cursor.execute("""INSERT into pedidos (cliente_id,valor,status) VALUES
                (45, 45.33, 'concluido'),
                (45, 78.96, 'pendente'),
                (23, 56.25, 'pendente'),
                (23, 78.21, 'cancelado'),
                (14, 74.12, 'concluido'),
                (87, 12.33, 'cancelado')""")

#cursor.execute("DELETE FROM pedidos WHERE id = 3") # DELETA COM BASE NO ID
# DELETA COM BASE EM UM CRITÉRIO
#cursor.execute("DELETE FROM pedidos WHERE status = 'cancelado' ")
# DELETA COM BASE EM UM CRITÉRIO NUMERICO
#cursor.execute("DELETE FROM pedidos WHERE valor < 70 ")
#DELETA TODOS OS REGISTROS 
#cursor.execute("DELETE FROM pedidos")

conexao.commit()
# RESETA IDS
#cursor.execute("VACUUM;")
conexao.close()
