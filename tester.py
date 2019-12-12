import random
import time

mpg1 = 0
mpg2 = 0
x = 0
y = 0
health = 0
mana = 0

roomsx = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
roomsy = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

rooms = []
roomstype = []

index = 0

trapdam = 0
floor = 1


inventory = []
treasure = []
visited = False

weapon = False

def start():
    global health
    global mana
    global mpg1
    global mpg2
    global x
    global y
    global health
    global roomsx
    global roomsy
    global rooms
    global index
    global roomstype
    global trapdam
    global floor
    global inventory
    global treasure
    global visited

    inventory = []
    treasure = []
    floor = 0
    
    def floorstart():
        global health
        global mana
        global mpg1
        global mpg2
        global x
        global y
        global health
        global roomsx
        global roomsy
        global rooms
        global index
        global roomstype
        global trapdam
        global floor
        global inventory
        global treasure
        global visited
        global weapon

        weapon = False
        
        mpg1 = random.randint(-5,5)
        mpg2 = random.randint(-5,5)
        x = 0
        y = 0
        health = 100
        mana = 100

        trapdam = 5

        visited = True

        #inventory system
        class weapon():
            def __init__(self, name, durab, damage):
                self.name = name
                self.durab = durab
                self.damage = damage

            def use(self):
                self.durab -= 1
                if self.durab <= 0:
                    print(self.name, "was destroyed!")
                else:
                    print("Used", self.name, "!")
                    print(self.durab, "uses left.")

        class armor():
            def __init__(self, name, durab, block):
                self.name = name
                self.durab = durab
                self.block = block

            def use(self):
                self.durab -= 1
                if self.durab <= 0:
                    print(self.name, "was destroyed!")
                else:
                    print(self.durab, "hits left.")

        class bruh():
            def __init__(self, name):
                self.name = name

            def use(self):
                print(self.name)

        class potion():
            def __init__(self, name, health, mana, boost, istype):
                self.name = name
                self.health = health
                self.mana = mana
                self.boost = boost
                self.istype = istype
                self.durab = 1

            def use(self):
                
                if self.durab <= 0:
                    inventory.pop(inventory.index(self))
                    
                    print(self.name, "was used up!")
                    
                else:
                    self.durab -= 1
                    print("Used", self.name, "!")
                    
                    if self.istype == "mana":
                        self.mana += self.boost
                        print("Gained", self.boost, "mana!")
                        print("Mana now", self.mana)
                        
                    if self.istype == "health":
                        self.health += self.boost
                        print("Gained ", self.boost, "health!")
                        print("Health now", self.health)

        inventory = [weapon("punch", 100000, 1)]
            
        def pop_item():
            global inventory
            global treasure

            print("Inventory: ", inventory)
            pick = int(input("pick one: "))
            
            inventory.pop(pick)
            print(inventory)

        #items list
            
        treasure = ["filler",
        potion("red potion", health, mana, 5, "health"),
        potion("blue potion", health, mana, 5, "mana"),
        weapon("rusty sword", 10, 2),
        weapon("rusty dagger", 5, 2),
        armor("wooden shield", 1, 1),
                    
        potion("glowing red potion", health, mana, 8, "health"),
        potion("glowing blue potion", health, mana, 8, "mana"),
        weapon("knight's sword", 10, 5),
        weapon("coward's blade", 10, 3),
        armor("leather cap", 1, 1),

        potion("glowing green potion", health, mana, 10, "health"),
        potion("gold potion", health, mana, 10, "mana"),
        weapon("Sickle of Lost Requiem", 15, 8),
        potion("vial of blessed water", health, mana, 15, "health"),
        armor("chainmail armor", 1, 1),

        potion("goldenleaf tea", health, mana, 15, "health"),
        potion("glowing gold potion", health, mana, 15, "mana"),
        bruh("Forbidden Tome"),
        weapon("Argonaut's Spear", 10, 15),
        weapon("Cursed Blade", 15, 13),
        armor("gorgonskin armor", 1, 1),

        potion("Elixir of Life vial", health, mana, 25, "health"),
        bruh("Sorcerer's Scroll"),
        weapon("Sword of Heroic Desire", 15, 25),
        bruh("Monkey's Paw"),
        armor("Ancient Magus' Robes", 1, 1),

        potion("Potion of Regeneration", health, mana, 50, "health"),
        bruh("Grimoire"),
        weapon("Magus' Staff", 25, 30),
        weapon("Holy Hand Grenade", 1, 40),
        armor("Dragonskin Armor", 1, 1)]

        #room assignment

        roomsx = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        roomsy = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

        rooms = []
        roomstype = []

        index = 61

        for i in roomsx:
            for a in roomsy:
                rooms.append([i, a])

        for i in rooms:
            z = random.randint(1, 3)
            if z == 1:
                b = str("trap")
            if z == 2:
                b = str("loot")
            if z == 3:
                b = str("monster")    
            roomstype.append(b)
            
        print(mpg1, mpg2)

        if floor == 0:
            input("You awaken in a cold, dark room.")
            input("Your face is pressed against rough hewn stone. A damp lichen gives off an earthy scent nearby.")
            input("Lifting yourself with a slight grunt of effort, you try to take in your surroundings in the dim light.")
        else:
            input("Your feet hit the stone beneath you, echoeing into the halls of the Dungeon.")
        input("It's dark, but not quite pitch-black. You can just barely make out the outline of an old, wooden door on each wall.")
        input("As far as you can tell, all four doors are identical, so which one should you choose?")

        def endscene():
            print("As the air changes once more, you feel that something is different, this time. A familiar presence fills the room.")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print("Indeed, the disembodied voice from eariler has returned...")
            input("Noticing your awareness, it begins to speak once more:")
            print("After a long and arduous journey, you managed to survive the Dungeon! Along the way, whilst battling great evils, you collected treasures and arcane knowledge beyond the wildest dreams of man and have lived to tell the tale! Few other heroes have been able to complete the 100 floors of the dungeon.")
            x = input("Among them, you surely stand as a living legend. What is your name, hero?")
            print("Well, we honor you, ", x, " for your strength and bravery! Now go! Other legends about your deeds surely wait to be told!")
            input("[THE END]")
            return

        def deathscene():
            global health
            if health <= 0:
                input("The world suddenly cuts to black.")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print(".")
                time.sleep(1)
                input("A deep, booming voice bellows inside your head:")

                x = input("It seems that your health has reached 0! I regret to inform you that you are dead. I can revive you, if you so choose, but I cannot return you to your position in the Dungeon. You must begin again. Do you still wish to continue? y/n ")

                if x == str("y"):
                    input("What great spirit! Onwards!")
                    start()
                else:
                    input("Very well. Farewell, adventurer!")
                    return
                     

        def new_lvl():
            global floor
            
            input("Before you, a latch protrudes from the cobblestones.")
            input("You brush off the layers of dust and grime to find a long-forgotten trapdoor.")
            x = input("Do you enter? y/n ")

            if x == str("y"):
                #load new level
                input("The air gets a little cooler as you descend into the darkness...")
                floor += 1
                print("[REACHED DUNGEON FLOOR", floor,"!]")
                input("")
                floorstart()
            else:
                input("You decide there is still more to be found on the level of the dungeon you are already in.")
                step()
                

        #room types
        def trap():
            global trapdam
            global floor
            global health

            if floor <= 5:
                trapdam = 5
            if floor <= 10 and floor > 5:
                trapdam = 10
            if floor <= 20 and floor > 10:
                trapdam = 15
            if floor <= 40 and floor > 20:
                trapdam = 20
            if floor <= 80 and floor > 40:
                trapdam = 25
            if floor <= 100 and floor > 80:
                trapdam = 30

            x = random.randint(0,3)
            z = random.randint(1, int(trapdam))

            traps = ["a giant axe swings down from the ceiling, the blade rusted with the blood of its last victim.",
                     "the ground opens up before you, revealing a deep pit. Far below, the hissing of snakes can be heard.",
                     "you spot a old chest sitting in the corner of the room. Covered in cobwebs, it lures you with the promise of treasure and arcane secrets.",
                     "the door shuts behind you and the whole dungeon seems to rumble as the stone walls begin to slide closer."]
            input("Pushing open the heavy door, you peer into the room.")
            print("Suddenly,", traps[x])
            input("...")

            if x == 2:
                input("Carefully resting your hands on the lid, you attempt to open the trunk. Much to your surprise, the chest lunges towards you and opens its wood-like mouth wide.")
            
            input("Match the number to surive! Your accuracy determines the damage dealt.")
            
            print("On Floor", floor, ", the max number is", trapdam, ".")
            y = input("Choose your number: ")
            h = abs(z - int(y))
            health -= h
            
            print("You took", h, "damage!")
            print("Health: ", health)
            
        def loot():
            global floor
            global treasure
            global inventory
            global treasure

            if floor <= 5:
                a = 1
                x = 5
            if floor <= 10 and floor > 5:
                a = 1
                x = 10
            if floor <= 20 and floor > 10:
                a = 5
                x = 15
            if floor <= 40 and floor > 20:
                a = 10
                x = 21
            if floor <= 80 and floor > 40:
                a = 15
                x = 26
            if floor <= 100 and floor > 80:
                a = 15
                x = 31

            t1 = treasure[int(random.randint(a, x))]
            t2 = treasure[int(random.randint(a, x))]
            t3 = treasure[int(random.randint(a, x))]
            
            input("Pushing open the heavy door, you peer into the room.")
            print("Suddenly, you spot a old chest sitting in the corner of the room. Covered in cobwebs, it lures you with the promise of treasure and arcane secrets.")
            input("...")
            input("You carefully lift the lid of the ancient trunk, revealing a great number of trinkets, some more useful than others.")
            print("Primarily, a few things catch your eye: a ", t1.name, ", a ", t2.name, ", and a", t3.name, ".")

            pick = int(input("Pick an item - 0, 1, 2:"))
            if pick == 0:
                picked = t1
            if pick == 1:
                picked = t2
            if pick == 2:
                picked = t3
            
            inventory.append(picked)
            print("Added", picked.name, "!")
      

        def monster():
            global floor
            global health
            global weapon
            
            input("Pushing open the heavy door, you peer into the room.")
            input("...")
            input("Before you, a dark shape is huddled in the corner of the room. A chewing sound echoes throughout the space.")
            input("The creature turns it's misshappen head towards you and grins, its white lips stretching into a gruesome shape.")

            if weapon == True:
                input("You tighten your grip on your weapon and prepare for a fight.")
                battle()
            else:    
                input("You clench your fists and prepare for a fight.")
                battle()
