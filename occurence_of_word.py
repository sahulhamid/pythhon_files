# Creating a List of words
# you can take your own list or get if from user
words = ['python','java','python','python','javascript','java','java',]

# Defining a function
def No_Of_Occur(lis):
    #Counter
    counter=[]
    # Checking the count of each element in the list
    for i in lis:
        # storing in a variable
        c=lis.count(i)
        counter+=[c]

    # Getting the maximum value of the counter
    max_count = max(counter)

    #checking the maximum value with the count using a loop
    # storing in a third variable
    st = []
    for j in lis:
        if max_count == lis.count(j):
            # stored in a third variable
            st+=[j]

    # Converting the stored data into set of list because reduce repeatation
    list_st = list(set(st))
    # iterating a loop
    for k in list_st:
        print(k)

# Calling a loop
No_Of_Occur(words)



