class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Sell price is :",self.__maxprice)
    def setMaxprice(self,maxprice):
        self.__maxprice = maxprice
        print("Max price is :",self.__maxprice)

a = Computer()
a.sell()
a.setMaxprice(1500)