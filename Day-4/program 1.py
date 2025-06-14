#inheritance
class Parent:
    def feature1(self):
        print("This is feature1")

    def feature2(self):
        print("This is feature2")

class Child(Parent):
    def feature3(self):
        print("This is feature3")

    def feature4(self):
        print("This is feature4")

c = Child()
c.feature1()
c.feature2()
c.feature3()
c.feature4()