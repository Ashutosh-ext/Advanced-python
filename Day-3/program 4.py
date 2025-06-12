#addition of month and year


class Year:
    def __init__(self,year=0,month=0):
        self.year = year + month // 12
        self.month = month % 12

    def __add__(self,other):
        total_year = self.year + other.year
        total_month = self.month + other.month

        if self.month >= 12:
            total_year = total_year + total_month // 12
            total_month = total_month % 12

        return Year(total_year,total_month)

    def __repr__(self):
        return f"year={self.year}, month={self.month}"

y1 = Year(5,7)
y2 = Year(3,4)
print(y1 + y2)