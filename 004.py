import random

# random.randint(2,10)
#
# random.random()

# random_num = random.random() * 10
#
# print(random_num)
#
# if random_num < 5:
#     print("Heads")
#
# else:
#     print("Tails")

# import random
#
# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#
# random_friend = random.randint(0,4)
#
# print(friends[random_friend])

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]

# print(dirty_dozen[0])



# test

import random

choice_number = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
             
rock = "石头"

paper = "布"

scissors = "剪刀"

game_options = [rock, paper, scissors]

user_choice = game_options[choice_number]

computer_choice_number = random.randint(0, 2)

computer_choice = game_options[computer_choice_number]

print(choice_number)

print(user_choice)

print("Computer chose:")

print(computer_choice)
 
if choice_number == 0:
    if computer_choice_number == 0:
        print("Let's call it a draw!")
    elif computer_choice_number == 1:
        print("You lose!")
    else:
        print("You win!")
elif choice_number == 1:
    if computer_choice_number == 0:
        print("You win!")
    elif computer_choice_number == 1:
        print("Let's call it a draw!")
    else:
        print("You lose!")
else:
    if computer_choice_number == 0:
        print("You lose!")
    elif computer_choice_number == 1:
        print("You win!")
    else:
        print("Let's call it a draw!") 