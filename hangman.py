# tiy hangman project
from sys import exit
import random

with open("/usr/share/dict/words") as word_file:
    words = word_file.readlines()


def get_user_guess():
    valid_guess = False

    while not valid_guess:
        guess = input("Guess a letter.\n>> ")
        if guess.isalpha() and len(guess) == 1:
            valid_guess = True
    return guess


def get_random_word():
    word = random.choice(words)
    return word.lower().strip()


def play_game():
    turns = 8
    word = get_random_word()
    hidden_word = list('_'*len(word))
    incorrect_guesses = []
    correct_guesses = []

    # for debugging
    # print(word, len(word))
    print(''.join(hidden_word), "{} letters.".format(len(word)))

    while ''.join(hidden_word) != word:
        guess = get_user_guess()

        if guess in incorrect_guesses or guess in correct_guesses:
            print("You've already guessed that letter!")
        elif guess not in word:
            turns -= 1
            incorrect_guesses.append(guess)

            print("Sorry your guess was incorrect. You have {} turns left.".format(turns))
            if turns == 0:
                print("Game over. The word was {}.".format(word))
                play_again()
        elif guess in word:
            correct_guesses.append(guess)

            for idx in range(len(word)):
                if guess == word[idx]:
                    hidden_word[idx] = word[idx]

        print(''.join(hidden_word))
        print("Incorrect guesses: " + " ".join(incorrect_guesses))

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
