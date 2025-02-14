class Item:
    def __init__(self,name,value,rarity):
        self.name = name        #publico
        self._value = value     #private fraco
        self.__rarity = rarity  #private forte

    def showInfo(self):
        print(f'Nome do item:{self.name},\nValor do item:{self._value},\nRaridade do item:{self.__rarity}')

item1 = Item("Sword",200,'common')
#print(item1.__rarity)
#item1.showInfo()
print(item1._Item__rarity)
