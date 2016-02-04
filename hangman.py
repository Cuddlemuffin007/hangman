# tiy hangman project
from sys import exit
# import random


def get_user_guess():
    guess = input("Guess a letter.\n>> ").lower()
    return guess


def get_random_word():
    pass


def play_game():
    turns = 5
    word = 'bathroom'
    hidden_word = list('_'*len(word))

    while ''.join(hidden_word) != word and turns > 0:
        guess = get_user_guess()

        if guess not in word:
            turns -= 1
            print("Sorry your guess was incorrect. You have {} turns left.".format(turns))
            if turns == 0:
                print("Game over.")
                play_again()
        elif guess in word:
            for idx in range(len(word)):
                if guess == word[idx]:
                    hidden_word[idx] = word[idx]

    else:
        print("You win! The word was {}.".format(word))
        play_again()

    print(word)
    print(''.join(hidden_word))
    exit(0)


def play_again():
    play_again = input("Would you like to play again? (Enter 'Y' or 'N')\n>> ")
    while play_again != 'Y' and play_again != 'N':
        play_again = input("Please enter 'Y' or 'N'.\n>> ")
    if play_again == 'Y':
        play_game()
    elif play_again == 'N':
        print('Goodbye!')
        exit(0)


play_game()
