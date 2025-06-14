class student:
    __name = None
    __roll = None
    __branch = None
    def __init__(self, name, roll, branch):
        self.__name = name
        self.__roll = roll
        self.__branch = branch
    def __displayDetails(self):
        print("Name:", self.__name)
        print("Roll:", self.__roll)
        print("Branch:", self.__branch)
    def accessPrivateMethod(self):
        self.__displayDetails()


a = student("Ashutosh", 1500, "Data Science")
a.accessPrivateMethod()