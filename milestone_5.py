import random

word_list = ['apple', 'orange', 'kiwi', 'peach', 'melon']

class Hangman:
    # initialise method
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word_guessed = []
        self.target_word = random.choice(word_list)
        self.num_letters = len(set(self.target_word))
        self.list_of_guesses = []
        
        for letter in range(len(self.target_word)):
            self.word_guessed.append('_')
        
    # method that checks to see if the inputted letter matches any in the target word
    def check_guess(self, letter_guess):
        letter_guess = letter_guess.lower()

        if letter_guess in self.target_word:
            print(f'Good guess! {letter_guess} is in the word \n')
            for letter in range(len(self.target_word)):
                if self.target_word[letter] == letter_guess:
                    self.word_guessed[letter] = letter_guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry, {letter_guess} is not in the word. Try again.\n')
            print(f'You have {self.num_lives} lives left')

            
    # method that checks that the inputted value is a single aplohabetical character
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
                
 # Method creates a game and assigns the word_list and number of lives
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True: 
        print(''.join(game.word_guessed))
        if game.num_lives == 0:
            print('You Lost!')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif game.num_lives != 0 and game.num_letters <= 0:
            print('Congratulations. You won the game!')
            break


play_game(word_list)