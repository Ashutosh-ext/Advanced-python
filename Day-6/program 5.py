lt = [52,12,17,23,47,44]
def my_for_loop(iterable):
    iterator = iter(iterable)
    try:
        while True:
            print(next(iterator))
    except StopIteration:
        pass
my_for_loop(lt)