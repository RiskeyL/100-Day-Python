# def great():
#     print("This is a great function!")
#     print("It does wonderful things.")
#     print("You should definitely use it!")


# def great(name):
#     print(f"This is a great function, {name}!")
#     print("It does wonderful things.")
#     print("You should definitely use it!")

# great("Alice")


# def great_with(name, location):
#     print(f"Hello, {name}!")
#     print(f"What is it like in {location}?")

# # great_with(name = "Bob", location = "New York")
# great_with("Bob", "New York")


# def calculate_love_score(name1, name2):
    
#     true_score1 = 0
    
#     love_score1 = 0

#     true_score2 = 0

#     love_score2 = 0
    
#     for letter1 in name1:

#         if letter1.lower() in "true":
            
#             true_score1 += 1
            
#         if letter1.lower() in "love":
            
#             love_score1 += 1

#     for letter2 in name2:

#         if letter2.lower() in "true":
            
#             true_score2 += 1
            
#         if letter2.lower() in "love":
            
#             love_score2 += 1
    
#     true_score = true_score1 + true_score2

#     love_score = love_score1 + love_score2

#     true_love_score = str(true_score) + str(love_score)
    
#     print(true_love_score)

# calculate_love_score("Alice", "Bob")

# def calculate_love_score(name1, name2):

#     combined_name = name1 + name2
    
#     true_score = 0
    
#     love_score = 0
    
#     for letter in combined_name:

#         if letter.lower() in "true":
            
#             true_score += 1
            
#         if letter.lower() in "love":
            
#             love_score += 1

#     print(f"{true_score}{love_score}")

# calculate_love_score("Anne", "Bob")

def encrypt(text, shift):

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    new_text_list = []

    for letter in text:

        if letter not in alphabet:
            new_text_list.append(letter)

        else:

            letter_location = alphabet.index(letter)

            if letter_location + shift > 25:

                new_letter = alphabet[(letter_location + shift) - 26]

            else:
                new_letter = alphabet[letter_location + shift]
                
            new_text_list.append(new_letter)

    new_text = ''.join(new_text_list)

    print(new_text)

def decrypt(text, shift):

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    new_text_list = []

    for letter in text:

        if letter not in alphabet:
            new_text_list.append(letter)

        else:

            letter_location = alphabet.index(letter)

            if letter_location - shift < 0:

                new_letter = alphabet[26 + (letter_location - shift)]

            else:

                new_letter = alphabet[letter_location - shift]

            new_text_list.append(new_letter)

    new_text = ''.join(new_text_list)

    print(new_text)    

def caesar(text, shift, direction):

    if direction == "encode":
        encrypt(text, shift)

    elif direction == "decode":
        decrypt(text, shift)

    else:
        print("Invalid direction. Please choose 'encode' or 'decode'.")

while more == "yes":

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    text = input("Type your message:\n").lower()

    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    more = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()  