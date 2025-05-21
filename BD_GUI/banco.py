import sqlite3
conexao = sqlite3.connect("produtos.bd")
cursor = conexao.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL
    )  
""")
conexao.commit()
# Inserir Produto
def inserir_produto(n, p):
    cursor.execute("INSERT INTO produtos (nome,preco) VALUES(?,?)",
                   (n, p))
# Listar produtos
def listar_produtos():
    cursor.execute("SELECT * FROM produtos")
    return cursor.fetchall()
#Excluir produto
def excluir_produto(id_produto):
    cursor.execute("DELETE FROM produtos WHERE id = ?",
                    (id_produto,))
    conexao.commit()
    return cursor.rowcount
# Fechar conexao
def fechar_conexao():
    conexao.close()
