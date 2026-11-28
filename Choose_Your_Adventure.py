import random

# List of our functions
def main():
    a = 0

def f1_randomizer():
    b = 1

def f2_the_adversary():
    c = 2

def f3_guess_the_code(word):
    '''This function is designed to have the user guess the answer to a riddle. 
    The riddle is the 'code' that the user has five chances to guess or else the loop breaks.
    '''
    count = 0
    code = "river" 
    while word != code:
        count += 1
        print("The goblin laughs, 'wrong! haha try again you fool!'")
        word = input()
        if count == 4:
            print("The goblin growls,'You have failed me for the last time! Prepare to meet your doom!'")
            return False
    if word == code:
        print()
        print("The goblin grins evilly, 'I suppose you are not as impotent as I thought. Here is the map,\nas promised.' It passes you the aged scroll and dissapears silently into the tall grass.")   
        return True
        
def f4_decode_the_message():
    e = 4

def f5_the_maze():
    f = 5


def f6_combat_system():
    '''
    This functions allows the player to fight a Magical Guardian.
    The plater chooses between Fire, Water and Earth.
    The Guardian randomly chooses an element. 
    A draw allos the player to try again.
    '''

    print()
    print("The Magical Guardian blocks your path!")
    print("'You shall not pass unless you defeat me in a magical duel!'")

    while True:
        print()
        print("Choose your magical element:")
        print("1. Fire")
        print("2. Water")
        print("3. Earth")

        player = input("Choose your element: ")

        while player not in ["1", "2", "3"]:
            print("Invalid choice. Try again.")
            player = input("Choose your element: ")

        if player == "1":
            player_spell = "fire"
        if player == "2":
            player_spell = "water"
        else:
            player_spell = "earth"

        guardian_spell = random.choice(["fire", "water", "earth"])

        print()
        print("You cast", player_spell)
        print("The Guardian casts", guardian_spell)
        
        if player_spell == guardian_spell:
            print("It's a draw! Try again.")


        elif (player_spell == "fire" and guardian_spell == "earth") or \
             (player_spell == "earth" and guardian_spell == "water") or \
             (player_spell == "water" and guardian_spell == "fire"):

            print("You win! The Guardian disappears.")
            return True

        else:
            print("You lost! The Guardian defeats you.")
            return False

def f7_potion_challenge():
    '''
    This function challenges the player to create a magical potion.
    The player must choose three ingredients in the correct order.
    They have three attempts.
    Hints are provided.
    '''

    print()
    print("You have reached the castle!")
    print("A magical door blocks your way.")
    print("'Only the correct potion can break this spell!'")

    print()
    print("Choose three ingredients in the correct order:")
    print("1. Moonflower")
    print("2. Dragon scale")
    print("3. Stardust")
    print("4. Nightshade")

    print()
    print("HINT: Begin where petals bloom, awaken the ancient fire for power, and let the cosmos lock the spell")

    attempts = 0

    while attempts < 3:
        print()
        ingredient_1 = input("Choose your first ingredient (1-4): ")

        while ingredient_1 not in ["1", "2", "3", "4"]:
            ingredient_1 = input("Invalid choice. Choose 1-4: ")

        ingredient_2 = input("Choose your second ingredient (1-4): ")

        while ingredient_2 not in ["1", "2", "3", "4"]:
            ingredient_2 = input("Invalid choice. Choose 1-4: ")

        ingredient_3 = input("Choose your third ingredient (1-4): ")

        while ingredient_3 not in ["1", "2", "3", "4"]:
            ingredient_3 = input("Invalid choice. Choose 1-4: ")

        if ingredient_1 == "1" and ingredient_2 == "2" and ingredient_3 == "3":
            print()
            print("The potion glows with a bright magical light!")
            print("The door opens. You successfully created the potion!")
            return True

        else:
            attempts += 1
            print()
            print("The potion produces a strange purple smoke!")
            
            if attempts < 3:
                print("Something is wrong with the ingredients.")
                print("Remember the HINT!!!")
                print("You have", 3-attempts, "attempts left.")

    print()
    print("The potion explodes!")
    print("The magical door remains locked.")
    return False

def f8_final_battle_wr():
    '''
    RPG battle against the Dark Wizard.
    The player can attack, heal or use a shield.
    The Dark Wizard can attack, heal or gain fire immunity.
    '''

    print()
    print("THE FINAL BATTLE!")
    print("The Dark Wizard raises his staff.")

    player_health = 100
    wizard_health = 100
    crystal_shield = False
    fire_immunity = 0
    
    while player_health > 0 and wizard_health > 0:
        print()
        print("Wizard Raccoon:", player_health, "HP")
        print("Dark Wizard:", wizard_health, "HP")
        
        print("1. Arcane Comet (18-25 damage)")
        print("2. Phoenix Flame (25-32 damage)")
        print("3. Healing spell (+22 HP)")
        print("4. Crystal shield (you take half damage)")
        
        choice = input("Choose your action: ")
        
        while choice not in ["1", "2", "3", "4"]:
            print("Invalid choice.")
            choice = input("Choose your action: ")

        if choice == "1":
            damage = random.randint(18, 25)
            wizard_health -- damagee
            print("Arcane comet deals", damage, "damage!")

        elif choice == "2":
            if fire_immunity > 0:
                print("The Dark Wizard is immune to fire!")
            else:
                damage = random.randint(25, 32)
                wizard_health -= damage
                print("Phoenix flame deals", damage, "damage!")

        elif choice == "3":
            player_health = min(100, player_health +22)
            print("You recover health:", player_health, "HP")

        elif choice == "4":
            crystal_shield = True
            print("Crystal shield activated!")

        if wizard_health <= 0:
            break

        if fire_immunity > 0:
            fire_immunity -= 1

        wizard_action = random.choice(["attack", "attack", "heal", "potion"])

        if wizard_action == "heal" and wizard_health < 80:
            wizard_health = min(100, wizard_health + 18)
            print("Dark Wizard heals 18 HP.")

        elif wizard_action == "potion" and fire_immunity == 0:
            fire_immunity = 2
            print("Dark Wizard gains fire immunity!")

        else:
            damage = random.randint(15, 23)
            spell = random.choice(["Shadow bolt", "Dark lightning", "Soul drain"])
            
            if crystal_shield:
                damage //= 2
                crystal_shield = False
                print("Crystal shield reduces the damage!")

            player_health -= damage
            print(spell, "deals", damage, "damage!")

    print()
    
    if player_health > 0:
        print("VICTORY! The Dark Wizard has been defeated!")
        return True

    else:
        print("DEFEAT! The Dark Wizard was too powerful!")
        return False

