class Car:
    wheel = 4   #class variable
    def __init__(self,name):
        self.name = name
n1 = Car("Mercedes")
print(n1.wheel)
print(Car.wheel)
print(n1.name)