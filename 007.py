import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

placeholder = ""

for letter in chosen_word:
    placeholder += "_"

print(placeholder)

game_over = False

correct_guesses = []

while not game_over:

    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word: 

        if letter == guess: 
            display += letter
            correct_guesses.append(guess)

        elif letter in correct_guesses:
                display += letter

        else:
            display += "_"

    print(display)
    
    if "_" not in display:
        game_over = True
        print("You win!")