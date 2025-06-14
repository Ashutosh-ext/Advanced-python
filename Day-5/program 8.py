#Abstract method and concrete method
from abc import ABC, abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):              #abstract method
        pass
    def message(self):              #concrete method
        print("Computer is an electronic device")

class Laptop(Computer):
    def process(self):
        print("Executing laptop process")

class Desktop(Computer):
    def process(self):
        print("Executing desktop process")

com1 = Laptop()
com2 = Desktop()
com1.process()
com2.process()
