class MyClass:
    def sum(self,a=None,b=None,c=None):
        s = 0
        if a != None and b != None and c != None:
            s=a+b+c
        elif a != None and b != None:
            s=a+b
        else:
            s = a
        return s

s = MyClass()
print(s.sum(1,2,3))
print(s.sum(1,2))
print(s.sum(1))