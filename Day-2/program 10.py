#Addition and substraction using static method
class MathOperation:
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def sub(a,b):
        return a-b

Operation = MathOperation()
result_add = MathOperation.add(1,2)
result_sub = MathOperation.sub(1,2)
print(f"Addition result: {result_add}")
print(f"Subtraction result: {result_sub}")
