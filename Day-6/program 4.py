List = [4, 6, 9, 1, 5, 4, 7, 8, 3, 12 , 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
iter_obj = iter(List)
print(iter_obj)
print(type(iter_obj))
print(next(iter_obj))
for i in iter_obj:
    print(i)

