import sqlite3

conexao = sqlite3.connect("Empresa.db")
cursor = conexao.cursor()
conexao.execute("PRAGMA foreign_keys = ON")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS pedidos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER NOT NULL,
        valor REAL CHECK(valor>0),
        status TEXT CHECK(status IN ('pendente','concluido','cancelado')),
    FOREIGN KEY (cliente_id)
        REFERENCES clientes(id)
        ON DELETE CASCADE
    )
""")

def inserir_cliente(nome):
    cursor.execute("INSERT INTO clientes (nome) VALUES(?)",
                   (nome,))

def inserir_pedido(cliente_id,valor,status):
    cursor.execute("INSERT INTO pedidos (cliente_id,valor,status) VALUES(?,?,?)",
                   (cliente_id,valor,status))
    
def listar_clientes_com_pedidos():
    cursor.execute("""
        SELECT c.id, c.nome, p.id, p.valor, p.status
        FROM clientes AS c
        LEFT JOIN pedidos AS p ON p.cliente_id = c.id
        ORDER BY c.id
    """)
    resultados = cursor.fetchall()
    for i in  resultados:
        print(i)

def atualizar_cliente(cliente_id, novo_nome):
    cursor.execute("UPDATE clientes SET nome = ? WHERE id = ?",
        (novo_nome,cliente_id))   
    
def atualizar_pedido(pedido_id, novo_status):
    cursor.execute("UPDATE pedidos SET status = ? WHERE id = ?",
        (novo_status,pedido_id))   
    
def excluir_cliente(cliente_id):
    cursor.execute("DELETE FROM clientes WHERE id = ?",
                   (cliente_id,))

inserir_cliente('Pedro')
inserir_cliente('Maria')
inserir_pedido(1,200.21,'concluido')
inserir_pedido(1,50.42,'pendente')
inserir_pedido(2,147.25,'cancelado')
listar_clientes_com_pedidos()
atualizar_cliente(1,'Miguel')
atualizar_pedido(3,'concluido')
listar_clientes_com_pedidos()
excluir_cliente(1)
listar_clientes_com_pedidos()

conexao.commit()
conexao.close()

