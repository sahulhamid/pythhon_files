# Importing random module
import random
#getting a random number from the User
ran_number = random.randint(1,15)
print(ran_number)

# printing the numbers
print("You have select number from 1 to 15")

# Getting a Number From User
num = int(input('Enter a Number: '))

# No Fo turns User can play
turns = 12

#Checking the input matches or not
if num == ran_number:
    print("You are Intelligent,Guess is correct")
else:
    print('Game Starts')
    # Running an infinite loop
    while turns >=0 :
        num = int(input('Enter a Number again!: '))
        # checking the the num and ran_num once again
        if num == ran_number:
            print('Great, Guess is correct')
            turns=0
        else:
            print('Remaining Turns are:',turns)
        turns-=1



