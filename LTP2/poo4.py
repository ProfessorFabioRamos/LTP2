class Bateria:
    def __init__(self, voltagem, capacidade):
        self.voltagem = voltagem
        self.capacidade = capacidade
    def status(self):
        return 'Voltagem:', self.voltagem,", Capacidade:",self.capacidade
    
class Motor:
    def __init__(self,potencia, tensao):
        self.potencia = potencia
        self.tensao = tensao

    def status(self):
        return 'Pôtencia:',self.potencia,' Tensão:',self.tensao

class Robot(Bateria,Motor):
    def __init__(self, voltagem, capacidade,potencia, tensao):
        super().__init__(voltagem, capacidade)
        #Bateria.__init__(self,voltagem, capacidade)
        Motor.__init__(self,potencia, tensao)
    def status(self):
        print(Bateria.status(self))
        print(Motor.status(self))
        if self.voltagem == self.tensao:
            print('Status: OK')
        else:
            print('Tensao Incompativel')

bateria1 = Bateria(180,10000)
#print(bateria1.status())
motor1 = Motor(200,220)
#print(motor1.status())
robot1 = Robot(bateria1.voltagem,bateria1.capacidade,motor1.potencia,motor1.tensao)
robot1.status()