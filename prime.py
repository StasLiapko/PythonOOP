def is_prime(n):
    """Функція, яка перевіряє, чи є число простим."""
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_generator(limit):
    """
    Генераторна функція, яка повертає прості числа до заданої верхньої межі.

    Параметри:
    limit (int): Верхня межа діапазону простих чисел.

    Yields:
    int: Прості числа до верхньої межі (не включаючи її).
    """
    for number in range(2, limit):
        if is_prime(number):
            yield number

# Приклад використання
upper_limit = 20
for prime_number in prime_generator(upper_limit):
    print(prime_number)