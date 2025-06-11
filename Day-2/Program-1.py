class Apple_design:
    count = 0   #class variable or static variable

    def __init__(self,cpu,ram):     #constructor
        self.cpu = cpu
        self.ram = ram
    def mobile(self):       #instance variable
        print("this is apple phone 1")
        print(self.cpu,self.ram)
        print(type(self))
m1 = Apple_design(3.5,8)
m2= Apple_design(4.5,16)      #default constructor
m1.mobile()
m2.mobile()
print(id(m1))
print(id(m2))