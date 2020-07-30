# Getting a list from user
# You can also take your own list or an array
#Creating an Empty list
lis = []

# Asking length of thr length of list
len_lis = int(input('Enter the Length of List: '))

# Iterating a Loop
i = 0
while i < len_lis:
    num = int(input('Enter values: '))
    lis.append(num)
    i+=1
print(lis)

# asking the user to enter a number to find
n = int(input('Enter a Number to Search: '))

# Defining the Function of Binary Search