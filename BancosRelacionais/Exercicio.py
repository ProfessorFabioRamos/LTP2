import sqlite3

conexao = sqlite3.connect("Biblioteca.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS autor(
    id INTEGER PRIMARY KEY,
    nome TEXT
    )
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS livro(
    id INTEGER PRIMARY KEY,
    autor_id INTEGER,
    titulo TEXT,
    FOREIGN KEY (autor_id) REFERENCES autor(id)
    )
""")

# cursor.execute("INSERT INTO autor(nome) VALUES('George Orwell'),('Manuel Bandeira'),('Mário Quintana')")
# cursor.execute("""INSERT INTO livro(autor_id, titulo) VALUES
#                (1,'1984'),
#                (1,'A Revolução dos Bichos'),
#                (2,'Estrela da Manhã'),
#                (4,'Dagon')
# """)

# JOIN COM INNER -> REGISTROS QUE CASAM NAS DUAS TABELAS 
# cursor.execute("""
#     SELECT autor.nome, livro.titulo 
#     FROM livro
#     INNER JOIN autor ON livro.autor_id = autor.id
# """)

# JOIN COM LEFT -> TODOS OS REGISTROS DA TABELA DA ESQUERDA MESMO QUE NÃO CASEM COM A DIREITA
# cursor.execute("""
#     SELECT autor.nome, livro.titulo 
#     FROM livro
#     LEFT JOIN autor ON livro.autor_id = autor.id
# """)

# JOIN COM RIGHT -> TODOS OS REGISTROS DA TABELA DA DIREITA MESMO QUE NÃO CASEM COM A ESQUERDA
cursor.execute("""
    SELECT autor.nome, livro.titulo 
    FROM livro
    RIGHT JOIN autor ON livro.autor_id = autor.id
""")

for i in cursor.fetchall():
    print(i)

conexao.commit()
conexao.close()

#EXERCICIO INCLUIR TABELA BIBLIOTECA COM OS VALORES LIVRO_ID E GENERO
