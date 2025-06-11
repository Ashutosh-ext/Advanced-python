class Car:
    def __init__(self,company,price,year):
        self.company = company
        self.price = price
        self.year = year
    def display(self):
        print("Company:",self.company)
        print("Price:",self.price)
        print("Model:",self.year)


n1 = Car("Honda","700k","2019")
n2 = Car("Suzuki","800k","2020")
n1.display()
n2.display()