class Student:
    _name = None        #protected variable because of '_'
    _roll = None
    _branch = None

    def __init__(self,name,roll,branch):
        self._name = name
        self._roll = roll
        self._branch = branch

    def _displayInfo(self):
        print("Roll:",self._roll)
        print("Branch:",self._branch)

class Learnox(Student):
    def __init__(self,name,roll,branch):
        Student.__init__(self,name,roll,branch)
    def displayDetails(self):
        print("Name:",self._name)
        self._displayInfo()

obj = Learnox("Ashutosh","1654","Data Science")
obj.displayDetails()

