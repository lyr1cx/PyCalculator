# My_first_basic_calculator

# Asks the user for their name
name = input("Hi, what is your name? ")
print("Nice to meet you " + name + "! Please follow the prompts below...")

# Asks the user to provide input for basic addition
num1 = input("Enter a random number: ")
num2 = input("Enter another random number: ")
num3 = input("Enter yet again, another number: ")

# Addition results displayed
result = int(num1) + int(num2) + int(num3)
print("Result:", result)

# Printing a thank you to the end_user
print("Congratulations " + name + "!" + " You've used my simple, yet overcomplicated calculator!")
print("See you next time!")
