def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_generator(upper_limit):
    for num in range(2, upper_limit):
        if is_prime(num):
            yield num

upper_limit = 20
print(f"Prime numbers up to {upper_limit}:")
for prime_num in prime_generator(upper_limit):
    print(prime_num, end = " ")