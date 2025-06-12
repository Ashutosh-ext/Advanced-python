class Distance:
    def __init__(self,km=0,m=0):
        self.km = km + m // 1000
        self.m = m % 1000

    def __add__(self, other):
        total_km = self.km + other.km
        total_m = self.m + other.m

        if total_m >= 1000:
            total_km += total_m//1000
            total_m = total_m % 1000


        return Distance(total_km, total_m)
    def __repr__(self):
        return f'km: {self.km}, m: {self.m}'

dist1 = Distance(5,700)
dist2 = Distance(3,400)
print(dist1 + dist2)