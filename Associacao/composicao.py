#COMPOSIÇÃO
#Um objeto contém outro e não faz sentido existir sem ele.
#O Motor é criado dentro do Carro, e não pode existir sem ele.
class Motor():
    def __init__(self,tipo):
        self.tipo = tipo

class Carro:
    def __init__(self,marca,modelo,tipo_motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor(tipo_motor)  #Composição: o motor pertence 
                                        #exclusivamente ao carro
    def exibirInfo(self):
        print(f'Carro {self.marca},{self.modelo}, - Motor: {self.motor.tipo}')

#Instanciando objeto
carro1 = Carro('Lamborghini','Aventador','V12')
carro1.exibirInfo()
