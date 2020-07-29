# Finding maximum number in a list by Sorting

import array

# creating an array
arr = array.array('i',[])

# asking lengtyh of array
len_arr = int(input("Enter the legthof array: "))

#using a for loop getting inputs from array
for i in range(len_arr):
    # geting the numbers
    n = int(input('Enter values: '))
    arr.append(n)
print(arr)

# sorting the given input
s = sorted(arr)

# here we sorted the given array
# printing the largest values

# we can say max(s)

