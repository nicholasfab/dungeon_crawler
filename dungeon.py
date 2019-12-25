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
enemies = []
visited = False

weapon = False

enemy_health = 0
enemy_damage = 0

r = 0

deaths = 0

battling = False

spells_1 = []
spells_2 = []
spells_3 = []

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
    global enemies
    global battling

    inventory = []
    treasure = []
    spells = []
    player_spells = []
    enemies = []
    floor = 0
    level = 0
    health = 1000
    mana = 5000
    deaths = 0
    battling = False
    
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
        global enemies
        global spells_1
        global spells_2
        global spells_3

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
                global battling

                if battling:
                    self.durab -= 1
                    if self.durab <= 0:
                        print(self.name, "was destroyed!")
                        inventory.pop(inventory.index(self))
                    else:
                        print("Used", self.name, "!")
                        print(self.durab, "uses left.")
                else:
                    print("Nothing to use that against!")

        class magic():
            global mana
            def __init__(self, name, damage, heal, typeis, cost, text):
                self.name = name
                self.damage = damage
                self.heal = heal
                self.typeis = typeis
                self.cost = cost
                self.text = text
                
            def use(self):
                global mana
                if mana >= self.cost:
                    input(self.text)
                    mana -= self.cost
                    print(mana, "mana remaining!")
                else:
                    print("Not enough mana for this spell!")

        class special():
            global spells_1
            global spells_2
            global spells_3
            
            def __init__(self, name, level):
                self.name = name
                self.level = level

            def use(self):
                x = random.randint(0, 2)
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
            def __init__(self, name, enter, attacks, death):
                self.name = name
                self.enter = enter
                self.attacks = attacks
                self.death = death

            def intro(self):
                print(self.enter)

            def attack(self):
                r_pick = random.randint(0, len(self.attacks)-1)
                print(self.name, self.attacks[r_pick])
                
            def die(self):
                print(self.death)

                
        inventory = [weapon("punch", 100000, 1), "magic"]
        player_spells = [magic("Heal", 0, 2, "heal", 5, "You speak the ancient words and are enveloped in a green, healing light.")]

        #magic list
        spells_1 = [magic("Firebolt", 1, 0, "attack", 5, "Your hands begin to glow red as you chant in the dead language. With a final shout, red lightning shoots from yout palm and strikes the creature, igniting it."),
        magic("Abracadabra", 2, 0, "attack", 5, "You recite the ridiculuous incantation until the enemy looks at you in disgust. You call that a spell? Your attempts are so pitiful that they bring the creature physical pain."),
        magic("Shock", 3, 0, "attack", 5, "You shout a single, ancient word. Faster than the eye can see, purple electricity zaps from your outstretched fingertips to the enemy.")]

        spells_2 = [magic("Fireball", 1, 0, "attack", 10, "Your body feels warm as you charge up your attack, rapidly muttering the spell. With both hands in front of you, a large fireball swells to life and burns your enemy."),
        magic("Turn Undead", 2, 0, "attack", 10, "A flash of blue-white light appears from the sky and blasts your enemy with a purifying light."),
        magic("God Blow", 3, 0, "attack", 10, "You are reminded of a certain useless goddess as you slam your brightly-glowing fist into the enemy.")]

        spells_3 = [magic("Ifrit's Curse", 1, 0, "attack", 20, "The air around you warps with heat, your hair glows red, and the distinct scent of cooking meat fills the air. If you chanted for too long, you'd probably die. The enemy's skin crackles and tears, black blood running out of the crevices before boiling into the air. Their eyes begin to glow white and the ground beneath them now resembles smoldering coals. The creature shrieks in agony as it burns."),
        magic("Vow of Caine", 2, 0, "attack", 20, "The words you speak now feel even more arcane than the spells you are used to, twisting your throat and tongue in ways clearly not meant for human voices. Your eyes glint gold in the darkness, a strange intensity falling upon your enemy. The creature pauses for a moment before its joints give a sickening pop as they are bent backwards, bony spurs sprouting beneath their skin and piercing through, black blood spewing everywhere. The air is filled with a putrid scent as large, tumorous pustules form on the thing's body. They expand and tremble until the cover the original form of the creature entirely."),
        magic("Edge of Oblivion", 3, 0, "attack", 20, "The moment the last of the incantation leaves your lips, all air in the room vanishes. An unthinkable pressure seems to close in from all sides as the room gets even darker. Before you, your enemy seems afraid. It trembles, the blinks out of existence for a moment.")]

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
        enemies = [enemy("scorpion", "As you enter the room, you are greeted by a distinct clicking emanating from the ground. You squint into the darkest far corner to be met by a horrible sight. The tapping of hard, pointed feet against stone intensifies as you shine your light onto a huge scorpion, its tail waving menacingly behind it.", ["The creature lunges forwards, skittering on spindly legs.", "You try to duck, but the joints of the tail creak as an unsettlingly long stinger shoots towards you.", "You manage to dodge most of the scorpion's attacks, but you soon find yourself too close to its mouth. The jet-black fangs bear down on you."], "The massive arachnid shudders, the great exoskeleton cracking and spurting black, sticky blood. The scorpion's corpse falls to the ground with a thud before vanishing in a cloud of black smoke."),
                   enemy("snake", "Pushing open the door, you find yourself in a space covered in a thin dusting of sand. Stepping into the center of the room, you are quickly met by a sudden hissing as a pair of slit eyes stares back at you, unblinking. Before you can react, the huge, pale viper lunges towards you.", ["The snake hisses as you sprint towards it. Just as you think you see an opening, it strikes.", "The hissing stops momentarily. You tense up, searching the dark for movement, but you are surprised when pain rockets through your shoulder and you feel long fangs sink deep into your flesh.", "Before you can react, the snake slithers over and coils around your body. You struggle to break free from the cord of muscle that is crushing your organs."], "The snake gives one last hiss before falling lifelessly to the ground, black blood pooling around it. Before your eyes, the creature disintegrates in a cloud of black smoke."),
                   enemy("goblin", "The creaking of the old wooden door is met by a raspy cackle from some unseen place. You take a step back as a shuffling sound reveals a small creature, gray-skinned and dressed in dusty rags, walking towards you. Halfway across the room, it looks at you and grins, its dry lips pulling back to reveal sharp, yellowed teeth and little black bugs.", ["The goblin laughs and leaps at you, slashing in the air with sharp, filthy claws.", "The small creature produces a small, sharp object from beneath its robes and grins, a crazed look in its eyes. It laughs as it runs towards you, blade in hand.", "With surprising speed, the goblin rushes behind you and scrabbles onto your back, sinking its little razor teeth into your arm."], "The smug little creature is no longer smiling, falling to its knees and coughing. It spits out a smatter of black blood onto the rough stone floor. You can see one final look of panic in the goblin's eyes as it stares right at you before bursting into black smoke."),
                   enemy("ogre", "Entering the room, there is a moment of silence. Everything is still, then a heavy huff blows moisture in your face. The scent is enough to make you double over, a combination of mildew, rotting meat, and blood. A giant, twisted creature stands on two trunks of knotted flesh and emits a guttural sound that vibrates in your chest.", ["The mammoth thing groans and takes a slow step towards you. It brings a long, powerful arm down on you with great force.", "The ogre grunts and makes a grab for you with a giant, knotted hand.", "Out of breath, you stop for a minute. Your stomach drops as you look up to see a huge, rock-like foot bearing down on you."], "The huge ogre freezes, swinging arms falling to its sides. All is silent for a moment, then the giant lets out an earth-shaking bellow, the vibrations rumbling in your chest. All of a sudden, the roar is cut short as the beast explodes into a cloud of black smoke with such force that you can feel the wind blow against your face."),
                   enemy("chimera", "Though you are deeper in the dungeon, it seems that the sand has actually increased here. It muffles your footsteps as you enter the room. An ear-piercing shriek, somewhere between a roar and a woman's scream, forces you to grip your head in pain. Quickly, you whip around to see a taloned lion leaping through the air, snake tail hissing and wings outstretched.", ["You jump behind the beast, only to be struck by its hissing tail.", "The chimera leaps into the air, hovering for a second on heavily beating wings before swooping down and slamming into you with incredible force.", "You are knocked to the ground with a single stroke of the monster's powerful claws."], "Slumping to the floor, the monster gives a weak growl. Collapsed in a pile, the chimera doesn't seem as large as it did before before disintegrating into black smoke."),
                   enemy("mummy", "You are met with a strange, dry scent as you enter the room. A dark shape lies on the floor in the corner, draped in red, moth-eaten robes. As you lean over the dried-out corpse, the body heaves to life, sucking in a hollow breath, bones creaking beneath leathery skin. The sunken eyes snap open and lock onto you.", ["A deep breath is sucked into the ancient lungs as the mummy stumbles unsteadily towards you. Suddenly, the broken body launches towards you with supernatural speed, the bony fingers ripping at your flesh.", "The dry corpse shakes slightly as its jaw snaps open and a buzzing ensues. A swarm of shiny, rainbow-shelled locusts erupt from the thing's mouth.", "The ancient thing points a shaking finger at you and utters an inhuman shriek. You clasp your hands against your ears as warm blood drips down the side of your face."], "With no warning, the seemingly-immortal thing's head droops before the mummy collapses into a pile of blackened soot."),
                   enemy("cultist", "Cultist of P'tik 'Kira", ["tbd", "tbd"], "dead"),
                   enemy("demon", "'Dai va", ["tbd", "tbd"], "dead"),
                   enemy("dragon", "Tan'ni na", ["tbd", "tbd"], "dead"),
                   enemy("lizard", "Lizard statue", ["tbd", "tbd"], "dead"),
                   enemy("mountain", "Lamashtu", ["tbd", "tbd"], "dead"),
                   enemy("vampire", "Ekimmu", ["tbd", "tbd"], "dead")]

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

            h = 0

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

            level = 4

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
            global enemies
            global r
            
            input("...")

            if level == 1:
                enemy_health = 3
                enemy_damage = 1

                r = random.randint(0, 1)
                enemies[r].intro()
                
            if level == 2:
                enemy_health = 6
                enemy_damage = 2

                r = random.randint(2, 3)
                enemies[r].intro()
                
            if level == 3:
                enemy_health = 12
                enemy_damage = 4

                r = random.randint(4, 5)
                enemies[r].intro()
                
            if level == 4:
                enemy_health = 24
                enemy_damage = 8

                r = random.randint(6, 7)
                enemies[r].intro()
                
            if level == 5:
                enemy_health = 48
                enemy_damage = 16

                r = random.randint(8, 9)
                enemies[r].intro()
                
            if level == 6:
                enemy_health = 96
                enemy_damage = 32

                r = random.randint(10, 11)
                enemies[r].intro()
            
            battle()
                
#battle system
        def battle():
            global health
            global mana
            global level
            global enemy_health
            global enemy_damage
            global enemies
            global r
            global battling

            battling = True
            
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
                                enemies[r].die()
                                print("You won!")
                                
                            else:
                                print("Enemy health:", enemy_health)

                                if misscheck == True:
                                    print("You missed!")
                                #enemy's attack
                                enemies[r].attack()
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
            global battling

            battling = False

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

                            if inventory[pick] == "magic":
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
                                        if player_spells[y].typeis == "attack":
                                            if battling == True:
                                                enemy_health -= player_spells[y].damage
                                                print("Enemy took", player_spells[y].damage, "damage!")
                                                player_spells[y].use()
                                            else:
                                                print("Nothing to use that against!")
                                        else:
                                            health += player_spells[y].heal
                                            print("Gained", player_spells[y].heal, "health!")
                                            player_spells[y].use()
                                    step()
                            else:
                                #items not magic
                                inventory[pick].use()
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
            global battling
            #durab
            
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
                    if isinstance(i, weapon):
                        if battling == True:
                            print(i.name)
                        else:
                            print(i.name, ", Durability:", i.durab)
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
