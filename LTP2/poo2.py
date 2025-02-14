class Player:
    def __init__(self,nome,hp,mana):
        self.__name = nome
        self.__hp = hp
        self.__mana = mana
        self.__armor = 0

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,novoNome):
        if novoNome != '':
            self.__name = novoNome
    
    def getHP(self):
        return self.__hp

    def setHP(self, novoHP):
        if novoHP > 0:
            self.__hp = novoHP

player1 = Player("Aragorn",100,10)
player1.name = "Legolas"    #player1.name é um SETTER
print(player1.name)         #player1.name é um GETTER    
print(player1.getHP())