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
while i < len(HANGMAN_BOARD)
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
    for eachletter in missedletters 
    print(eachletter, end = ' ')
    print()

