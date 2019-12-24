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
level = 0

inventory = []
treasure = []
spells = []
player_spells = []
visited = False

weapon = False

enemy_health = 0
enemy_damage = 0

deaths = 0

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
    global level
    global spells
    global player_spells
    global deaths

    inventory = []
    treasure = []
    spells = []
    player_spells = []
    floor = 0
    level = 0
    health = 10
    mana = 5
    deaths = 0
    
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
        global level

        weapon = False
        
        mpg1 = random.randint(-5,5)
        mpg2 = random.randint(-5,5)

        x = 0
        y = 0

        trapdam = 5

        visited = True
        level = 0

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
                    inventory.pop(inventory.index(self))
                else:
                    print("Used", self.name, "!")
                    print(self.durab, "uses left.")

        class magic():
            global mana
            def __init__(self, name, damage, heal, typeis, cost):
                self.name = name
                self.damage = damage
                self.heal = heal
                self.typeis = typeis
                self.cost = cost
                
            def use(self):
                global mana
                if mana >= self.cost:
                    print("Conjured", self.name, "!")
                    mana -= self.cost
                    print(mana, "mana remaining!")
                else:
                    print("Not enough mana for this spell!")

        class special():
            def __init__(self, name, level):
                self.name = name
                self.level = level

            def use(self):
                x = random.randint(1, 3)
                if self.level == 1:
                    player_spells.append(spells_1[x])
                if self.level == 2:
                    player_spells.append(spells_2[x])
                if self.level == 3:
                    player_spells.append(spells_3[x])
                    
                print("You read the", self.name, "!")
                inventory.pop(inventory.index(self))
                                   
        class potion():
            global health
            
            def __init__(self, name, boost, istype):
                self.name = name
                self.boost = boost
                self.istype = istype
                self.durab = 1

            def use(self):
                global health
                global mana

                print("Used", self.name, "!")
                
                if self.istype == "mana":
                    mana += self.boost
                    print("Gained", self.boost, "mana!")
                    print("Mana now", mana)
                    
                if self.istype == "health":
                    health += self.boost
                    print("Gained ", self.boost, "health!")
                    print("Health now", health)

                print(self.name, "was used up!")
                inventory.pop(inventory.index(self))

        class enemy():
            def __init__(self, name, intros, attacks, deaths):
                self.name = name
                self.intros = intros
                self.attacks = attacks
                self.deaths = deaths
                
                
        inventory = [weapon("punch", 100000, 1), "magic"]
        player_spells = [magic("Heal", 0, 2, "heal", 5)]

        #magic list
        spells_1 = [magic("Firebolt", 1, 0, "attack", 5),
        magic("Abracadabra", 2, 0, "attack", 5),
        magic("Shock", 3, 0, "attack", 5)]

        spells_2 = [magic("Fireball", 1, 0, "attack", 10),
        magic("Turn Undead", 2, 0, "attack", 10),
        magic("God Blow", 3, 0, "attack", 10)]

        spells_3 = [magic("Ifrit's Curse", 1, 0, "attack", 20),
        magic("Vow of Caine", 2, 0, "attack", 20),
        magic("Edge of Oblivion", 3, 0, "attack", 20)]

        #items list
        treasure = ["filler",
        potion("red potion", 1, "health"),
        potion("blue potion", 1, "mana"),
        weapon("rusty sword", 10, 2),
        weapon("rusty dagger", 5, 2),
                    
        potion("glowing red potion", 2, "health"),
        potion("glowing blue potion", 2, "mana"),
        weapon("knight's sword", 10, 5),
        weapon("coward's blade", 10, 3),

        potion("glowing green potion", 4, "health"),
        potion("gold potion", 4, "mana"),
        weapon("Sickle of Lost Requiem", 15, 8),
        potion("vial of blessed water", 6, "health"),

        potion("goldenleaf tea", 8, "health"),
        potion("glowing gold potion", 8, "mana"),
        special("Forbidden Tome", 1),
        weapon("Argonaut's Spear", 10, 15),
        weapon("Cursed Blade", 15, 13),

        potion("Elixir of Life vial", 16, "health"),
        special("Sorcerer's Scroll", 2),
        weapon("Sword of Heroic Desire", 15, 25),
        potion("Bottle of Aether", 16, "mana"),

        potion("Potion of Regeneration", 32, "health"),
        special("Grimoire", 3),
        weapon("Magus' Staff", 25, 30),
        weapon("Holy Hand Grenade", 1, 40)]

        #enemies
        enemies = [enemy("scorpion"), enemy("snake"), enemy("goblin"), enemy("ogre"), enemy("chimera"), enemy("mummy"), enemy("cultist"), enemy("demon"), enemy("dragon"), enemy("lizard"), enemy("mountain"), enemy("vampire")]

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
            
        if floor == 0:
            input("[BEGINNING OF PART 1: ENTERING THE TOMB]")
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
            x = input("Among them, you surely stand as a living legend. What is your name, hero?  ")
            print("Well, we honor you, ", x, " for your strength and bravery! Now go! Other legends about your deeds surely wait to be told!")
            input("[THE END]")
            return

        def deathscene():
            global deaths
            
            input("The world suddenly cuts to black.")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            input("A deep, booming voice bellows inside your head:")

            x = input("It seems that your health has reached 0! I regret to inform you that you are dead. I can revive you, if you so choose, but I cannot return you to your position in the Dungeon. You must begin again. Do you still wish to continue? [y/n] ")

            if x == str("y"):
                input("What great spirit! Onwards!")
                deaths = 0
                start()
            if x == str("n"):
                input("Very well. Farewell, adventurer!")
                return
            else:
                deaths += 1
                if deaths == 1:
                    print("")
                    input("That's not an answer, let's try that again.")
                    print("")
                    deathscene()
                if deaths == 2:
                    print("")
                    input("If you're confused right now, it would appear that you aren't pressing 'y' or 'n.'")
                    input("Hopefully I've cleared up your little mishap. Off you go now.")
                    print("")
                    deathscene()
                if deaths == 3:
                    print("")
                    input("Well, which will it be? Yes or no? Pick one!")
                    print("")
                    deathscene()
                if deaths == 4:
                    input("This is just getting ridiculuous. I don't have all the time in the- well, actually.. Look, you know what I mean.")
                    deathscene()
                if deaths >= 5:
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    input("You again? I can't believe you. You call yourself an adventurer, and yet you spend all your time in Limbo?")
                    input("Fine, fine. You clearly don't want to be here and are just trying to break the game. I hope you're happy being trapped here with me forever.")
                    return
                     

        def new_lvl():
            global floor
            global level
            
            input("Before you, a latch protrudes from the cobblestones.")
            input("You brush off the layers of dust and grime to find a long-forgotten trapdoor.")
            x = input("Do you enter? y/n ")

            if x == str("y"):
                #load new level
                input("The air gets a little cooler as you descend into the darkness...")
                floor += 1
                print("[REACHED DUNGEON FLOOR", floor,"!]")
                input("")
        
                if level == 4:
                    print("[BEGINNING OF PART 2: BREAKING THE SEAL]")
                    #part two intro paragraph
                floorstart()
            else:
                input("You decide there is still more to be found on the level of the dungeon you are already in.")
                step()
                

        #room types
        def trap():
            global trapdam
            global level
            global health

            if level == 1:
                trapdam = 5
            if level == 2:
                trapdam = 10
            if level == 3:
                trapdam = 15
            if level == 4:
                trapdam = 20
            if level == 5:
                trapdam = 25
            if level == 6:
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
            
            input("Match the number to survive! Your accuracy determines the damage dealt.")
            
            print("On Floor", floor, ", the max number is", trapdam, ".")
            y = input("Choose your number: ")

            if any(s.isdigit() for s in y):
                r = int(y)
                h = abs(z - r)
                health -= h
                
            else:
                print("Pick a number!")
                trap()
            
            print("You took", h, "damage!")

            if health <= 0:
                deathscene()
            
            print("Health: ", health)

        def lvl_check():
            global floor
            global level

            if floor <= 3:
                level = 1
            if floor <= 6 and floor > 3:
                level = 2
            if floor <= 9 and floor > 6:
                level = 3
            if floor <= 12 and floor > 9:
                level = 4
            if floor <= 15 and floor > 12:
                level = 5
            if floor <= 18 and floor > 15:
                level = 6
                
        def loot():
            global floor
            global treasure
            global inventory
            global treasure
            global level

            if level == 1:
                a = 1
                x = 5
            if level == 2:
                a = 1
                x = 10
            if level == 3:
                a = 5
                x = 15
            if level == 4:
                a = 10
                x = 21
            if level == 5:
                a = 15
                x = 26
            if level == 6:
                a = 15
                x = 31

            t1 = treasure[int(random.randint(a, x))]
            t2 = treasure[int(random.randint(a, x))]
            t3 = treasure[int(random.randint(a, x))]
            
            input("Pushing open the heavy door, you peer into the room.")
            print("Suddenly, you spot a old chest sitting in the corner of the room. Covered in cobwebs, it lures you with the promise of treasure and arcane secrets.")
            input("...")
            input("You carefully lift the lid of the ancient trunk, revealing a great number of trinkets, some more useful than others.")
            print("Primarily, a few things catch your eye: a ", t1.name, "[1], a ", t2.name, "[2], and a", t3.name, "[3].")

            pick = int(input("Pick an item:"))

            if pick == 1:                
                inventory.append(t1)
                b = t1
            if pick == 2:                
                inventory.append(t2)
                b = t2
            if pick == 3:                
                inventory.append(t3)
                b = t3

            if len(inventory) < 6:
                print("Added", b.name, "!")
            else:
                print("Inventory full!")
      

        def monster():
            global floor
            global health
            global weapon
            global level
            global enemy_health
            global enemy_damage

            lvl_1 = ["As you enter the room, you are greeted by a distinct clicking emanating from the ground. You squint into the darkest far corner to be met by a horrible sight. The tapping of hard, pointed feet against stone intensifies as you shine your light onto a huge scorpion, its tail waving menacingly behind it.", "Pushing open the door, you find yourself in a space covered in a thin dusting of sand. Stepping into the center of the room, you are quickly met by a sudden hissing as a pair of slit eyes stares back at you, unblinking. Before you can react, the huge, pale viper lunges towards you.", "The creaking of the old wooden door is met by a raspy cackle from some unseen place. You take a step back as a shuffling sound reveals a small creature, gray-skinned and dressed in dusty rags, walking towards you. Halfway across the room, it looks at you and grins, its dry lips pulling back to reveal sharp, yellowed teeth and little black bugs."]
            lvl_2 = ["The creaking of the old wooden door is met by a raspy cackle from some unseen place. You take a step back as a shuffling sound reveals a small creature, gray-skinned and dressed in dusty rags, walking towards you. Halfway across the room, it looks at you and grins, its dry lips pulling back to reveal sharp, yellowed teeth and little black bugs.", "Entering the room, there is a moment of silence. Everything is still, then a heavy huff blows moisture in your face. The scent is enough to make you double over, a combination of mildew, rotting meat, and blood. A giant, twisted creature stands on two trunks of knotted flesh and emits a guttural sound that vibrates in your chest.", "Though you are deeper in the dungeon, it seems that the sand has actually increased here. It muffles your footsteps as you enter the room. An ear-piercing shriek, somewhere between a roar and a woman's scream, forces you to grip your head in pain. Quickly, you whip around to see a taloned lion leaping through the air, snake tail hissing and wings outstretched."]
            lvl_3 = ["Though you are deeper in the dungeon, it seems that the sand has actually increased here. It muffles your footsteps as you enter the room. An ear-piercing shriek, somewhere between a roar and a woman's scream, forces you to grip your head in pain. Quickly, you whip around to see a taloned lion leaping through the air, snake tail hissing and wings outstretched.", "You are met with a strange, dry scent as you enter the room. A dark shape lies on the floor in the corner, draped in red, moth-eaten robes. As you lean over the dried-out corpse, the body heaves to life, sucking in a hollow breath, bones creaking beneath leathery skin. The sunken eyes snap open and lock onto you.", "Cultist of P'tik 'Kira"]
            lvl_4 = ["Cultist of P'tik 'Kira","'Dai va", "Tan'ni na"]
            lvl_5 = ["Tan'ni na","Lizard statue", "Lamashtu"]
            lvl_6 = ["Lamashtu","Ekimmu"]
            
            input("Pushing open the heavy door, you peer into the room.")
            input("...")

            x = random.randint(0, 1)
            
            if level == 1:
                enemy_health = 3
                enemy_damage = 1
                input(lvl_1[x])
            if level == 2:
                enemy_health = 6
                enemy_damage = 2
                input(lvl_2[x])
            if level == 3:
                enemy_health = 12
                enemy_damage = 4
                input(lvl_3[x])
            if level == 4:
                enemy_health = 24
                enemy_damage = 8
                input(lvl_4[x])
            if level == 5:
                enemy_health = 48
                enemy_damage = 16
                input(lvl_5[x])
            if level == 6:
                enemy_health = 96
                enemy_damage = 32
                input(lvl_6[x])
            
            battle()
                
