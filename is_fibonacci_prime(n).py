import math

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def is_perfect_square(x):
    s = int(math.isqrt(x))
    return s * s == x

def is_fibonacci(number):
    return is_perfect_square(5 * number * number + 4) or is_perfect_square(5 * number * number - 4)

def is_fibonacci_prime(n):
    return is_fibonacci(n) and is_prime(n)

num = int(input("Enter a number to check: "))
if is_fibonacci_prime(num):
    print(f"{num} is a Fibonacci prime.")
else:
    print(f"{num} is not a Fibonacci prime.")
