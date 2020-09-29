#ETGG 1801
#Eli Vaudrin
#Lab04 Flow Control
#9/26/20

i = 0

while i < 100:
    i = i + 1

    def fizzbuzz(i):
        if i % 3 == 0 and i % 5 == 0:
            return("FizzBuzz")
        elif i % 3 == 0:
            return("Fizz")
        elif i % 5 == 0:
            return ("Buzz")
        else:
            return i
    print(fizzbuzz(i))

input("Press enter to continue.")


#Expand on lesson ( Text Adventure )

y_n = ["yes", "no"]
direction = ["north", "south", "east", "west"]

name = input("What is your name adventurer?")
print("Hello " + name, ",lets begin our adventure.")
print("You are on a dirt trail that branches into three different paths up ahead.")

answer = ""
while answer not in y_n:
    answer = input("Do you want to follow a trail?")
    if answer == "yes":
        print("You continue down the trail and stop at the branching paths. \n")
    elif answer == "no":
        print("You decide to play it safe and walk back home.")
        input("Press enter to end the program")
        quit()
    else:
        print("That is not an answer to the question try yes or no. \n")

answer = ""
while answer not in direction:
    print("To the east is a pack of hungry wolves guarding a treasure.")
    print("to the west is a village being attacked by a band of bandits.")
    print("To the north is a mountain.")
    print("To the south is back to your home.")
    answer = input("Which way do you decide to travel? \n north, south, east, or west. \n")
    if answer == "east":
        print("There were to many wolves and they end up killing you. Goodbye, " + name, ".")
        input("Press enter to end the program")
    elif answer == "south":
        print("You change your mind about continuing your adventure and head back home. Goodbye, " + name, ".")
        input("Press enter to end the program")
    elif answer == "north":
        print("You head to the mountain and try to make your way around but you step on a loose rock and fall to your death. So long, " + name, ".")
        input("Press enter to end the program")
    elif answer == "west":
        print("You help the villagers fend off the bandits and they reward you with gold and are now known as a hero in their village.")
        input("Press enter to end the program")
    else:
        print("That is not an answer to the question try north, south, east, or west. \n")