"""
__file name__ = Guess game(multiplayer).py
__author__ = "ankit thakur"
__purpose__ = practice
__date created__ = 02/01/2022
__copyright__ = "Copyright 2025"
__credits__ = ["ankit thakur"]
__version__ = "1.1.0"
__maintainer__ = "ankit thakur"
__email__ = "itsankit.contact@gmail.com"
__discription__ = this program take input from user , on the bases of there input it decides who is the winner. 
"""
# Guess the number game.(Multiplayer game)

import random

print("               Gusee the number ! Game ") 

def guessGame(min_value, max_value, number_to_guess):
    '''
    this function will tell the no. of turns player has taken.
    '''
    guess = int(input(f"guess the number between {min_value} and {max_value} :\n"))
    no_of_guesses = 1
    while guess != number_to_guess:
        if guess < number_to_guess:
            guess = int(input("Enter a bigger number:\n"))
            no_of_guesses += 1

        else:
            guess = int(input("Enter a smaller number:\n"))
            no_of_guesses += 1

    print(f"Player {i} !\n You have guess the number in {no_of_guesses} Guess")
    return no_of_guesses



def findWinner(seq, item):
    '''
    This fuction will tell us the number of players who won !
    '''
    winners = []
    for idx, value in enumerate(seq):

        if value == int(item):
            idx += 1
            winners.append(idx)
        else:
            pass
    return winners

def restart():
            '''
            this is to ask user if they want to play again or not .
            '''
            start = ""
            while start != "q" and start != "s":
                start = input("Press 'q' to end the game and 's' to start again:\n")
                if start == "q":
                    exit()
                else:
                    pass



if __name__ == "__main__":
    while True:

        # basic input which we need from user to start ths game

        number_of_players = int(input("Enter the no. of players:\n"))
        min_value = int(input("Enter the minimum value for guessing:\n"))
        max_value = int(input("Enter the maximum value to guessing:\n"))
        score_list = []
        if min_value == max_value:
            print("Minimum and Maximum must be different!")
        # ths loop is for player turns
        for i in range(1, number_of_players + 1):
            print(f"it's player {i} turn ")
            number_to_guess = random.randint(min_value, max_value)
            player_score = int(guessGame(min_value, max_value, number_to_guess))
            score_list.append(player_score)

        mini = str(min(score_list))
        winners = findWinner(score_list, mini)

        # This is to convert list into string so output not in []

        winner = ", ".join([str(elem) for elem in winners])
        
       
        if len(winners) == 1:
            print(
            f"Congratulations Palyer {winner}. . . . . \n YOU ARE THE WINNNER OF THIS GAME"
            )
        elif len(winners) < 0:
            print("SOMETHING WENT WRONG")
            
        else:
            print(f" It's a tie between Player {winner}")

        restart()
        
