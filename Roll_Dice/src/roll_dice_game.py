#Rolling dice game with user inputs 


import random

# function to roll dice
def roll_dice():
    
    while True:

        # Take use input
        user_input = input("Roll the Dice? y/n ")

        # check if the user input is Yes or not or invalid choice
        if user_input.lower() == 'y':
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            print(f'({die1},{die2})')
        elif (user_input == 'n'):
            print("Thanks for playing the game. Have a great day!!!")
            break
        else:
            print("Invalid Choice")


# start of the function
if __name__ == '__main__':
    roll_dice()