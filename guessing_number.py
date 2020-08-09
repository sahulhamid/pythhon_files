# Importing random module
import random
#getting a random number from the User
ran_number = random.randint(1,15)
print(ran_number)

# printing the numbers
print("You have select number from 1 to 15")

# Getting a Number From User
num = int(input('Enter a Number: '))

# No of turns that a player can choose a number
turns = 12

#Checking the input matches or not
if num == ran_number:
    print("You are Intelligent,Guess is correct")
else:
    # Running an infinite loop
    while num !=ran_number:
        num = int(input('Enter a Number again!: '))
        # checking the the num and ran_num once again
        if num == ran_number:
            print('Great, Guess is correct')



