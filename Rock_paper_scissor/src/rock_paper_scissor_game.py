#ROCK PAPER SCISSOR game


import random

#Initialize the input through constants 
ROCK = 'r'
PAPER = 'p'
SCISSOR = 's'
input_choices = ('ROCK', 'PAPER', 'SCISSOR')


#function to choose user choice
def get_user_choice():
    while True:
        user_input = input("Enter your input?  ")
        if user_input in input_choices:
                return user_input
        else:
                print("Please enter a valid input") 

#function to display user choices
def display_choices(user, computer):
     print(f'You chose {user}')
     print(f'Computer chose {computer}')

#determine the Winner  of the game
def determine_winner(user_input,computer_input):
    if ((user_input == 'ROCK' and computer_input == 'SCISSOR') or 
           (user_input == 'PAPER' and computer_input == 'ROCK') or 
           (user_input == 'SCISSOR' and computer_input == 'PAPER')):
            print(" Player is the Winner")
        
    elif ((user_input == 'ROCK' and computer_input == 'PAPER') or 
             (user_input == 'PAPER' and computer_input == 'SCISSOR') or 
             (user_input == 'SCISSOR' and computer_input == 'ROCK')) :
            print("Computer is the Winner")
        
    elif user_input == computer_input:
            print("Tie!")

     
     
#Play the ROCK PAPER and SCISSOR game
def play_game():

    while True:
        user_input = get_user_choice()
        computer_input = random.choice(input_choices)
        display_choices(user_input,computer_input)
        determine_winner(user_input,computer_input)

        #print(emoji.emojize('ROCK'))
        player_input = input("Do you want to conntinue the Game?  Enter y/n: ")
        if player_input.lower() == 'y':
            continue
        else:
            break


#Initialize the main function to start the game
if __name__ == "__main__":
    play_game()
 


