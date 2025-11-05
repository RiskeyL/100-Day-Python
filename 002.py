# print("hELLO"[2])

# print(122 + 456)

# print("122" + "122")

# print(12_345_453)

# print(12,345,453)

# Boolean values are case-sensitive
# print(False)


# print(len("123454"))

# print(type(123.456))

# print("Number of letters in your name: " + str(len(input("Enter your name\n"))))

# print(3 * (3 + 3) / 3 - 3)


# score = 1

# print(f"Your score is {score}")


print("Welcome to the tip calculator!")

a = float(input("What was the total bill?"))

b = int(input("How much tip would you like to give? 10, 12, or 15?"))

c = int(input("How many people to split the bill?"))

d = a * (1 + b / 100) / c

print(f"Each person should pay: {round(d,2)}")
