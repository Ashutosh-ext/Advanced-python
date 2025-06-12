class Mass:
    def __init__(self, kg=0, g=0):
        self.kg = kg + g//1000
        self.g = g % 1000
    def __add__(self, other):
        total_kg = self.kg + other.kg
        total_g = self.g + other.g

        if total_g >= 1000:
            total_kg += total_g // 1000
            total_g -= total_g % 1000

        return Mass(total_kg, total_g)
    def __repr__(self):
        return f"{self.kg} kg and {self.g} g"

mass1 = Mass(2,500)
mass2 = Mass(3,500)
print(mass1 + mass2)