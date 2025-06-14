def rev_str(my_str):
    length = len(my_str)
    for i in range(length -1, -1, -1):
        yield my_str[i]

n = input("Enter a string: ")
for char in rev_str(n):
    print(char)