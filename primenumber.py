# checking a number Prime or not

# Getting input from user
num = int(input('Enter a number: '))
# Defining a function

def prime_or_not(num):

    for i in range(2,num):
        # Condition for nonPrime numbers
        if num % i ==0:
            print(num,'is not a Prime Number')
            break
            # breaking the loop if it is divisible by any number
    #  this for 'for loop'
    # condition for Prime numbers
    else:
        print(num,'is a Prime Number')

# Calling the same function
prime_or_not(num)
