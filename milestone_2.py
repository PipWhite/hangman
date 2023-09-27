import random

word_list = ['apple', 'orange', 'kiwi', 'peach', 'melon']
print(word_list)

choice = random.choice(word_list)
word = choice
print(word)

guess = input('Enter a single letter: ')

if len(guess) == 1 and guess.isalpha() == True:
    print('Good guess')
else:
    print('Oops! That is not a valid input')