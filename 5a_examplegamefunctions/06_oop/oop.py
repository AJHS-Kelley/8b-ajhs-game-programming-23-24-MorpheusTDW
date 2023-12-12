#object oriented programming, phillip henry v0.0
class person: # use pascal for classname 
    def __init__(self, name, age, weight):
        self.name = name
        self,age = age 
        self.weight = weight 
    
    def __str__(self):
        return f"name: {self.name}\n this person is {self.name}\nthis person is {self.age} he weights {self.weight}

print(person1) = person("phillip henry",2,150)