# collection examples , phillip henry, v0.1b
# list--- ordered, changeable, allows duplicate values
#
breakfastfoods = ["waffles","pancakes" , "cereal", "milk"]
# each iteam on the list is known as an element
#the postion in the list for each is the index
# the element "bacon" is at index 0.
# python only: index -1 it is the last item on the list
testscores = [95, 100, 25, 15, 27, 35]
classGPA = [3.14, 2.25, 1.74, 1.99, 0.99,4.25]

#printing contents of an list
#print(breakfastfoods)
#print(testscores)
#print(classGPA)

#access specific elements ----- remember first elements is 0
#print(breakfastfoods[0])
#print(testscores[0])
#print(classGPA[0])

# accessing the last element
#print(breakfastfoods[-1])
#print(classGPA[-1])
#print(testscores[-1])

# write code

#print(breakfastfoods[2])
#print(classGPA[2])
#print(testscores[2])

#changing iteams in a list
breakfastfoods[0] = "waffles"
testscores[0] = 95
classGPA[0] = 3.14
print(breakfastfoods[0])
print(testscores[0])
print(classGPA[0])
print(breakfastfoods)
print(testscores)
print(classGPA)

#wyoc

#breakfastfoods[4] = "milk"
#testscores[4] = 15
#classGPA[4] = 1.99
#print(breakfastfoods0)
#print(testscores)
#print(classGPA)

# adding and inserting items to a list
#. append() adds an iteam to the end of the list
#breakfastfoods.append("hashbrowns")
#print(breakfastfoods)
#testscores.append(100)
#print(testscores)
#lassGPA.append(3.90)
#print(classGPA)
# .insert() allows you to place an iteam at a specific index in the list
#breakfastfoods.insert(3,"yorgurt")
#print(breakfastfoods)
#classGPA.insert(2, 2.5)
#print(classGPA)
#testscores.insert(3,400)

#wyoc

breakfastfoods.insert(2,"fruit")
print(breakfastfoods)
testscores.insert(2, 87)
print(testscores)
classGPA.insert(1, 4.8)
print(classGPA)

