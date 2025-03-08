"""Write a program that simulates  rolling  a pair  of dice . Each time the program runs,it should randomly generate 
two numbers between 1 and 6 (inclusive), representing the result of each die.THr program should then display  the results and ask if you 
want to roll again"""
import random

# function to roll dice
def roll_dice():
    
    while True:

        # Take use input
        user_input = input("Roll the Dice? y/n ").lower()

        # check if the user input is Yes or not or invalid choice
        if user_input == 'y':
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            print(f"You rolled  a {die1} and a {die2}")
        elif (user_input == 'n'):
            print("Thanks for playing the game. Have a great day!!!")
            break
        else:
            print("Invalid Choice")


# start of the function
if __name__ == '__main__':
    roll_dice()