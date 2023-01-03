class Person:
    def __init__(self, name, hobby):
        self.name = name
        self.hobby = hobby


    def printInformations(self):
        print(self.name)
        print(self.hobby)

p = Person("Phil", "Coding")

p.printInformations()