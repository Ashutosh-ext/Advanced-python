class Animal:
    def speak(self):
        print("Animals make some sound")

class Dog(Animal):
    def speak(self):
        print("Dogs bark")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

a=Animal()
b= Dog()
c = Cat()
a.speak()
b.speak()
c.speak()