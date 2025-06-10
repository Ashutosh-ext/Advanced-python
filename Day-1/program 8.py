def sum_num(num1 , *num):
    result = num1
    for i in num:
        result = result + i
    return result
print(sum_num(1,2,3,4))