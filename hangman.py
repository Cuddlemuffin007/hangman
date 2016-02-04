# tiy hangman project
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
                break
        elif guess in word:
            for idx in range(len(word)):
                if guess == word[idx]:
                    hidden_word[idx] = word[idx]

    print(word)
    print(''.join(hidden_word))
    exit(0)


def play_again():
    pass

play_game()
