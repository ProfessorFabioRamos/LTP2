#Agregação
class Professor:
    def __init__(self,nome):
        self.nome = nome

class Departamento:
    def __init__(self,nome):
        self.nome = nome
        self.professores = []  #Lista vazia de professores(agregação)

    def adicionarProfessor(self,professor):
        self.professores.append(professor)
    
    def listarProfessores(self):
        for p in self.professores:
            print(f'Professor: {p.nome} pertence ao departamento: {self.nome}')

#Instanciando objetos
dep_ti = Departamento('Cursos de TI')
prof1 = Professor('Ofugi')
prof2 = Professor('Flávio')

# Adicionando professores ao departamento
dep_ti.adicionarProfessor(prof1)
dep_ti.adicionarProfessor(prof2)

# Exibindo informações
dep_ti.listarProfessores()
