#dice rolling module
import random
def rolldice(numdice,sizedice):
    while numrolled < numdice:
        roll = random.randint(1,sizedice)
        sum += roll
        print (f"Roll: {roll}\n")
        print(f"sum: {sum}\n")
        numrolled += 1
        sum = 0