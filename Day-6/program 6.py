import sys
L = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for num in L:
    print(num**2)

print("For L",sys.getsizeof(L),"Bytes")
var = range(1,16)
for num in var:
    print(num**2)
print("for var",sys.getsizeof(var),"Bytes")