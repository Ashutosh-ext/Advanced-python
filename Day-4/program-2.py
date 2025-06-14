class Animal:
    name=""
    def eat(self):
        print("I need pedigree")

class Dog(Animal):
    def display(self):
        print(f"My name is {self.name}")

labrador = Dog()
labrador.name = "Sher"

labrador.display()
labrador.eat()