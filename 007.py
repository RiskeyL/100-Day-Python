import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

placeholder = ""

for letter in chosen_word:
    placeholder += "_"

print(placeholder)

game_over = False

correct_guesses = []

stage = ["You lose!", "1 life left", "2 lives left", "3 lives left", "4 lives left"]

lives = 5

while not game_over:

    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word: 

        if letter == guess: 
            display += letter
            correct_guesses.append(guess)
            print("Correct guess!")

        elif letter in correct_guesses:
                display += letter

        else:
            display += "_"

    print(display)
    
    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong Guess! {stage[lives]}")
        if lives == 0:
            game_over = True
        
    # Solution B
    #
    # if guess not in chosen_word:
    #     stage.pop(0)
    #     print(stage[0])
    #
    #     if len(stage) == 1:
    #         game_over = True
    
    if "_" not in display:
        game_over = True
        print("You win!")   