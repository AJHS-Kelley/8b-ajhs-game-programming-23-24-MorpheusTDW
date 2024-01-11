#dna rep game , phil v0.0
import time,datetime

import random
import choice 

dnabases = ["A", "T", "G" "C"]

def gameintro() -> none:
    pass

def genDNA() -> str:
    basegenerated = 0
    baserequested = int(input("please enter a positive interger number of bases to generate.\n"))

    while basegenerated < baserequested:

        

def genRNA(dnasequence: str) -> tuple:
    print(f"the DNA sequence is {dnasequence}.\n")
    print("you will now genarate the dna sequence the would match\n")
    print("please remember, in the RNA sequence u pairs with a from the DNAsequence.\n")
    rnastart = time.time()
    rnasequence = input("please enter the matching rna sequence . leave no space! then press enter\n").upper()
    rnastop = time.time()
    rnatime = rnastop - rnastart
    return (rnasequence, rnatime)

