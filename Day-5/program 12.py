def decor(func):
    def inner():
        print("-------------------")
        func()

        print("-------------------")
    return inner
@decor
def msg():
    print("python programming")

msg()