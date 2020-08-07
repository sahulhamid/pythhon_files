# Creating a List of words
words = ['python','java','python','javascript','java','java']

# Defining a function
def No_Of_Occur(lis):
    #Counter
    counter=[]
    # Checking the count of each element in the list
    for i in lis:
        # storing in a variable
        c=lis.count(i)
        counter+=[c]

