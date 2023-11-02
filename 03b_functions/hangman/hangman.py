import random
words = "dragon ball awesome plankton apple cat rat fat plat hat cap rap ultra hulk captian america spider man gwen ultimate battle marvel versus capcom three number lock Antidisestablishmentarianism Floccinaucinihilipilification mortal kombat fighterz two wubba lubba dub dub goku vegeta".split()
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
i = 0 
while i < len(HANGMAN_BOARD):
    print(HANGMAN_BOARD[i])
    i += 1
# PICK word from list
def getrandomword(wordlist):
    wordindex = random.randint(0,len(wordlist)-1)
#len(listname) - 1 is extreamly common for working with lists
return wordlist [wordindex]
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
        def playagain()
        print('do you want to play again? yes or no')
        return input().lower().startswith('y')
    
    print('welcome to hangman by phil')
    missedletters = ''
    correctletters = ''
    secretword = getrandomwords(words)
    gameisdone = False
    while true:
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
                                














