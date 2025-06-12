import math
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def simplify(self):
        common_divisor = math.gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < self.denominator * other.numerator

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"



n1 = Fraction(1,2)
n2 = Fraction(3,4)

print(n1 + n2)
print(n1>n2)
print(n1<n2)
print(n1==n2)