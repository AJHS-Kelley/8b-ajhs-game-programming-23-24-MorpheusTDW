import dice
def rolldice(numdice,sizedice):
    while numrolled < numdice:
        roll = random.randint(1,sizedice)
        sum += roll
        print (f"Roll: {roll}\n")
        print(f"sum: {sum}\n")
        numrolled += 1
        sum = 0
rolldice(3, 6)
rolldice(1, 20)
rolldice(10, 7)
