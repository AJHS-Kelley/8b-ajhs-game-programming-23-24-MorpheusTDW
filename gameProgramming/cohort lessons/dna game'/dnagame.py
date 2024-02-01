# Import Entire Modules -- Get the whole tool box
import time, datetime

# Import Specific Methods -- Get the specific tool
from random import choice

# Store the DNA Bases
dnaBases = ["A", "T", "G", "C"]

# Game Functions
def gameIntro() -> None:
    pass

def genDNA() -> str:
    basesGenerated = 0
    basesRequested = int(input("How many bases do you want, Please enter a possitive number\n"))
    dnaSequence = ""

    while basesGenerated < basesRequested:
        dnaSequence += choice(dnaBases)
        basesGenerated += 1
    return dnaSequence

def doTranscription(dnaSequence: str, basesRequested: str) -> tuple:
    print(f"The DNA Sequence is {dnaSequence}.\n")
    print("You will now generate the RNA sequence that would match\n")
    print("Please remember, in the RNA sequence U pairs with A from the DNA sequence")
    rnaStart = time.time() # time.time() returns the number of seconds since 00:00:00 UTC Jan, 01, 1970
    rnaStop = time.time()
    rnaTime = rnaStop - rnaStart
    rnaSequence = input("Please enter the matching RNA sequence.  Leave no spaces! Then press enter.\n").upper().split()
    return (rnaSequence, rnaTime)


    

    

