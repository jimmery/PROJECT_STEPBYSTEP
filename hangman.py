# Name: Arkadip Saha
# MIT Username: Hahahahahaha nope.
# 6.S189 Project 1: Hangman template
# hangman_template.py

# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *
from hangman_lib import *
print "Art made by sk"

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
    word=words_dict[randrange(0,len(words_dict))]
    return word

# end of helper code
# -----------------------------------


# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES 
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
    #valid = False
    #for char in secret_word:
    #    if char in letters_guessed:
    #        valid = valid | True
    #return valid

    if print_guessed() == secret_word:
        return True
    else:
        return False

def print_guessed():
    '''
    Prints a string that contains the word with a dash "-" in
    place of letters not guessed yet. 
    '''
    global secret_word
    global letters_guessed
    
    ####### YOUR CODE HERE ######
    character_list = []
    for char in secret_word:
        if char in letters_guessed:
            character_list.append(char)
        else:
            character_list.append("-")
    print join(character_list, "")
    return join(character_list, "")

def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0

    # Update secret_word. Don't uncomment this line until you get to Step 8.
    secret_word  = get_word()

    ####### YOUR CODE HERE ######
    while mistakes_made < MAX_GUESSES:
        guesses_left = MAX_GUESSES - mistakes_made
        print "*************************************************************"
        if guesses_left == 1:
            print str(guesses_left) + " guess left!"
        else:
            print str(guesses_left) + " guesses left!"
        print "You have guessed:" + str(letters_guessed)
        print_hangman_image(mistakes_made)
        print_guessed()

        letter = lower(raw_input("Guess a letter! "))
        if letter in letters_guessed:
            print "You already guessed that letter! Choose another."
            mistakes_made += 1
        else:
            letters_guessed.append(letter)
            if letter in secret_word:
                print "Congratulations! That letter is in the secret word!"
            else:
                print "Oops, that's not in the secret word."
                mistakes_made += 1
        if word_guessed() == True:
            print "You have guessed the secret word!"
            break
    if mistakes_made == MAX_GUESSES:
        print_hangman_image(6)
        print "You lose. GAME OVER."
    print "The word was " + secret_word + "."
                
    return None

play_hangman()
