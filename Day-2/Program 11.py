#Parameterized constructor
class Addition:
    first = 0
    second = 0
    answer = 0
    def __init__(self,f,s):      #parameterized constructor
        self.first = f
        self.second = s
    def display(self):
        print("first number:",self.first)
        print("second number:",self.second)
        print("addition result: ",self.answer)
    def calculate(self):
        self.answer = self.first + self.second


obj = Addition(3,4)
obj.calculate()
obj.display()
