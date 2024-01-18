#DNAGame phillip henry
# Import entire tool box
import time, datetime
#import specific tools
from random import choice

dnaBases = ["A","T","G","C"]

#Game Fuctions
def gameIntro() -> None:
    pass
def genDNA() -> str:
    bassGenerated = 0
    bassRequested = int(input("Please inter positive integer number of bases to generate.\n"))
    dnaSequence = ""

    while bassGenerated < bassRequested:
        dnaSequence += choice(dnaBases)
        bassGenerated += 1
    return dnaSequence
   
dna = genDNA()


def doTranscription (dnaSequence: str) -> tuple:
    print(f"The DNA Sequence is {dnaSequence}.\n")
    print("You will now generate the RNA sequence that would match.\n")
    print("Please remember, in the RNA sequence U pairs with A from the DNA sequence.\n")
    rnaStart= time.time() #time.time() return the number of seconds since 00:00:00 UTC Jan. 01, 1970
    rnaSequence = input("Please enter the matching rna sequence.\n").upper()
    rnaStop = time.time()
    rnaTime = rnaStop-rnaStart
    return (rnaSequence, rnaTime)
    # Tuples are Ordered-- you can refrence items with the index.
    # Tuples are unchangeable -- you cannot add, modify, or delete
    # tuples can have duplicate values

def verifySequence(dnaSequence: str, rnaSequence: str) -> bool:
    isMatch = False
    if len(dnaSequence) != len(rnaSequence):
        print("The sequence is diffrent lengths and cannot match.\n")
        return isMatch
    for dnaBase, rnaBase in zip(dnaSequence, rnaSequence):
        if dnaBase == "A" and rnaBase == "U":
            isMatch = True
        elif dnaBase == "C" and rnaBase == "G":
            isMatch=True
        elif dnaBase== "T" and rnaBase=="A":
            isMatch=True
        elif dnaBase == "G" and  rnaBase == "C":
            isMatch=True
        else:
            isMatch=False
            print ("Error no Match.")

    return isMatch

def calcScore(rnaSequence:str, rnaTime: float ) ->  int:
    score = 0
    if rnaTime < 1.0:
        score +=1000000
    elif rnaTime < 5.0:
        score += 9000
    elif rnaTime < 15.0:
        score += 800
    else:
        score += 10

    scoreMulti = 0.0
    if len(rnaSequence) >= 30:
        scoreMulti = 5.0
    elif len(rnaSequence) >= 25:
        scoreMulti= 4.0
    elif len(rnaSequence) >= 15:
        scoreMulti= 1.0
        score *= scoreMulti
    return score

def saveScore(dnaSequence: str, rnaSequence: str, rnaTime, float,score saveData)-> None:
    playerName = input ("Whats your name?\n")
    lastName = input("And your last name?\n")
    fullName = playerName + " " + lastName

    fileName = "dnaReplicationScore"+ fullName + ".txt"
    saveData = open(fileName, "a")
    #File Modes
    # "x" mode -- CREATE FILE, IF FILE EXISTS, EXIT WITH ERROR
    # "w" mode -- CREATE FILE IF FILE EXITS, OVERWRITE IT
    # "a" mode -- CREATE FILE, IF FILE EXIXTS, APPEND TO IT
   

rna = doTranscription(dna)
print (verifySequence(dna, rna[0]))

print(calcScore(rna[0],rna[1]))

saveData.write(f"DNA sequence:{dnaSequence}\nRNA sequence: {rnaSequence}\n")
saveData.write(f"Transcription Time: {rnaTime}\n")
saveData.write(f"Score: {score}\n")
saveData.write(f"{Fullname}\n")
saveData.write(f"{datetime.datetime.now()}\n")


dna = genDNA()
rna = doTranscription(dna)
if verifySequence(dna, rna[0]):
    score = (calcScore(rna[0], rna[1]))
    saveScore(dna, rna[0, rna[1], score])
