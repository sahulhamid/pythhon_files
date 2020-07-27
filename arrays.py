import array
# first we are an empty array
arr = array.array('i',[])
# getting the length of the array from the user
arr_len=int(input('Enter the lenght of an array: '))

for i in range(arr_len):
    # appendind the values
    x=int(input('Enter the values: '))
    arr.append(x)

print(arr)


