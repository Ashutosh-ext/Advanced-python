class Student:
    Counter = 0
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        Student.Counter = Student.Counter + 1
    def msg(self):
        print("Hello",self.name,"you got",self.marks,"% marks")
    @classmethod
    def object_count(cls):
        return cls.Counter
s1=Student('Ashutosh',81)
s2=Student('Dhruv',95)
s1.msg()
s2.msg()
print(Student.object_count())
print(s1.object_count())