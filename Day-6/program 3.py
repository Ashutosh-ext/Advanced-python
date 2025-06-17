def print_name(prefix):
    print("Searching prefix:{}".format(prefix))
    try:
        while True:
            name = (yield)
            if prefix in name:
                print(name)
    except GeneratorExit:
        print("Closing")
corou = print_name("Dear")
next(corou)
corou.send("Dear")
corou.send("Dear World")
corou.close()