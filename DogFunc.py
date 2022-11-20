class Dog:
    
    def __init__(self, name, age, coatColor):
        self.name = name
        self.age = age
        self.coatColor = coatColor
    
    def description(self):
        return "{} is {} years old".format(self.name, self.age)
    
    def get_info(self):
        return "{} is {}".format(self.coatColor, coatColor)

class JackRussellTerrier(Dog):
    def run(self, coatColor):
            return "{} color {}".format(self.name, coatColor)

class Bulldog(Dog):
     def run(self, coatColor):
            return "{} color is  {}".format(self.name, coatColor)

jimi = Bulldog("Tuffy", 2 , "Grey")
print(jimi.description())

print(jimi.run("Grey"))