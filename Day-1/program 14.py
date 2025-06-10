from functools import reduce
list1 = [10,20,30,40,50,60,70,80,90]
largest = reduce(lambda x,y:x if x>y else y,list1)
print(largest)