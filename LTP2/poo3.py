class Enemy:
    def __init__(self,name,hp,goldDrop,armor):
        self.name = name
        self.hp = hp
        self.goldDrop = goldDrop
        self.armor = armor
    def attack(self):
        print('Buuuyyyaaa')

class Boss(Enemy):
    def __init__(self, name, hp, goldDrop, armor, mana):
        super().__init__(name, hp, goldDrop, armor)
        self.mana = mana
    def attack(self):
        super().attack()
        print('Morra Seya!')

enemy1 = Enemy('Goblin', 50, 10, 0)
boss1 = Boss('Saga',1000,500,200,500)    
boss1.attack()   
boss1.super().attack() 