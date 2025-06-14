def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice
@do_twice
def message(name):
    print(f"Hello {name}")

message("Ashutosh")