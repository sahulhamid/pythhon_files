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

