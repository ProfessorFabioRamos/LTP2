#EXERCICIO INCLUIR TABELA GENERO COM OS VALORES LIVRO_ID E AUTOR_ID

import sqlite3

conexao = sqlite3.connect("Biblioteca.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS autores(
    id INTEGER PRIMARY KEY,
    nome TEXT
    )
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros(
    id INTEGER PRIMARY KEY,
    autor_id INTEGER,
    titulo TEXT,
    FOREIGN KEY (autor_id) REFERENCES autor(id)
    )
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS generos(
    id INTEGER PRIMARY KEY,
    livro_id INTEGER,
    genero_text TEXT,
    FOREIGN KEY (livro_id) REFERENCES livros(id)
    )
""")

cursor.execute("INSERT INTO autores(nome) VALUES('George Orwell'),('Manuel Bandeira'),('Mário Quintana')")
cursor.execute("""INSERT INTO livros(autor_id, titulo) VALUES
               (1,'1984'),
               (1,'A Revolução dos Bichos'),
               (2,'Estrela da Manhã'),
               (4,'Dagon')
""")
cursor.execute("""INSERT INTO generos(livro_id, genero_text) VALUES
               (1,'Ficção Científica'),
               (2,'Fábula'),
               (3,'Suspense'),
               (4,'Terror'),
               (5,'Aventura')
""")

# JOIN COM INER -> REGISTROS QUE CASAM NAS 3 TABELAS
cursor.execute("""
    SELECT
    l.titulo    AS livro,
    a.nome      AS autor,
    g.genero_text    AS genero
    FROM livros AS l
        INNER JOIN autores AS a
            ON l.autor_id = a.id
        INNER JOIN generos AS g
            ON g.livro_id = l.id
""")

for livro,autor,genero in cursor.fetchall():
    print(f"{livro} de {autor} do genero: {genero}")

conexao.commit()
conexao.close()

