""" Guessing number Game"""

import random

#select a low range 
low = 1
#select a high range 
high = 100

#store the secret number in variable
secret_number = random.randint(low, high)

#Infinite loop for game execution in a function 
def guessing_game_function(counter):
    while True:
        try:
            user_input = int(input(f"Guess the number between {low} and {high}:  "))
            if  user_input > secret_number:
                print("Too High!")
                counter = counter + 1
            elif user_input < secret_number:
                print("Too low!")
                counter = counter + 1
            else:
                print(f"Congratulations!You guessed the number in {counter} attempts")
                break
        except ValueError:
            print("Please enter a valid number")



if __name__ == "__main__":
    #count the number of attempts
    counter = 0
    guessing_game_function(counter)
        
