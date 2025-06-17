from time import sleep
students = ['Ashutosh','Dhruv','Arpit','Harshit']
def read():
    sleep(3)
    print("Reading done...")
    data = students
    while True:
        name = (yield)
        if name in data:
            print("Found!")
        else:
            print("Not found!")
search = read()
print("Reading all data...")
next(search)
search.send("Mayank")
search.send("Harshit")