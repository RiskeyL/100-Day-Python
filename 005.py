import random

# random_list = [random.randint(1, 198) for i in range(50)] + [199]

# max_number = 0

# for number in random_list:
#     if number > max_number:
#         max_number = number
        
# print(max_number)

# sum_number = 0

# for number in range(1, 101):
#     sum_number += number

# print(sum_number)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letters_pick = []

numbers_pick = []

symbols_pick = []

disordered_pwd = ""

for i in range(4):
    
    letters_pick.append(random.choice(letters))

for i in range(2):

    numbers_pick.append(random.choice(numbers))
    
for i in range(3):

    symbols_pick.append(random.choice(symbols))

generated_pwd = letters_pick + numbers_pick + symbols_pick

for i in range(9):
    item = random.choice(generated_pwd)
    disordered_pwd += item
    generated_pwd.remove(item)
    
print(disordered_pwd)
