#Associação Simples
class Curso:
    def __init__(self,nome):
        self.nome = nome

class Aluno:
    def __init__(self, nome, curso):
        self.nome = nome
        self.curso = curso  #Associação Simples
    
    def info(self):
        print(f'Aluno:{self.nome} - Curso:{self.curso.nome}')

#Instanciando objetos
curso1 = Curso("Ciência da Computação")
aluno1 = Aluno('Bob',curso1)
aluno1.info()