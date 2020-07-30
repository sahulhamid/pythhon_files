# We are going to discuss about Linear Search

num_lis = [45,56,78,1,23,56,89]

# Defining a Function
def linear_search(list):
    # asking a Number From User
    num=int(input('Enter the number to find: '))
    # Running a loop
    for i in range(len(list)):
        if num == list[i]:
            print('Number Found at',i)
            break
    else:
        print("Number Not Found")


# Calling te function
linear_search(num_lis)

