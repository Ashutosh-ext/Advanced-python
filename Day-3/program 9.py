class MyClass(object):
    def __init__(self, value):
        self.value = value

def create_object(value):
    return MyClass(value)

obj = create_object(10)
print(obj.value)