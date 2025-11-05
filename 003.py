print("Welcome to Python Pizza Deliveries!")

size = input("What size do you want? S, M, or L?")

bill = 0

if size == "S":

    bill = 15

elif size == "M":

    bill = 20

elif size == "L":

    bill = 25

pepperoni = input("Would you like pepperoni? (Y/N) ")

if pepperoni == "Y" and size == "S":

    bill += 2

elif pepperoni == "Y" and size == "M":

    bill += 3

elif pepperoni == "Y" and size == "L":

    bill += 3

extra_cheese = input("Would you like extra_cheese? (Y/N) ")

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}.")
