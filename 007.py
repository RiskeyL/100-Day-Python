# TODO-1

import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

placeholder = ""

for letter in chosen_word:
    placeholder += "_"

# TODO-2

guess = input("Guess a letter:").lower()

# TODO-3

display = ""

left_lives = 5


while left_lives > 0:
    
    for letter in chosen_word: 
        if letter == guess: 
            display += letter
        elif letter != guess and letter != "_":
            display = display
        else:
            display += "_"
            left_lives -= 1

print(display)