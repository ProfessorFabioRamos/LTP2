import sqlite3
conexao = sqlite3.connect('empresa.db')
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    email TEXT UNIQUE
)
""")

cursor.execute("INSERT INTO clientes (nome, idade, email) VALUES (?,?,?)",
            ('Alice', 30, 'alice@email.com'))
cursor.execute("INSERT INTO clientes (nome, idade, email) VALUES ('Alice', 30, 'alice@email.com.br')")
cursor.execute("INSERT INTO clientes VALUES (NULL, 'Alice', 30, 'alice@email.gov')")
cursor.execute("""INSERT INTO clientes (nome, idade, email) VALUES
    ('Alice', 30, 'alice@email.br'),
    ('Bob', 25, 'bob@email.com'),
    ('Eva', 19, 'eva@email.com')
""")

conexao.commit()
conexao.close()