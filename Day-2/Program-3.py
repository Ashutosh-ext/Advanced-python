
class Computer:
    def __init__(self,name,ram,rom):
        self.name = name
        self.ram = ram
        self.rom = rom
    def display(self):
        print("Name:",self.name)
        print("Ram:", self.ram)
        print("Rom:", self.rom)

n1 = Computer("Dell","16","512")
n2 = Computer("Hp","32","512")
n1.display()
n2.display()