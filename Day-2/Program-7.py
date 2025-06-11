class Number:
    even = []
    odd = []
    def __init__(self,num):
        self.num = num
        if num % 2 == 0:
            self.even.append(num)
        else:
            self.odd.append(num)
n1 = Number(98)
n2 = Number(92)
n3 = Number(94)
n4 = Number(99)
n5 = Number(100)
n6 = Number(101)
n7 = Number(102)
n8 = Number(103)
print("even numbers are:",Number.even)
print("odd numbers are:",Number.odd)