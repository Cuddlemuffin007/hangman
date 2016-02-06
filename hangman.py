# tiy hangman project
from sys import exit, argv
import random

# Flag to check if a user has won the game at least once
# Winning a normal game sets this to true unlocking evil mode
won_once = False
if len(argv) > 1:
    won_once = True if argv[1] == 'unlock' else False

with open("/usr/share/dict/words") as word_file:
    words = word_file.readlines()


def get_user_guess():
    valid_guess = False

    while not valid_guess:
        guess = input("Guess a letter.\n>> ")
        if guess.isalpha() and len(guess) == 1:
            valid_guess = True
    return guess.lower()


def get_random_word():
    if won_once:
        evil_mode = input(
                "Wouldn't you like more of a challenge?\nYou can now play Evil Mode! Give it a try? ('Y' or 'N')\n>> ")
        while evil_mode != 'Y' and evil_mode != 'N':
            evil_mode = input("What was that? Please enter 'Y' or 'N'.")

        if evil_mode == 'Y':
            play_evil_game()
        else:
            pass

    valid_word = False
    word = random.choice(words).strip()
    game_mode = input("""Please select the level of difficulty.\n
            'H' = Hard (Words 10+ characters)\n
            'N' = Normal (Words from 6 - 9 characters)\n
            'E' = Easy (Words from 4 - 6 characters)\n>> """)

    while game_mode != 'H' and game_mode != 'N' and game_mode != 'E':
        game_mode = input("Please enter 'H', 'N', or 'E'.\n>> ")

    while not valid_word:
        word = random.choice(words).strip()
        if game_mode == 'H' and len(word) >= 10:
            valid_word = True
        elif game_mode == 'N' and len(word) in range(6, 10):
            valid_word = True
        elif game_mode == 'E' and len(word) in range(4, 6):
            valid_word = True

    return word.lower()


def update_remaining_list(guess, remaining):
    """for use in Evil mode. Takes guess and the remaining possible word
    list as arguments and returns an updated remaining words list and the
    positions of any correctly guessed letters."""
    user_guess = guess
    remaining_words = remaining
    word_families = {}
    for word in remaining_words:
        key = ''.join(user_guess if char == user_guess else '-' for char in word)
        if key not in word_families:
            word_families[key] = []
        word_families[key].append(word)

    sorted_families = sorted(word_families.keys(), key=lambda k: len(word_families[k]), reverse=True)

    index = sorted_families[0]
    new_remaining = word_families[sorted_families[0]]

    word_families.clear()

    return index, new_remaining


def play_evil_game():
    turns = 8
    word_list = [word.strip().lower() for word in words]
    picked_word = random.choice(word_list)
    hidden_word = list('-'*len(picked_word))
    remaining_words = [word for word in word_list if len(word) == len(picked_word)]
    letters_used = []

    print(''.join(hidden_word), "{} letters.".format(len(picked_word)))

    while ("-" in ''.join(hidden_word)):
        guess = get_user_guess()

        if guess in letters_used:
            print("You've already guessed that letter!")

        else:
            guess_pos = update_remaining_list(guess, remaining_words)[0]
            if guess not in guess_pos:
                turns -= 1
                letters_used.append(guess)
                print("Sorry, '{}' is not there! You have {} turns left.".format(guess, turns))
                remaining_words = update_remaining_list(guess, remaining_words)[1]
                picked_word = random.choice(remaining_words)
                if turns == 0:
                    print("Game over. The word was {}.".format(picked_word))
                    play_again()
            elif guess in guess_pos:
                letters_used.append(guess)

                for idx in range(len(hidden_word)):
                    if hidden_word[idx] == '-' and guess_pos[idx] == guess:
                        hidden_word[idx] = guess

                remaining_words = update_remaining_list(guess, remaining_words)[1]
                picked_word = random.choice(remaining_words)

        print(''.join(hidden_word))
        print("Letters used: " + " ".join(sorted(letters_used)))

    else:
        print("You win! The word was {}.".format(picked_word))
        play_again()


def play_game():
    global won_once
    turns = 8
    word = get_random_word()
    hidden_word = list('-'*len(word))
    letters_used = []

    # for debugging
    # print(word, len(word))
    print(''.join(hidden_word), "{} letters.".format(len(word)))

    while ''.join(hidden_word) != word:
        guess = get_user_guess()

        if guess in letters_used:
            print("You've already guessed that letter!")
        elif guess not in word:
            turns -= 1
            letters_used.append(guess)

            print("Sorry '{}' is not there! You have {} turns left.".format(guess, turns))
            if turns == 0:
                print("Game over. The word was {}.".format(word))
                play_again()
        elif guess in word:
            letters_used.append(guess)

            for idx in range(len(word)):
                if guess == word[idx]:
                    hidden_word[idx] = word[idx]

        print(''.join(hidden_word))
        print("Letters used: " + " ".join(sorted(letters_used)))

    else:
        won_once = True
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
