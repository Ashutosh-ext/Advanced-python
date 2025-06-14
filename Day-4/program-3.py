class Father:
    money = 1000
    def show(self):
        print("Parent class instance method")

    @classmethod
    def moneyshow(cls):
        print("Parent class method instance method,Money:",cls.money)

    @staticmethod
    def stat_method():
        a=5
        print("Parent class static method value of a:",a)


