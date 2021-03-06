# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import re
import string
#
WORDLIST_FILENAME = "words.txt"
#
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    counter = 0
    for i in secretWord:
        if i in lettersGuessed:
            counter += 1
    if counter == len(secretWord):
        return True
    else:
        return False

# -----------------------------------
# isWordGuessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's'])  #False
# isWordGuessed('pineapple', ['o', 'i', 'g', 's', 'e', 'u', 'z', 'w', 'p', 'f']) #False
# -----------------------------------





# -----------------------------------
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    showUser = []
    for i in secretWord:
        showUser.append("_ ")
    #print(showUser)

    for i in lettersGuessed:
            if i in secretWord:
                index = 0
                while index < len(secretWord):
                    index = secretWord.find(i, index)
                    if index == -1:
                        break
                    showUser[index] = i
                    index += 1
    return " ".join(showUser)
# -----------------------------------
# getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's'])
# -----------------------------------




# -----------------------------------
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    availableLetters = list(string.ascii_lowercase)
    #print(availableLetters)
    for letter in lettersGuessed:
        #print('current letter: ' + letter)
        if letter in availableLetters:
            #print('current letter IS in alphabet ')
            availableLetters.remove(letter)
    return "".join(availableLetters)

# -----------------------------------
#should return the letters in alphabetical order
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(getAvailableLetters(lettersGuessed))
# -----------------------------------




# -----------------------------------
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print("-----------")

    lettersGuessed = []
    numGuesses = 8

    while numGuesses > 0:
        availableLetters = getAvailableLetters(lettersGuessed)
        print("You have " + str(numGuesses) + " guesses left.")
        print("Available letters: " + str(availableLetters))

        userInput = raw_input("Please guess a letter: ").lower()
        lettersGuessed.append(userInput)
        isInTheWord = getGuessedWord(secretWord, lettersGuessed)

        if (userInput not in availableLetters):
            print("Oops! You've already guessed that letter: " + str(isInTheWord))
        else:
            if userInput in isInTheWord:
                print("Good guess: " + str(isInTheWord))
                if isWordGuessed(secretWord, lettersGuessed):
                    print("Congratulations, you won!")
                    break
            else:
                print("Oops! That letter is not in my word: " + str(isInTheWord))
                numGuesses -= 1
        print("-----------")

    if isWordGuessed(secretWord, lettersGuessed):
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was else.")
        print("The word was: " + secretWord)


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
# -----------------------------------
