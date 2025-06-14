class Drone:
    def fly(self):
        print("Drone can fly")

class Airplane():
    def fly(self):
        print("Airplane can fly")

class Bird:
    def fly(self):
        print("Bird can fly")

for obj in (Drone(),Airplane(), Bird()):
    obj.fly()