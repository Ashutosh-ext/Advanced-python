#decorator
#it is a function that updates existing function

def decor(addition):
    def inner():
        result=addition() #existing
        num3 = float(input("Enter number3: "))
        result = result + num3
        return result
    return inner #closure
@decor
def addition():
    num1 = float(input("Enter number1: "))
    num2 = float(input("Enter number2: "))
    result = num1 + num2
    return result
print(addition())