def wizard_raccoon():
    '''
    This function controls the Wizard Raccoon's storyline. 
    The player must defeat the Magical Guardian, create a potion and defeat the Dark Wizard to recover the stolen crystal. 
    Losing any of the challegenges results in game over.
    '''

    print()
    print("You have chosen the Wizard Raccoon!")
    print("You are a young wizard who lives in an enchanted forest.")
    print("One morning, you discover the magical crystal")
    print("protecting your forest has been stolen by a Dark Wizard.")
    print("You must recover it before the forest loses its magic.")

    print()
    print("You travel tgrough the forest until you reach an old bridge.")
    print("A Magical Guardian appears and challenges you to a duel.")

    if f6_combat_system() == False:
        print()
        print("Game Over!! Your journey ends at the bridge.")
        return

    print()
    print("You cross the bridge and reach the Dark Wizard's castle.")
    print("Inside, you discover a magical door protecting the crystal.")
    print("You must prepare a special potion to open it.")

    if f7_potion_challenge() == False:
        print()
        print("Game Over!! You failed to break the magical spell.")
        return

    print()
    print("The magical doors opens!")
    print("You enter the throne room and find the Dark Wizard.")
    print("He is holding the stolen crystal.")
    print("You must defeat him to save the forest!")

    if f8_final_battle_wr() == False:
        print()
        print("Game Over!! The Dark Wizard keeps the crystal.")
        return

    print()
    print("You recover the stolen crystal!")
    print("You return to the forest and restore its magic.")
    print("The trees begin to glow and the creatures celebrate.")

    print()
    print("CONGRATULATIONS!!")
    print("You completed the Wizard Raccoon's adventure!")
    print("ENGING: TH GUARDINAN OF THE FOREST.")    

# Start of game    
print("Hello and welcome to this choose your own adventure game!\nIn this game, every decision you make will affect how your story ends, so choose wisely...")
print()
print("Your first decision is the most important. You must choose your character to start the journey.")
choice_0 = input("Type '1' to select the dwarf riding a goat, type '2' to select the wizard raccoon,\nor type '3' to select the frog.")

while choice_0 not in ["1", "2", "3"]:
    print("Invalid choice. Please try again.")
    choice_0 = input("Type '1' to select the dwarf riding a goat, type '2' to select the wizard raccoon, or type '3' to select the frog.")  

if choice_0 == "1":
    print()
    print("Excellent choice! The dwarf riding a goat is a steadfast and reliable hero who will\nserve you well on your journey.")
    print("Your story begins on a lonely mountain trail, winding through the trees, the scent of adventure\nin the air.")
    print("Around a sharp corner, you come across a fork in the path. To the left, you see a wide, open valley. To the right, the path continues deeper into the forest.")
    print()
    choice_1 = input("Type '1' to turn left into the valley, or type '2' to turn right into the forest.")
    while choice_1 not in ["1", "2"]:
        print()
        print("Invalid choice. Please try again")
        choice_1 = input("Type '1' to turn left or '2' to turn right")
    if choice_1 == "1":
        print()
        print("You ride down into the valley, your goat easily traversing the rocky terrain. Tall grass grows on\neither side of the path, swaying and rustling in the breeze.")
        print("You continue for some time until suddenly, a goblin leaps out from the tall grass and blocks your path. In one hand, it holds a short but deadly-looking sword, and in the other, a scroll of tattered yellow parchment.")
        print()
        print("The goblin snarls, 'stop! you may go no further until you have answered my riddle. Answer correctly, and I will give you this map that leads to untold treasures. Answer incorrectly, and you will become acquainted with my sword. You have five guesses'.")
        guess = input("My riddle is this: What has a bed but never sleeps, can run but never walks, and has a mouth\nbut never talks?")
        if f3_guess_the_code(guess):
            print("You examine the map. It leads out of the meadow path and towards a rocky cliff")
        else:
            print("The goblin lunges at you and pierces your side with its sword. You fall from your mount and\neverything goes black.")
            print("GAME OVER")

        
    elif choice_1 == "2":
        print()
        print("You ride deeper into the forest, your goat's hooves clopping merrily on the stones.")

elif choice_0 == "2":
    print()
    print("You have chosen the wizard raccoon.")

elif choice_0 == "3":
    print()
    print("You have chosen the frog.")
