#AGREGAÇÃO
#Um objeto pode conter outro,
#mas ambos podem existir separadamente.
#Um Departamento pode ter vários Professores,
#mas se o Departamento deixar de existir,
#os Professores continuam existindo.
class Professor:
     def __init__(self,nome):
        self.nome = nome
        
class Departamento:
    def __init__(self,nome):
        self.nome = nome
        self.professores = [] #Lista vazia de professores(agregação)

    def adicionarProfessores(self,professor):
        self.professores.append(professor)
    
    def listarProfessores(self):
        for p in self.professores:
            print(f'Professor {p.nome} pertence ao departamento:{self.nome}')

#Instanciar objetos
departamento1 = Departamento('Departamento de TI')
professor1 = Professor('Ofugi')
professor2 = Professor('Huston')
# Adicionando professores ao departamento

departamento1.adicionarProfessores(professor1)
departamento1.adicionarProfessores(professor2)

# Exibindo informações
departamento1.listarProfessores()



