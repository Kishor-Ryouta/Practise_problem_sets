#Guessing game program........

import random

while True:
    try:
#Prompts the user for a level, If the user does not input a positive integer, the program should prompt again.
        user_level = int(input("level: "))
        if user_level > 0:
            break
    except ValueError:
        pass

#Randomly generates an integer between 1 and , inclusive, using the random module.
x = random.randint(1,user_level)

while True:
    try:
#Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
        user_input = int(input("Guess: "))
        if user_input > 0:
#If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
#If the guess is larger than that integer, the program should output Too large! and prompt the user again.
#If the guess is the same as that integer, the program should output Just right! and exit
            if user_input < x:
                print("Too small!")
            elif user_input > x:
                print("Too large!")
            else:
                print("Just right!")
                break
    except ValueError:
        pass

