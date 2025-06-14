def generate_numbers():
    for num in range(1,11):
        yield num

numbers_generator = generate_numbers()
print(type(numbers_generator))

for num in numbers_generator:
    print(num)