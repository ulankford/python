# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
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
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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
    # FILL IN YOUR CODE HERE...
    count=0
    total=0
    for char in lettersGuessed:
        count=secretWord.count(char)
        total+=count
    if (total >= len(secretWord)):
        return True
    else:
        return False
    



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessedstring = ''
    x = len(secretWord)
    u = 0
    while u < x:
        guessedstring=guessedstring+'_ '
        u+=1
    l= list(guessedstring)

    for char in lettersGuessed:
        a=0
        for i in secretWord:
            if char == i:
                l[a]=char
            else:
                pass
            a+=2
        guessedstring="".join(l)
    return guessedstring




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    s='abcdefghijklmnopqrstuvwxyz'
    
    for char in lettersGuessed:
        for i in s:
            if i == char:    
                s=s.replace(i,'')
                break
            else:
                pass
    return s
    

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
    # FILL IN YOUR CODE HERE...
    guesses = 8
    lettersGuessed=''
    mistakesMade=0
    comparestring=getGuessedWord(secretWord, '')
    
    print"Welcome to the game of Hangman!"
    print"I am thinking of a word that is %d letters long" % len(secretWord)
    
    while mistakesMade != 8:
        print"-------------"
        print"You have %d guesses left." % guesses
        print"Available Letters: ", getAvailableLetters(lettersGuessed)
        guess=raw_input('Please guess a letter: ')
        guess=guess.lower()
        
        if lettersGuessed.find(guess) >= 0:
            print "Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed)
            
        else:
            lettersGuessed+=guess
            if comparestring == getGuessedWord(secretWord, lettersGuessed):
                print "Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed)
                
                mistakesMade+=1
                guesses-=1
            else:
                print "Good guess: ", getGuessedWord(secretWord, lettersGuessed)
                
                comparestring=getGuessedWord(secretWord, lettersGuessed)
        
        #Is the word guessed correctly? Use the function to check, if not continue game
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print"-------------"
            print "Congratulations, you won!"
            break
        elif guesses == 0:
            print" Sorry, you ran out of guesses. The word was %s ." % secretWord
        else:
            pass



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

#secretWord = chooseWord(wordlist).lower()
secretWord="y"
hangman(secretWord)