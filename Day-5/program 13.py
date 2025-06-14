from datetime import datetime

def not_during_night(func):
    def inner():
        if 7<= datetime.now().hour < 22:
            func()
        else:
            print("Sorry! Unable to play music in night")
    return inner
@not_during_night
def music():
    print("Music playing")

music()