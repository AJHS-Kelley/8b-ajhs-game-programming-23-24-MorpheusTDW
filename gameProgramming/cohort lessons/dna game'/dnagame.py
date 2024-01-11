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
    
