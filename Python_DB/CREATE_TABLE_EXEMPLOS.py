import sqlite3

conexao = sqlite3.connect('empresa.db')
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS pedidos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    valor REAL CHECK(valor>0),
    status TEXT CHECK(status IN ('pendente','concluido','cancelado')),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)           
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS log_acessos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL,
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)           
""")

def inserir_pedido(cliente_id, valor, status):
    try:
        cursor.execute("INSERT INTO pedidos (cliente_id, valor, status) VALUES(?,?,?)",
        (cliente_id, valor, status))
        conexao.commit()
        print(f"Pedido inserido com sucesso! ID:{cursor.lastrowid} ")
    except sqlite3.IntegrityError as e:
        print(f"Erro ao inserir pedido: {e}")
    #finally:
        #conexao.close()

#inserir_pedido(1,25.99,'pendente')            
#inserir_pedido(1,-50.54,'pendente')            
#inserir_pedido(1,100.98,'caro')            

def inserir_log(user):
    cursor.execute("INSERT INTO log_acessos (usuario) VALUES(?)",(user,))

inserir_log("Vinicius")

conexao.commit()
conexao.close()
