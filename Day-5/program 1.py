class Duck:
    def quack(self):
        print("Quack!")

    def eat(self):
        print("Duck eats")

class Person:
    def quack(self):
        print("Person quacks like duck")

    def eat(self):
        print("Person eats duck")

a = Duck()
b = Person()
a.quack()
b.quack()
a.eat()
b.eat()