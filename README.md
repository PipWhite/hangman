# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

###Usage
#### word_list
The word_list variable is all the possible words you could be guessing from. Words of your choice may be added or removed from this list in the code, however the must all be lowercase and not contain any numbers or special characters for the game to work (must only contain lowercase alphabetical characters).

### Playing the game
To play the game you can simply run the milestone_5.py file and follow the instructions give.


### Methods

#### ask_for_input()
While loop asks for the user to input a single letter. <br>
Checks that the input has a length of one and is alphabetical.  <br>
Prints a response if the input is invalid.  <br>
While loop is broken if input is valid.  <br>
Calls the check_guess() method with the users input as a parameter.  <br>

#### check_guess(letter_guess)
Takes the users guess as a parameter.
Converts the guess to lowercase.
checks if the letter is in the target word and prints an appropriate response


