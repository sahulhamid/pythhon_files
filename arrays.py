import array
# first we are creating an empty array
arr = array.array('i',[])
# getting the length of the array from the user
arr_len=int(input('Enter the lenght of an array: '))

for i in range(arr_len):
    # appending the values
    x=int(input('Enter the values: '))
    arr.append(x)

print(arr)

# asking the user to enter a value
f = int(input('Enter a value to find: '))

# here i am using while you can use for loop which is much easier than

# searching using  the while loop
i = 0
# introducing a constant to find a index of the value
k = 0
while i < len(arr):
    # checking for the number
    if f == arr[i]:
        print('Index of the given value is',k)
    k+=1
    i+=1

# There is a simple built in function ' index' you can use that