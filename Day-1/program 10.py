list1 = [1,2,3,4,5,6,7,8,9,10]
def isEven(num):
    if num % 2 == 0:
        return True
even_number = filter(isEven, list1)
a = list(even_number)
print(a)