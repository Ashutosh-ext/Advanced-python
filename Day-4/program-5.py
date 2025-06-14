class Father:
    def __init__(self):
        print("Father class constructor")

    def show_father(self):
        print("Father class method")

class Son(Father):
    def __init__(self):
        print("Son class constructor")
    def show_son(self):
        print("Son class method")

class Grandson(Son):
    def __init__(self):
        print("Grandson class constructor")
    def show_grandson(self):
        print("Grandson class method")

g = Grandson()
g.show_grandson()
g.show_son()
g.show_father()