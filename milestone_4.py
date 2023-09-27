import random

word_list = ['apple', 'orange', 'kiwi', 'peach', 'melon']

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word_guessed = []
        self.target_word = random.choice(word_list)
        self.num_letters = len(set(self.target_word))
        self.list_of_guesses = []
        
        
        print(f'Target Word: {self.target_word}')
        print(f'Unique letters: {self.num_letters}')
        print(f'Lives: {self.num_lives}')

        
        for i in range(len(self.target_word)):
            self.word_guessed.append('_')
        print(self.word_guessed)

    def check_guess(self, letter_guess):
        letter_guess = letter_guess.lower()

        if letter_guess in self.target_word:
            print(f'Good guess! {letter_guess} is in the word')
            for i in range(len(self.target_word)):
                if self.target_word[i] == letter_guess:
                    self.word_guessed[i] = letter_guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry, {letter_guess} is not in the word. Try again.')
            print(f'You have {self.num_lives} lives left')

            
    
    def ask_for_input(self):
        while True:
            letter_guess = input('Enter a single letter: ')
            if len(letter_guess) != 1 or letter_guess.isalpha() == False:
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif letter_guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.list_of_guesses.append(letter_guess)
                break
        self.check_guess(letter_guess)
                
        

my_game = Hangman(word_list)
my_game.ask_for_input()

