# Building a Guessing word game(hangman) with random module
import random
# creating a list of words

list_of_words = ['python', 'swift', 'rudy', 'perl', 'sql', 'html','cprog','kotlin']

# letting the computer to choose word
word = random.choice(list_of_words)

# Getting dashes in alist format
guess_word = list('_'*len(word))

# joining the dashes by using the join method
join_guess_word = ''.join(guess_word)

# player should get 10 turns
turns = 10

# running a infinite loop(while loop) till 10 turns
while turns > 0:
    # Getting a letter from the player
    guess_letter = input('Enter a character: ')
    # Checking the character is in  word
    if guess_letter in word:
        # Finding the index of the guessing character
        f = word.find(guess_letter)
        # changing in list of guess_word
        guess_word[f] = guess_letter
        # joining the updated guess word
        join_guess_word = guess_word
        print(join_guess_word)
        turns-=1
        # checking for winning condition
        if join_guess_word == word:
            print('You win the game')
            # if player guessed the correct word then stop iterating
            turns = 0



