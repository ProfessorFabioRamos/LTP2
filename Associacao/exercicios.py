# 1 e 2 Associação Simples: Livro -> Autor
class Autor:
    def __init__(self, nome):
        self.nome = nome

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor  # Associação simples

    def exibir_info(self):
        print(f"Livro: {self.titulo} - Autor: {self.autor.nome}")

#3 - Agregação
class Biblioteca:
    def __init__(self,nome):
        self.nome = nome
        self.livros = [] #Agregação
    
    def adicionar_livros(self,livro):
        self.livros.append(livro)

    def listar_livros(self):
        for l in self.livros:
            l.exibir_info()
# 4 -Composição
class Pagina:
    def __init__(self,numero, nome_livro, nome_autor):
        self.numero = numero
        self.nome_autor = nome_autor
        self.livro = Livro(nome_livro,nome_autor)

    def info_pagina(self):
        print(f"Pagina: {self.numero} - Livro: {self.livro.titulo}")

# Instanciando objetos
autor1 = Autor("Machado de Assis")
livro1 = Livro("Dom Casmurro", autor1)
livro1.exibir_info()
biblioteca1 = Biblioteca("Biblioteca de Brasília")
biblioteca1.adicionar_livros(livro1)
biblioteca1.listar_livros()
pagina1 = Pagina(1,"O Alienista",autor1.nome)
pagina1.info_pagina()
