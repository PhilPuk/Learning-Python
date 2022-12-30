class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old.')


my_person = Person('Phil', 20)

print(my_person.name)

print(my_person.age)

my_person.say_hello()