from abc import ABC,abstractmethod

class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        #Método a ser implementado na subclasse
        pass

    @abstractmethod
    def calcular_perimetro(self):
        #Método a ser implementado na subclasse
        pass

class Retangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return self.base * self.altura
    def calcular_perimetro(self):
        return 2*(self.base + self.altura)
    def mostrar_calculos(self):
        print('Area:',self.calcular_area(),' Perimetro: ',self.calcular_perimetro())
#forma1 = Forma()     
retangulo1 = Retangulo(5,6)
print(retangulo1.mostrar_calculos())
