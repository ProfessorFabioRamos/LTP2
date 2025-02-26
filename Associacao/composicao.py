#Composição
class Motor:
    def __init__(self,tipo):
        self.tipo

class Carro:
    def __init__(self,marca,modelo,tipo_motor):
        self.marca = marca
        self.modelo = modelo
        self.tipo_motor = Motor(tipo_motor) #Composição: o motor pertence
                                            #exlusivamete ao carro
    def exibirInfo(self):
        print(f'Carro {self.marca} {self.modelo} - Motor {self.motor.tipo}')

#Instanciação do Objeto
carro1 = Carro('Lamborghini','Aventador', 'V12')
carro1.exibirInfo()
