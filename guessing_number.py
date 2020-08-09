# Importing random module
import random
#getting a random number from the User
ran_number = random.randint(1,15)
print(ran_number)

# Getting a Number From User
num = int(input('Enter a Number: '))

# No of turns that a player can choose a number
turns = 12

#Checking the input matches or not
if num == ran_number:
    print("Guess is correct")
else:
    # Running an infinite loop
    while num !=ran_number:
        num = int(input('Enter a Number again!: '))



