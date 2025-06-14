def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def generate_primes(start, end):
    for num in range(start, end+1):
        if is_prime(num):
            yield num

primes_generator = generate_primes(5, 50)

for prime in primes_generator:
    print(prime,end=',')
    
