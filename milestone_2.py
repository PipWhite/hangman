import random

def check_guess(letter_guess):
    letter_guess = letter_guess.lower()

    if letter_guess in target_word:
        print(f'Good guess! {letter_guess} is in the word')
        
    else:
        print(f'Sorry, {letter_guess} is not in the word. Try again.')


def ask_for_input():
    while True:
        letter_guess = input('Enter a single letter: ')
        if len(letter_guess) == 1 and letter_guess.isalpha() == True:
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
    check_guess(letter_guess)
    
    




word_list = ['apple', 'orange', 'kiwi', 'peach', 'melon']
print(word_list)

word_choice = random.choice(word_list)
target_word = word_choice
print(target_word)

ask_for_input()

