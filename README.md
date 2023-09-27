# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

### Methods

#### ask_for_input()
While loop asks for the user to input a single letter.
Checks that the input has a length of one and is alphabetical.
Prints a response if the input is invalid.
While loop is broken if input is valid.
Calls the check_guess() method with the users input as a parameter.

#### check_guess(letter_guess)
Takes the users guess as a parameter.
Converts the guess to lowercase.
checks if the letter is in the target word and prints an appropriate response

### Usage
1. Starting the game will randomly select a word from the word list
2. Enter a single alphabetical character when prompted
3. Input is checked to ensure it is a single alphabetical character. While loop is broken when a valid input is given.
4. Input is then compared to the target word to see if it is part of the word or not.
