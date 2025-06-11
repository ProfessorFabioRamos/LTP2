import sqlite3
conexao = sqlite3.connect("inventario.db")
cursor = conexao.cursor()
cursor.execute('''
  CREATE TABLE IF NOT EXISTS itens (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome TEXT NOT NULL,
  quantidade INTEGER NOT NULL
  )
''')
conexao.commit()
def inserir_item(nome, quantidade):
  cursor.execute("INSERT INTO itens (nome, quantidade) VALUES (?, ?)", (nome,
  quantidade))
  conexao.commit()
def listar_itens():
  cursor.execute("SELECT * FROM itens")
  return cursor.fetchall()
