# We are going to find whether given word is palindrome or not

# Getting word from the user
word = input('Enter a word: ')

# Definig a function
def palindrome(word):
    # Condition for Palindrome
    if word == word[::-1]:
        print(word ,'is Palindrome')
    else:
        print(word ,'is Not a palindrome')


# Calling the Function
