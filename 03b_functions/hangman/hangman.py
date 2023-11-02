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