#left off here/ battle system
        def battle():
            battle_start = False

            if battle_start = False:
                print("The battle begins!")
                battle_start = True
            inventory_check()
            pick = int(input("Which item do you want to use?:"))
            if pick > len(inventory):
                print("Pick something in your inventory!")
                battle()
            else:
                inventory[pick].use()
                step()
                
        #steps
        def step():
            global x
            global y
            global mpg1
            global mpg2
            global roomsx
            global roomsy
            global rooms
            global index
            global roomstype
            global visited

            if x == mpg1:
                if y == mpg2:
                    new_lvl()
            
            else:
                print(visited)
                if visited == False:
                    for i in roomsx:
                        for a in roomsy:
                            if i == x and a == y:
                                print(roomstype[index])

                                if roomstype[index] == "trap":
                                    trap()
                                if roomstype[index] == "loot":
                                    loot()
                                if roomstype[index] == "monster":
                                    monster()
                visited = True
                pick1 = input('''                        -Go forward (1)
                        -Go right (2)
                        -Go back (3)
                        -Go left(4)
                        -Check your inventory (i)
                        -Drop an item (d)
                        -Use an item (u)


                            ''')
                if pick1 == "1":
                    up_check()
                if pick1 == "2":
                    right_check()
                if pick1 == "3":
                    down_check()
                if pick1 == "4":
                    left_check()
                if pick1 == "i":
                    inventory_check()
                    step()
                if pick1 == "u":
                    inventory_check()
                    pick = int(input("Use which item?:"))
                    if pick > len(inventory):
                        print("Pick something in your inventory!")
                        step()
                    else:
                        inventory[pick].use()
                        step()
                if pick1 == "d":
                    inventory_check()
                    pick = int(input("Drop which item?:"))
                    if pick == 0 or pick > len(inventory):
                        print("You can't drop that!")
                        step()
                    else:
                        inventory.pop(pick)
                        print("Dropped item!")    
                        step()
                    
                else:
                    print("Make a decision, adventurer!")
                    step()
                    
        def inventory_check():
            print("Current Health:", health)
            print("Inventory: ", len(inventory), "/6")
            if len(inventory) == 6:
                print("INVENTORY CURRENTLY FULL!")
            for i in inventory:
                print(i.name)
                
        def up_check():
            global x
            global y
            global index
            global visited

            if (y+1) > 5:
                print("A solid wall of rock blocks your path. It seems you have reached the wall of the dungeon.")
                step()
            else:
                y += 1
                index -= 11
                visited = False
                print("visited false")
                step()

        def right_check():
            global x
            global y
            global index
            global visited

            if (x+1) > 5:
                print("A solid wall of rock blocks your path. It seems you have reached the wall of the dungeon.")
                step()
            else:
                x += 1
                index += 1
                visited = False
                step()

        def down_check():
            global x
            global y
            global index
            global visited

            if (y-1) < -5:
                print("A solid wall of rock blocks your path. It seems you have reached the wall of the dungeon.")
                step()
            else:
                y -= 1
                index += 11
                visited = False
                step()

        def left_check():
            global x
            global y
            global index
            global visited

            if (x-1) < -5:
                print("A solid wall of rock blocks your path. It seems you have reached the wall of the dungeon.")
                step()
            else:
                x -= 1
                index -=1
                visited = False
                step()
        step()
    floorstart()
start()
