class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'{self.name} is {self.age} years old'

p = Person('Ashutosh',20)
print(p)