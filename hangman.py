# tiy hangman project
# import random

word = 'bathroom'

hidden_word = list('_'*len(word))

print(word, len(word))
print(hidden_word, len(hidden_word))


def get_user_guess():
    guess = input("Guess a letter.\n>> ").lower()
    return guess

while ''.join(hidden_word) != word:
    guess = get_user_guess()

    for idx in range(len(word)):
        if guess == word[idx]:
            hidden_word[idx] = word[idx]

    print(word)
    print(''.join(hidden_word))

print(word)
print(''.join(hidden_word))
