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
    g = 6

def f7_potion_challenge():
    h = 7

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
    if choice_1 == "1":
        print()
        print("You ride down into the valley, your goat easily traversing the rocky terrain. Tall grass grows on\neither side of the path, swaying and rustling in the breeze.")
        print("You continue for some time until suddenly, a goblin leaps out from the tall grass and blocks your path. In one hand, it holds a short but deadly-looking sword, and in the other, a scroll of tattered yellow parchment.")
        print()
        print("The goblin snarls, 'stop! you may go no further until you have answered my riddle. Answer correctly, and I will give you this map that leads to untold treasures. Answer incorrectly, and you will become acquainted with my sword. You have five guesses'.")
        guess = input("My riddle is this: What has a bed but never sleeps, can run but never walks, and has a mouth\nbut never talks?")
        if f3_guess_the_code(guess):
            print("You examine the map.  ")
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
