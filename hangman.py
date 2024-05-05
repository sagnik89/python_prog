import random
import time

word_list = ["Food", "Code", "Eat", "Program"]
chosen_word = random.choice(word_list).lower()

life = 8
check = False

res = ""


def display_current():
    for i in display:
        print(i, end=" ")
    print()

def checker():
    c = ""
    for i in display:
        c += i
    if c == chosen_word:
        return True
    else:
        return False


# initializing display list for entering and displaying the blank spaces
display = []

for letters in chosen_word:
    display += "_"

# to check the guesses of the user with the letters of the word

# print(f'Chosen word is: {chosen_word}')

while life > 0:
    guess = input("Enter the guess: ")

    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if guess == letter:
            display[i] = letter
            check = True

    display_current()
    if checker():
        life = -1
        print("You won the game! ")
    else:
        if not check:
            life -= 1
            print("Wrong Guess !!!")
            print(f'Lives left = {life}')
        else:
            check = False


if life == 0:
    print("You have failed to guess the word! ")













