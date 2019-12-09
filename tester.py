import time
import random

        
class item:
    def __init__(self, name):
        self.name = name

class weapon(item):
    def __init__(self, name, durability, damage):
        super().__init__("weapon")
        self.durability = durability
        self.damage = damage

    def use(self):
        self.durability -= 1
        if self.durability <= 0:
            print(self.name, "was destroyed!")
        else:
            print(self.durability, "uses left.")
            
class spell(item):
    def __init__(self, name, mana, damage):
        super().__init__("spell")
        self.damage = damage
        self.mana = mana

    def use(self):
        self.mana -= 1
        if self.mana <= 0:
            print("Not enough mana!")
        else:
            print(self.mana, "mana left.")
