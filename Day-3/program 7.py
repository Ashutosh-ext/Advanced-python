class MyClass:
    def __init__(self,value):
        self.value = value

def print_value(obj):
        print(f"The value is: {obj.value}")

obj = MyClass(10)
print_value(obj)