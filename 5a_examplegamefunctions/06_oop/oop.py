#object oriented programming, phillip henry v0.0
#class person: # use pascal for classname 
#    def __init__(self, name, age, weight):
#        self.name = name
#        self,age = age 
#       self.weight = weight 
#
#    def __str__(self):
#        return f"name: {self.name}\nthis person is {self.age} years old\nthey weigh {self.weight} pounds. \n"

person1 = person1 ("phillip",17,250.5)
person2 = person2 ("jordan",13,150.5)
#print(person1)
#print(person2)

#if person.age > person2.age:
#    print(f"person.name) haha shes older than you (person2.name),")
#elif person.weight == person2.weight:
 #   print("each person weighs the time. \n")
#else:
 #   print(f"(person2.name)weighs more than (person.name).")

print(person1.name)
person1.name = "phillip henry"
print(person1.name)

#deleting proprites -- danger danger 
# its gone forever
print(person1.name) 
del person1.name
#print(person1)

#deleting objects -- delete them if your finished with them
del person1
#adding prop to object
person2.weakness ="kryptonite"
print(person2) 
print(person2.weakness)       