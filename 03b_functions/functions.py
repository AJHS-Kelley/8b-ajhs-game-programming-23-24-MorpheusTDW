import random  
import numrolled
# function -- a named piece of code that can be reused easily 
# funtion signature -- syntax for creating a new function
def exampleFunction(): # no parameters
    count = 0
    num = int(input("how many times do you want to with a happy birthday?\n"))
    while count < num:
        print("happy birthday!\n")
        count += 1

def exampleFunctionB(num, count): #parameters
    while count < num:
        print("happy birthday!\n")
        count += 1
     
# if a function requires parameters your code will crash without them

# running a function is know as calling the function
#exampleFunction(30)
#exampleFunctionB(5, 0)
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
rolldice(20, 3)

strengthplayer = rolldice(3, 6)
dextarityplayer = rolldice(3, 6)
wisdomplayer = rolldice(3, 6)







