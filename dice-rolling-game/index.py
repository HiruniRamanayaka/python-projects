import random

while True :
    selectChoice = input('Roll the dice? (y/n): ')
    choice = selectChoice.lower()
    if choice == 'y':
        die1 = random.randint(1,6)          # Generate a random number between 1 and 6, randint-random integer
        die2 = random.randint(1,6)
        print(f'({die1}, {die2})')       # why f'' -> formatting string with variables
    elif choice == 'n':
        print('Thanks for playing!')
        break
    else: 
        print('Invalid choice')