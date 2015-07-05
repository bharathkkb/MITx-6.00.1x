from ps4a import *
import time

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList
#
#
# Problem #6: Computer chooses a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # TO DO ... <-- Remove this comment when you code this function
    s=0
    for ch in word:
        a=SCRABBLE_LETTER_VALUES.get(ch)
        s+=a
    l=len(word)
    if(l==n):
        return (s*l)+50
    else:
        return s*l
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    tempHand=hand.copy()
    c=0
    
    for ch in word:
        val=tempHand.get(ch,0)
        tempHand[ch]=val-1
        if(val!=0):
            c +=1
            
    if(c == len(word)):
        return True
    else:
        return False
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
    temphand=hand.copy()
    for x in word:
        val=temphand.get(x,0)
        val -=1
        temphand[x]=val
    return temphand


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

    # Create a new variable to store the best word seen so far (initially None) 
    top=0
    bword=None
    for wrd in wordList:
        if(isValidWord(wrd, hand, wordList)):
            points=getWordScore(wrd,n)
            if(points>top):
                top=points
                bword=wrd
    return bword
            


    # For each word in the wordList

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)

            # Find out how much making that word is worth

            # If the score for that word is higher than your best score

                # Update your best score, and best word accordingly


    # return the best word you found.


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
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
    totscr=0
    while(calculateHandlen(hand)>0):
        

        print "Current Hand: ",
        displayHand(hand)
        
        inp=compChooseWord(hand,wordList,n)

        
        if(inp!=None):
            scr=getWordScore(inp,n)
            totscr +=scr;

            print "\""+inp+"\""+" earned "+ str(scr)+" points. "+ "Total score: "+str(totscr) +" points."
            hand= updateHand(hand,inp)
        else:
            break
                
            
    
    print "Total score: "+str(totscr)+"."
    
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
    n=HAND_SIZE
    beg=True
    inp="f"
    while inp!="e":
        inp=raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
        if(inp=="n"):
            hand = dealHand(n)
            inp2=raw_input("Enter \"u\" to have yourself play, \"c\" to have the computer play: ")
            while(inp2!="u" and inp2!="c"):
                print "Invalid Command."
                inp2=raw_input("Enter \"u\" to have yourself play, \"c\" to have the computer play: ")
                
            beg=False
            if(inp2=="u"):
                        playHand(hand, wordList,n)
            else:
                        compPlayHand(hand, wordList,n)
            
                        
                        
        elif(inp=="r"):
            if(beg==True):
                 print "You have not played a hand yet. Please play a new hand first!"
            else:
                    inp2=raw_input("Enter \"u\" to have yourself play, \"c\" to have the computer play: ")
                    while(inp2!="u" and inp2!="c"):
                        print "Invalid Command."
                        inp2=raw_input("Enter \"u\" to have yourself play, \"c\" to have the computer play: ")
                    if(inp2=="u"):
                        playHand(hand, wordList,n)
                    else:
                        compPlayHand(hand, wordList,n)

        elif(inp!="e"):
            print "Invalid Command."









        
#
# Build data structures used for entire session and play game
#
WORDLIST_FILENAME = "C:\Users\Bharath Desktop\Desktop\ProblemSet4\words.txt"
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)



