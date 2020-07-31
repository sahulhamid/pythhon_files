# Bubble sorting

# creating a List
lis = [5, 7, 3, 4, 2, 9]
# we can take list from the user

# Defining a Function
def bubble_sort(num_list):
    # Iterating a Loop
    for i in range(len(num_list)-1,0,-1):
        # Iterating a for single values
        for j in range(i):
            if num_list[j] > num_list[j+1]:
                # Swaping my vales

