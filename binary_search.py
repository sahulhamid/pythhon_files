# Getting a list from user
# You can also take your own list or an array
#Creating an Empty list
lis = []

# position initially at -1
pos = -1

# Asking length of thr length of list
len_lis = int(input('Enter the Length of List: '))

# Iterating a Loop
i = 0
while i < len_lis:
    num = int(input('Enter values: '))
    lis.append(num)
    i+=1


#sorting ths given list
list = sorted(lis)
print(list)
# asking the user to enter a number to find
num = int(input('Enter a Number to Search: '))

# Defining the Function of Binary Search

def binary_search(list,num):

    # Lower value
    # Upper Value
    l = 0
    u = len(list) - 1
    # Iterating a Infinite loop
    while l <= u:
        mid = (l+u)//2
        if list[mid] == num:
            # Getting the position
            global pos
            pos = mid
            return True
        else:
            if num > list[mid]:
                l = mid+1
            else:
                u = mid-1
    return False

# Calling the Function

# Building Logic
if binary_search(list,num):
    print('Number Found at',pos+1)
else:
    print("Not Found")

