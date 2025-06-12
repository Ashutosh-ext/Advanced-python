class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person({self.name})"

class Greeting:
    def genrate_greeting(self,person):
        return f"Hello {person.name}!,Welcome!"

person = Person("John")
greeting = Greeting()

message = greeting.genrate_greeting(person)
print(message)