#left off here/ battle system
        def battle():
            global health
            global mana
            global level
            global enemy_health
            global enemy_damage

            enemies[]
            
            inventory_check()
            pick1 = input("Which item do you want to use? [Type the number]:")

            if any(s.isdigit() for s in pick1):
                pick = int(pick1)
                if isinstance(pick, int):
                    if pick >= len(inventory):
                        print("Pick something in your inventory!")
                        battle()
                    else:
                        #only be able to use weapons, magic, or potions during battle
                        if isinstance(inventory[pick], weapon) or isinstance(inventory[pick], potion) or pick == 1:
                            #miss 20% moves
                            miss = random.randint(1, 5)
                            misscheck = True
                        
                            if miss != 1:
                                misscheck = False
                                #player's attack successful
                                
                                if isinstance(inventory[pick], weapon):
                                    inventory[pick].use()
                                    enemy_health -= inventory[pick].damage
                                    print("Enemy took", inventory[pick].damage, "damage!")

                                if isinstance(inventory[pick], potion):
                                    inventory[pick].use()

                                if pick == 1:
                                    print("")
                                    print("Currently available spells:")
                                    
                                    for i in player_spells:
                                        print(i.name)
                                        print("[", player_spells.index(i), "]")
                                        
                                    print("['c' to cancel]")
                                    x = input("Which spell do you want to use? [Type the number]:")

                                    if x == "c":
                                        print("Spell cancelled.")
                                        battle()
                                    else:
                                        y = int(x)

                                        player_spells[y].use()

                                        if player_spells[y].typeis == "attack":
                                            enemy_health -= player_spells[y].damage
                                            print("Enemy took", player_spells[y].damage, "damage!")
                                        else:
                                            health += player_spells[y].heal
                                            print("Gained", player_spells[y].heal, "health!")

                            if enemy_health <= 0:
                                print("You won!")
                                
                            else:
                                print("Enemy health:", enemy_health)

                                if misscheck == True:
                                    print("You missed!")
                                #enemy's attack
                                print("The enemy attacked!")
                                print("-", enemy_damage, "health!")
                                health -= enemy_damage

                                if health <= 0:
                                    deathscene()
                                battle()
                        else:
                            print("You can't use that!")
                            battle()
            else:
                print("Pick a number!")
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
            global health
            global mana

            lvl_check()

            if x == mpg1:
                if y == mpg2:
                    new_lvl()
            
            else:
                if visited == False:
                    for i in roomsx:
                        for a in roomsy:
                            if i == x and a == y:
                   #             print(roomstype[index])

                                if roomstype[index] == "trap":
                                    trap()
                                if roomstype[index] == "loot":
                                    loot()
                                if roomstype[index] == "monster":
                                    monster()
                visited = True
                
                pick1 = input('''                        -Go forward [1]
                        -Go right [2]
                        -Go back [3]
                        -Go left [4]
                        -Check your inventory [i]
                        -Drop an item [d]
                        -Use an item [u]


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
                    pick2 = input("Use which item? [Type the number]:")

                    if any(s.isdigit() for s in pick2):
                        pick = int(pick2)
                      
                        if int(pick) >= len(inventory):
                            print("Pick something in your inventory!")
                            step()
                            
                        else:
                            if inventory[int(pick)] == "magic":
                                #items magic
                                print("")
                                print("Currently available spells:")
                                for i in player_spells:
                                    print(i.name)
                                    print("[", player_spells.index(i), "]")
                                print("['c' to cancel]")
                                
                                x = input("Which spell do you want to use? [Type the number]:")

                                if x == "c":
                                    print("Spell cancelled.")
                                    step()
                                    
                                else:
                                    y = int(x)
                                    
                                    if mana >= player_spells[y].cost:
                                        print("spell worked")
                                        if player_spells[y].typeis == "attack":
                                            enemy_health -= player_spells[y].damage
                                            print("Enemy took", player_spells[y].damage, "damage!")
                                        else:
                                            health += player_spells[y].heal
                                            print("Gained", player_spells[y].heal, "health!")
                                    player_spells[y].use()
                                    step()
                            else:
                                #items not magic
                                inventory[x].use()
                                step()
                    else:
                        print("Pick a number!")
                        step()
                            
                if pick1 == "d":
                    inventory_check()
                    pick2 = input("Drop which item? [Type the number]:")

                    if any(s.isdigit() for s in pick2):
                        pick = int(pick2)
                        if pick == 0 or pick == 1:
                            print("You can't drop that!")
                            step()
                        else:
                            if pick >= len(inventory):
                                print("Pick something in your inventory!")
                                step()
                                
                            else:
                                for i in inventory:
                                    if inventory.index(i) == pick:
                                        x = inventory.index(i)
                                
                            inventory.pop(x)
                            print("Dropped item!")    
                            step()
                    else:
                        input("Pick a number!")
                        step()
                else:
                    print("Make a decision, adventurer!")
                    step()
                    
        def inventory_check():
            global health
            global mana
            
            print("Current Health:", health)
            print("Current Mana:", mana)
            print("Inventory: ", len(inventory), "/6")
            
            if len(inventory) == 6:
                print("INVENTORY CURRENTLY FULL!")
                
            for i in inventory:
                if isinstance(i, str):
                    print(i)
                    print("[", inventory.index(i), "]")
                else:
                    print(i.name)
                    print("[", inventory.index(i), "]")
                
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
