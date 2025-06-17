import sys


class PowerOfTwo:
    def __init__(self,max_value):
        self.limit = max_value
        self.current = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= self.limit:
            result = self.current
            self.current = self.current*2
            return result
        else:
            raise StopIteration
n = int(input("Enter the limit: "))
iter_obj = PowerOfTwo(n)
print(iter_obj.__next__())
for num in iter_obj:
    print(num)
print("Memory for iter obj:",sys.getsizeof(iter_obj),"Bytes")
