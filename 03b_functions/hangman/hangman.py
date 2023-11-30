# Code crashes immediately upon running.  You need to fix these critical errors. 
import random
#words = "dragon ball awesome plankton apple cat rat fat plat hat cap rap ultra hulk captian america spider man gwen ultimate battle marvel versus capcom three number lock Antidisestablishmentarianism Floccinaucinihilipilification mortal kombat fighterz two wubba lubba dub dub goku vegeta".split()
#dictionary version 
#stored in key:value pairs 
#actual dictonary word (key) : value (defintion)
#uses {} to specify a dictionary
words = {'colors':'red orange yellow green blue prurple violet black gold silver white.split(),'
        'animals': 'cat rat cat bat dog dragon fish moose goose alligator'
        'shapes':' square circle rombus triangle rectangle trapizoid diamond'
        'food':' hamburger pizza hotdog waffle potato pancake chips steake'}
HANGMAN_BOARD =  ['''
        +---+
            |                  
            |
            |         
          ===== '''    ]
['''
        +---+
        0   |                  
            |
            |         
          ===== '''    ]
['''
        +---+
        0    |                  
        |    |
             |         
          ===== '''    ]
['''
        +---+
        0    |                  
        |\   |
             |        
          ===== '''    ]
['''
        +---+
         0     |                  
        /|\    |
               |         
          ===== '''    ]
['''
        +---+
         0    |                  
        /|\   |
        /     |         
          ===== '''    ]
['''
        +---+
         0    |                  
        /|\   |
        / \   |         
          ===== '''    ]
['''
         +---+
         0    |                  
       o-|-o   |
        / \   |         
          ===== '''    ]
#i = 0 
#while i < len(HANGMAN_BOARD):
#    print(HANGMAN_BOARD[i])
#    i += 1
# PICK word from list
def getrandomword(wordlist):
    wordindex = random.randint(0,len(wordlist)-1)
#len(listname) - 1 is extreamly common for working with lists
return wordlist[wordindex]
def getrandomword(wordDict):
    wordkey = random.choice(list(worddict.key()))
    wordindex = random.randint(0, len(wordDict[wordkey]- 1))
    return [wordDict[wordkey][wordindex], wordkey]
i = 0
while i < 50:
    word = randomword(words)
    print(word)
    i += 0 
def displayboard(missedletters, correctletters, secretword):
    print(HANGMAN_BOARD[len(missedletters)])
    print('missed letters:', end = ' ')
    for eachletter in missedletters:
        print(eachletter, end = ' ')
    print()

    blanks - '' * len(secretword)
    for i in range(len(secretword)):
        if secretword[i] in correctletters:
            blanks = blanks[:i] + secretword[i] + blanks[i+1:]
            
    for letter in blanks:
        print(letter, end = '')
        print()


def getguess(alreadyguessed):
    while true:
        print("pick a letter from all 26 letters of the alphabet.")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("put one letter ONLY.")
        elif guess in alreadyguessed:
            print("letter guesses already, try again ")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('please guess a letter only from the english alphabet.')
        else:
            return guess 
        def playagain():
            print('do you want to play again? yes or no')
        return input().lower().startswith('y')
    difficulty = 'X'
while difficulty not in 'EMH':
    print('please chose easy medium or hard type the first letter in upper case please ')
    diffuculty = input().upper()
    if difficulty == 'M':
        del HANGMAN_BOARD[8]
        del HANGMAN_BOARD[7]
        if difficulty == 'H':
         del HANGMAN_BOARD[8]
        del HANGMAN_BOARD[7]
        del HANGMAN_BOARD[6]
        del HANGMAN_BOARD[5]
        print('welcome to hangman by phil')
    missedletters = ''
    correctletters = ''
    secretword, secretset = getrandomword(words) 
    gameisdone = False

    while true:
        print('the secret word is from the ' + secretset + 'catagory.\n')
        displayboard(missedletters, correctletters, secretword)

        guess = getguess(missedletters + correctletters)
        if guess in secretword:
            correctletters = correctletters + guess

            foundallletters = True
            for i in range(len(secretword)):
                if secretword[i] not in correctletters:
                    foundallletters = False
                    break
                if foundallletters:
                    print('wow u won aginst a bot your so good')
                    print('the secret word was' + secretword)
                    gameisdone = true
                else:
                    missedletters = missedletters + guess
                    if len(missedletters) == len(HANGMAN_BOARD) - 1:
                        displayboard(missedletters, correctletters, secretword)
                        print('imagine losing lil bro')
                        print('you only made this number of corret guesses' + str(len(correctletters)))
                        print('the secret word was' + secretword)
                        gameisdone - True
                        if gameisdone:
                            if playagain():
                               missedletters = ''
                               correctletters = ''
                               gameisdone = False














