# select that sceret number from a given range 
# player must guess the number 
# compare guess to the secret number
# what happens if the guess is wrong?
    # Tell them the guess is wrong 
    # tell them the number of guess is wrong 
    # too high/too low 
# what happens if the guess is right 
# tell them its correct
# give them a point 
# what happens if the player runs out of guesses 
# tell the player he sucks 
# give a point to cpu
# check to see if player of cpu has >= 3 points, if so they win

import random # import the random module to our code 
# declarations 
secretnumber = 50
playerGuess =  3
playerScore = 0 
cpuScore = 0
numGuesses = 0
playername = ""
difficulty = ""
rangemin = 1
rangemax = 10 
numattempts = 3


print("""
      *~~~~~~~~~~~~~~~~~~~~~~~~~*
      |                         |
      |    phils number         |
      |guess game               |
      |                         |
      |~~~~~~~~~~~~~~~~~~~~~~~~~|""")

# CPU SECRET NUMBER GENERATION
secretnumber = random.randint(0 , 100)
print(secretnumber)
print(f"{playername}: {playerScore}\nCPU Score: {cpuScore}.\n")
X = 0
difficulty = input("select a difficulty bum. scary, kinda scary and GOD")
while X < 100:
    secretnumber = random.randint(0 , 100)
    #print(secretnumber)
    X += 1
# game loop
print("you need to guess the number from 0 to 100 and if. \nyou mess up you get it wrong bozo and the cpu gets a point") 
# print () an explnation of your three difficulty levels

# use input () to store diffuculty levels
#assign values to numattemps, rangwmin and rangemax
playername = input("put ya name bro.\n")
while playerScore != 3 and  cpuScore != 3:    #pass -- tells python to skip code 
    print(f"player score: {playerScore}\nCPU score: {cpuScore}.\n")
    secretnumber = random.randint(0 , 100)
    secretnumber = random.randint(rangemin , rangemax)
    # whenever you assign a specific value to something its called hard code 

    for guesses in range(4):
        if difficulty == "scary":
            rangemin = 1
            rangemax = 10 
            numattempts = 5
        elif difficulty == "kinda scary":
            rangemin = 1
            rangemax = 100 
            numattempts = 3
        elif difficulty == "GOD":
            rangemin = 1
            rangemax = 1000 
            numattempts = 1
        print(f"you have {numattempts - numGuesses} guesses remaining.\n")
        playerGuess = int(input("type a number from 0 to 100 and press ENTER.\n"))

    print(f"you have chosen {playerGuess}. Let's see if you're right!\n")
    if playerGuess == secretnumber:
        print("yoooo good job you guessed it right!\n")
        playerScore += 1
        break # IMMEDNETLY EXIT ANY LOOP YOU ARE IN!
    else: 
        print("you did not guess it right L bozo,\n")
        if playerGuess > secretnumber:
            #input() saves all data as a string.
            #int() will convert to an integer
            #float() will convert to a float
            print("your guess is to high.\n")
        else:
            print("your guess is to low.\n")
    numGuesses += 1
    if playerGuess != secretnumber:
        cpuScore += 1
        print("THE CPU WINNNNSS YOU GUESS IT WRONG BUDDY.\n")
if playerScore >= 3:
    print(" winner, winner you've one buddyyyyyyyy good job you scored 3 points")


    







