from functools import reduce
list1 = [10,20,30,40,50,60,70,80,90]
result = reduce(lambda x,y:x+y,list1)
print(result)