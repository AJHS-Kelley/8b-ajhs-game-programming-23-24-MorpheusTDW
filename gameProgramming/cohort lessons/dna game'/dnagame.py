#dna rep game , phil v0.0
import time,datetime

import random
import

dnabases = ["A", "T", "G" "C"]

def gameintro() -> none:
    pass

def genDNA() -> str:
    basegenerated = 0
    baserequested = int(input("please enter a positive interger number of bases to generate.\n"))

    while basegenerated < baserequested:

        

def doTranscriptiongenRNA(dnasequence: str) -> tuple:
    print(f"the DNA sequence is {dnasequence}.\n")
    print("you will now genarate the dna sequence the would match\n")
    print("please remember, in the RNA sequence u pairs with a from the DNAsequence.\n")
    rnastart = time.time()
    rnasequence = input("please enter the matching rna sequence . leave no space! then press enter\n").upper()
    rnastop = time.time()
    rnatime = rnastop - rnastart
    return (rnasequence, rnatime)

def verifysequence(dnasequence: str, rnasequence: str) -> bool:
    ismatch = False
    if len(dnasequence) != len(rnasequence):
         dnabases, rnabase in zip(dnasequence, rnasequence):
    x    if dnabases == "A" and rnabase == "U":
                ismatch = True
               elif dnabases C
                elif dnabases G
                elif dnabases T


    return ismatch



rna = doTranscriptiongenRNA(dna)
print(rna)

if len(dnasequence: str, rnasequence: str):
    print("the sequence are diffrent length and cannot match.\n")

    

    

