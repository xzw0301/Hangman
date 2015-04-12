# Name:
# Section:
# 6.189 Project 1: Hangman template
# hangman_template.py

# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *
dir()

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = split(line)
    print "  ", len(wordlist), "words loaded."
    print 'Enter play_hangman() to play a game of hangman!'
    return wordlist

# actually load the dictionary of words and point to it with
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word = words_dict[randrange(0,len(words_dict))]
    return word


# end of helper code
# -----------------------------------


# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES
secret_word = get_word()
letters_guessed = []

# From part 3b:
def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed

    ####### YOUR CODE HERE ######

    for val in secret_word:
        if val not in letters_guessed:
            return False
    return True


def print_guessed():
    '''
    Prints out the characters you have guessed in the secret word so far
    '''
    global secret_word
    global letters_guessed

    ####### YOUR CODE HERE ######
    character_list = ['-'] * len(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            character_list[i] = secret_word[i]
    return ''.join(character_list)

def print_hangman_image(mistakes = 6):
    """Prints out a gallows image for hangman. The image printed depends on
  the number of mistakes (0-6)."""
    print 'Art created by sk.'
    if mistakes <= 0:
        print''' ____________________
| .__________________|
| | / /
| |/ /
| | /
| |/
| |
| |
| |
| |
| |
| |
| |
| |
| |
| |
| |
| |
""""""""""""""""""""""""|
|"|"""""""""""""""""""|"|
| |                   | |
: :                   : :
. .                   . .'''

    elif mistakes == 1:
        print''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |
| |
| |
| |
| |
| |
| |
| |
| |
| |
""""""""""""""""""""""""|
|"|"""""""""""""""""""|"|
| |                   | |
: :                   : :
. .                   . .'''
    elif mistakes == 2:
        print''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |          -`--'
| |          |. .|
| |          |   |
| |          | . |
| |          |   |
| |          || ||
| |
| |
| |
| |
""""""""""""""""""""""""|
|"|"""""""""""""""""""|"|
| |                   | |
: :                   : :
. .                   . .'''
    elif mistakes == 3:
        print''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |         .-`--'
| |        /Y . .|
| |       // |   |
| |      //  | . |
| |     ')   |   |
| |          || ||
| |
| |
| |
| |
""""""""""""""""""""""""|
|"|"""""""""""""""""""|"|
| |                   | |
: :                   : :
. .                   . .'''
    elif mistakes == 4:
        print''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |         .-`--'.
| |        /Y . . Y\\
| |       // |   | \\\\
| |      //  | . |  \\\\
| |     ')   |   |   (`
| |          || ||
| |
| |
| |
| |
""""""""""""""""""""""""|
|"|"""""""""""""""""""|"|
| |                   | |
: :                   : :
. .                   . .'''
    elif mistakes == 5:
        print''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |         .-`--'.
| |        /Y . . Y\\
| |       // |   | \\\\
| |      //  | . |  \\\\
| |     ')   |   |   (`
| |          ||'||
| |          ||
| |          ||
| |          ||
| |         / |
""""""""""""""""""""""""|
|"|"""""""""""""""""""|"|
| |                   | |
: :                   : :
. .                   . .'''
    else: #mistakes >= 6
        print''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |         .-`--'.
| |        /Y . . Y\\
| |       // |   | \\\\
| |      //  | . |  \\\\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \\
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :
. .          `'       . .'''

def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0

    # Update secret_word. Don't uncomment this line until you get to Step 8.
    # secret_word  = get_word()

    ####### YOUR CODE HERE ######

    MAX_GUESSES = 6
    letters_guessed = []
    while not word_guessed() and mistakes_made < MAX_GUESSES:
        print '%s guesses left' % str(MAX_GUESSES - mistakes_made)
        print_hangman_image(mistakes_made)
        print print_guessed()
        letter = lower(raw_input('Enter the letter you guessed:'))
        while letter in letters_guessed:
            letter = lower(raw_input('Letter already guesses, please enter new one:'))
        if letter not in secret_word:
            mistakes_made += 1
        letters_guessed.append(letter)

    print 'Secret word is %s' % secret_word
    if mistakes_made >= MAX_GUESSES:
        print "Sorry, you lost! You do not have any more guesses."
    else:
        print "Congratulations!"

play_hangman()