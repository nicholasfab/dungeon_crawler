import random
import time

mpg1 = 0
mpg2 = 0
x = 0
y = 0
health = 0

roomsx = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
roomsy = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

rooms = []
roomstype = []

index = 0

trapdam = 0
floor = 1

treasure = ["filler",
"red potion",
"blue potion",
"rusty sword",
"rusty dagger",
"wooden shield",
            
"glowing red potion",
"glowing blue potion",
"knight's sword",
"coward's blade",
"leather cap",

"glowing green potion",
"gold potion",
"Sickle of Lost Requiem",
"vial of blessed water",
"chainmail armor",

"goldenleaf tea",
"glowing gold potion"
"Forbidden Tome",
"Argonaut's Spear",
"Cursed Blade",
"gorgonskin armor",

"Elixir of Life vial",
"Sorcerer's Scroll",
"Sword of Heroic Desire",
"Monkey's Paw",
"Ancient Magus' Robes",

"Potion of Regeneration",
"Grimoire",
"Magus' Staff",
"Holy Hand Grenade",
"Dragonskin Armor"]

inventory = []
visited = False

weapon = False

def start():
    global health
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
    global visited

    inventory = []
    floor = 0
    
    def floorstart():
        global health
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
        global visited
        global weapon

        weapon = False
        
        mpg1 = random.randint(-5,5)
        mpg2 = random.randint(-5,5)
        x = 0
        y = 0
        health = 100

        trapdam = 5

        visited = True

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

        #battle system
        def battle():
            global health
            global inventory
            global weapon

            x = input("[Choose an action: Attack(a), Defend(d), Item(i)]")

            if x == str("a"):
                x = input("[Choose your attack: ",  "]")
            if x == str("d"):
                
            if x == str("i"):
                

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
            print("Primarily, a few things catch your eye: a ", t1, ", a ", t2, ", and a", t3, ".")

            if len(inventory) == 6:
                print("Unfortunately, your inventory is already full!")
                d = input("Would you like to remove something from your inventory to make space? y/n")

                if d == "y":
                    e = input("What do you want to leave behind? 1/2/3/4/5/6")

                    if e == "1":
                        print("You leave your", inventory[1], ".")
                    if e == "2":
                        print("You leave your", inventory[2], ".")
                    if e == "3":
                        print("You leave your", inventory[3], ".")
                    if e == "4":
                        print("You leave your", inventory[4], ".")
                    if e == "5":
                        print("You leave your", inventory[5], ".")
                    if e == "6":
                        print("You leave your", inventory[6], ".")

            y = input("Which do you choose? 1/2/3/n")

            if y == "1":
                print("After some thought, you settle on the", t1, "and move on.")
                inventory.append(t1)
                input("")
            if y == "2":
                print("After some thought, you settle on the", t2, "and move on.")
                inventory.append(t2)            
                input("")
            if y == "3":
                print("After some thought, you settle on the", t3, "and move on.")
                inventory.append(t3)
                input("")
            if y == "n":
                input("After some thought. you decide that none of it is necessary and move on.")

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
                print("visit check")
                print(visited)
                if visited == False:
                    print("visited check fail")
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
                print("visited true")
                pick1 = input('''                        -Go forward (1)
                        -Go right (2)
                        -Go back (3)
                        -Go left(4)
                        -Check your inventory (i)
                        -Drop an item (d)


                            ''')
                #use an item will be here for health potions
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
                if pick1 == "d":
                    inventory_check()
                    g = input("Drop this item: ")
                    for i in inventory:
                        h = inventory.index(i)
                        if h == (int(g)-1):
                            inventory.remove(i)
                            print("You dropped your", i, ".")
                    step()
        def inventory_check():
            print("Current Health:", health)
            print("Inventory: ", len(inventory), "/6")
            if len(inventory) == 6:
                print("INVENTORY CURRENTLY FULL!")
            print(inventory)
                
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
