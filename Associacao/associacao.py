#ASSOCIAÇÃO SIMPLES
#Quando uma classe usa outra sem estabelecer 
#uma dependência forte.
#O Aluno contém uma referência ao Curso,
#mas o Curso pode existir sem o Aluno
class Curso:
    def __init__(self,nome):
        self.nome = nome

class Aluno:
    def __init__(self,nome,curso):
        self.nome = nome
        self.curso = curso      #ASSOCIAÇÃO SIMPLES  

    def exibirInfo(self):
        print(f'Aluno:{self.nome} - Curso: {self.curso.nome}')

#Instanciando Objetos
curso1 = Curso('Ciência da Computação')
aluno1 = Aluno('Bob',curso1)
aluno1.exibirInfo()
