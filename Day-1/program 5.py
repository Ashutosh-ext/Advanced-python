#print all prime numbers from a list
a = [1,2,3,4,5,6,7,8,9,10]
for x in a:
    i = 1
    flag = 0
    while i <= x:
        if x%i == 0:
            flag = flag + 1
        i = i+1
    if flag == 2:
        print(i)