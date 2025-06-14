class Person:
    def __init__(self,f_name,l_name):
        self.f_name=f_name
        self.l_name=l_name
        print(f"First name is: {self.f_name} and Last name is: {self.l_name}")

class Student(Person):
    def __init__(self,f_name,l_name):
        super().__init__(f_name,l_name) #super() is used to also consider the init in the Person class
        print("Student inside class init")

a = Student("Ashutosh","Singh")

