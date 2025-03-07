import sqlite3

# Conectar ao banco de dados(cria o arquivo se não existir)
conexao = sqlite3.connect('empresa.db')
cursor = conexao.cursor()

# Criando a tabela
cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        idade INTEGER
    )
""")
# Inserindo um cliente
cursor.execute("INSERT INTO clientes (nome,email,idade) VALUES(?,?,?)",
               ("Carlos Abreu","carlos@email.com", 40))

conexao.commit()
conexao.close()