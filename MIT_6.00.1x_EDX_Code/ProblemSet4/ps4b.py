from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxscore=0
    # Create a new variable to store the best word seen so far (initially None)
    bestword=None 
    wordfound=None 
    # For each word in the wordList
    for w in wordList:
        wordfound=isValidWord(w, hand, wordList)
        if wordfound == True:
            score=getWordScore(w, n)
            if score>maxscore:
                maxscore=score    
                bestword=w
                
            '''vowelCount=0
            for letter in VOWELS:
                if hand.get(letter)>0:
                    vowelCount+=1
            if vowelCount==0:
                sys.exit()'''
           

    return bestword
        
    # If you can construct the word from your hand
    # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)

    # Find out how much making that word is worth

    # If the score for that word is higher than your best score

    # Update your best score, and best word accordingly


    # return the best word you found.


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, testList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function
    totalscore=0
    while calculateHandlen(hand)>0:
        print "Current hand: ",
        displayHand(hand)
        computerword=compChooseWord(hand, testList, n)
        if computerword == None:
            break
        else:
            totalscore+=getWordScore(computerword,n)
            hand=updateHand(hand,computerword)
            print "\"%s\" earned %s points. Total: %s points.\n" % (computerword, getWordScore(computerword,n), totalscore )
        
        
    print "Total score: %s points" % totalscore
    
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    #print "playGame not yet implemented." # <-- Remove this when you code this function
    userinput=""
    userchoice=""
    handcount=0
    while userinput != "e":
        userinput=raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        #if userinput == "n" or (userinput == "r" and handcount!=0):
        if userinput == "n":
            while userchoice =='u' or userchoice =='c' or userchoice=="":
                userchoice=raw_input("Enter u to have yourself play, c to have the computer play: ")    
                if userchoice == 'u':
                    handcount+=1
                    hand=dealHand(HAND_SIZE)
                    playHand(hand, wordList, HAND_SIZE)
                    break
                elif userchoice == 'c':
                    handcount+=1
                    hand=dealHand(HAND_SIZE)
                    compPlayHand(hand, wordList,HAND_SIZE)
                    break
                else:
                    print "Invalid command."
                    userchoice=""
        elif userinput == "r" and handcount==0:
            print "You have not played a hand yet. Please play a new hand first!", handcount 
                       
        elif userinput == "r" and handcount!=0:
            while userchoice =='u' or userchoice =='c' or userchoice=="":
                userchoice=raw_input("Enter u to have yourself play, c to have the computer play: ")    
                if userchoice == 'u':
                    handcount+=1
                    playHand(hand, wordList, HAND_SIZE)
                    break
                elif userchoice == 'c':
                    handcount+=1
                    compPlayHand(hand, wordList,HAND_SIZE)
                    break
                else:
                    print "Invalid command."
                    userchoice=""
                    
        elif userinput == "e":
            break
            
        else:
            print "Invalid command."

    
    

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    testList = ['DINGHIES', 'ANTONYMY', 'THEURGIC', 'WAKIKIS', 'BIBBS', 'appels', 'imamate','in','koji','bi']
    playGame(testList)

#compChooseWord(hand, wordList, n)
#print compChooseWord({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, testList, 6)
#print compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, testList, 6)
#print compPlayHand({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, testList, 12)
#print compPlayHand({'b': 1, 'i': 2, 'k': 1, 'j': 1, 'o': 1, 'w': 2}, testList, 8)
