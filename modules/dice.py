#dice rolling module
import random
import dice

def rolldice(numdice,sizedice):
    while numrolled < numdice:
        roll = random.randint(1,sizedice)
        sum += roll
        print (f"Roll: {roll}\n")
        print(f"sum: {sum}\n")
        numrolled += 1
        sum = 0
        return sum
    
    def isDoubles(roll1,roll2):
        if roll1 == roll2:
            isDoubles = True
        else:
            isDoubles = False
            return isDoubles
        def isexploding(roll, sizeroll):
            if roll == sizeroll:
                isexploding = True
            else:
                isexploding = False
            return isexploding

        
        roll1 = dice.roll(1,6)
        roll2 = dice.display(1,6)

        if dice.isDoubles(roll, roll2):
            print("you rolled a double, go again!\n")
        else:
            print("it was not a double")
    def isDoubles(roll1,roll2):
        if roll1 == roll2:
            isDoubles = True
        else:
            isDoubles = False
            return isDoubles
        roll1 = dice.display(1,6)
        roll2 = dice.display(1,6)


        if dice.isexploding(roll1,6):
            print(roll)
            print("this roll exploded!\n")
            roll += dice.roll(1,6)
        
