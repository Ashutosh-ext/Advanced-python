#Creating a class

class Greeting:
    message = "Hello"

    def say_hello(self):
        print(self.message)

    #creating an object
    greet = Greeting()
    greet.say_hello()