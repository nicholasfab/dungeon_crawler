import time
import random

weapon_list = ["sword", "bow", "rock"]
item_list = ["potion", "arrow", "stick"]

class item:
    def __init__(self, name):
        self.name = name

class weapon(item):
    def __init__(self, name, damage, durability):
        super().__init__(name, "weapon")
        self.damage = damage
        self.durability = durability

    def use(self):
        self.durability -= 1
        if self.durability =< 0:
            print(self.name, "was destroyed!")
        else:
            print(self.durability, "uses left.")

class armor(item):
    def __init__(self, name, protect, durability):
        super().__init__(name, "armor")
        self.protect = protect
        self.durability = durability

    def use(self):
        self.durability -= 1
        if self.durability =< 0:
            print(self.name, "was destroyed!")
        else:
            print(self.durability, "uses left.")
            
class spell(item):
    def __init__(self, name, damage, mana):
        super().__init__(name, "potion")
        self.damage = damage
        self.mana = mana

    def use(self):
        self.durability -= 1
        if self.durability =< 0:
            print("Out of mana!")
        else:
            print(self.mana, "mana left.")
