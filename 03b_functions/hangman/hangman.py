words = "dragon ball awesome plankton apple cat rat fat plat hat cap rap ultra hulk captian america spider man gwen ultimate battle marvel versus capcom three number lock Antidisestablishmentarianism Floccinaucinihilipilification mortal kombat fighterz two wubba lubba dub dub goku vegeta".split()
HANGMAN_BOARD =  ['''
        +---+
            |                  
            |
            |         
          ===== '''    ]
['''
        +---+
        0    |                  
            |
            |         
          ===== '''    ]
['''
        +---+
        0    |                  
        |     |
             |         
          ===== '''    ]
['''
        +---+
        0    |                  
        |\    |
            |         
          ===== '''    ]
['''
        +---+
         0    |                  
        /|\    |
            |         
          ===== '''    ]
['''
        +---+
         0    |                  
        /|\    |
        /    |         
          ===== '''    ]
['''
        +---+
         0    |                  
        /|\    |
        / \   |         
          ===== '''    ]
i = 0 
while i < len(HANGMAN_BOARD)
    print(HANGMAN_BOARD[i])
    i += 1