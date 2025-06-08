# Generate a random number

# Loop
# Ask the user to make a quess
# Check if the number is higher or lower than the user's guess
#   If number > guess
#     print("Too high, try again")
#   If number < guess
#     print("Too low, try again")
#   If number == guess
#     print("You got it!")

import random

number_to_guess = random.randint(1, 100)

while True:
    guess = int(input("Guess a number between 1 and 100: "))

    if guess > number_to_guess:
        print("Too high, try again")
    elif guess < number_to_guess:
        print("Too low, try again")
    else :
        print("Congratulations! You got it!")
        break

print ("Thanks for playing!") 


# Can be updated to check whether wnter number or not. Use Exceptions
    