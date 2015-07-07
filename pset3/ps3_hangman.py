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

WORDLIST_FILENAME = "C:\Users\Bharath Desktop\Desktop\hangm\words.txt"

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
    wrdlst=list(secretWord) #making the secretWord chars into a list
    
    wrdlst=list(set(wrdlst)) # using the set function to remove duplicates from the list and re casting it as list
     
    lettersGuessed=list(set(lettersGuessed))# similarly removing duplicated from the letters guessed
    
    
    c=0
    x=0
    flag=0
    
    for i in lettersGuessed:
        
        
        for j in wrdlst:
           
            
            if(i is j):

                flag=1
                break
            flag=0
        if(flag==1):
            
            c+=1
            
            
        

    if(c == len(wrdlst)):#if the number of matched chars eqals the len of the wrdlist then its a match
        
        return True
        
        
    return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    #similar to the earlier fuction, with a modification for returning the string
    wrdlst=list(secretWord)
    
    wrdlst=list(set(wrdlst))
    
    
    lettersGuessed=list(set(lettersGuessed))
    
    s=[]
    c=0
    x=0
    flag=0
    
    for i in lettersGuessed:
        
        
        for j in wrdlst:
           
            
            if(i is j):

                flag=1
                s.append(i)
                break
            flag=0
        if(flag==1):
            
            c+=1
           
            
    y=''
    for x in secretWord:
        if( x in s):
            y=y+ x
        else:
            y=y+ " _ "
    return y
    



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    let= list(string.ascii_lowercase)
    
    for p in lettersGuessed:
        
        if(p in let):
            
            let.remove(p)
   
    op=''
    for x in let:
        op=op+x
    return op
    

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
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is "+str(len(secretWord))+" letters long.")
    print("-------------")
    remG=8
    letG=[]
    gameOvr=False
    won=0
    guess=getGuessedWord(secretWord, letG)
    while(not gameOvr):
        print("You have "+str(remG)+" guesses left.")
        avalet=getAvailableLetters(letG)
        print("Available letters: "+avalet)
        g=raw_input("Please guess a letter: ")
        g=g.lower()
        if(g in avalet):
            l=list(g)
            letG=letG+l

            if(g in secretWord):
                guess=getGuessedWord(secretWord, letG)
                print("Good guess: "+guess)
                if (isWordGuessed(secretWord,letG)):
                    won=1
                    gameOvr=True
                    
            else:
                print("Oops! That letter is not in my word: "+guess)
                remG -=1
                if(remG == 0):
                    gameOvr=True

        else:
            print("Oops! You've already guessed that letter: "+guess)
        print("-------------")
    if(gameOvr and won==0 ):
        print("Sorry, you ran out of guesses. The word was "+secretWord+".")
    elif(gameOvr and won==1 ):
        print("Congratulations, you won!")
        




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

#secretWord = chooseWord(wordlist).lower()
secretWord = 'zzz'
hangman(secretWord)
