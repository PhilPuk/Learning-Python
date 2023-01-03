import random

class Person:
    def __init__(self, name, age, height, country):
        self.name = name
        self.age = age
        self.height = height
        self.country = country

    def printInformations(self):
        print("Name: ", self.name)
        print("Age: ",self.age)
        print("Height: ",self.height)
        print("Country: ",self.country)



def createRandomPerson(amountOfPersons):
    persons = [] # Empty person container
    name_list = []
    country_list = []
    #Import names into the list
    with open("C:\\Users\\Phil\\Documents\\Coding\\Python\\Learning Python\\Day 2\\Class Testing\\names.txt") as f:
        for name in f:
            name_list.append(name.strip())
    #Import countries into the list       
    with open("C:\\Users\\Phil\\Documents\\Coding\\Python\\Learning Python\\Day 2\\Class Testing\\countries.txt") as f:
        for country in f:
            country_list.append(country.strip())
    #Create persons
    for i in range(amountOfPersons):
        random_name = name_list[random.randint(0, 18239)]
        random_country = country_list[random.randint(0, 196)]
        random_age = random.randint(1, 120)
        random_height = round(random.uniform(1.10, 2.50), 2)
        persons.append(Person(random_name, random_age, random_height, random_country))

    #Print persons
    for i in persons:
        print("----------------")
        i.printInformations()

#Main Programm
createRandomPerson(10)


