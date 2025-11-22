import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

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

def prime_factors(n):
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n //= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.add(i)
            n //= i

    if n > 2:
        factors.add(n)
    return factors

def is_carmichael(n):
    if n < 2 or is_prime(n):
        return False  

    factors = prime_factors(n)
    product = 1
    for p in factors:
        if n % (p * p) == 0:
            return False  

    for p in factors:
        if (n - 1) % (p - 1) != 0:
            return False
    return True

n = int(input("Enter a composite number to check if Carmichael: "))
if is_carmichael(n):
    print(f"{n} is a Carmichael number.")
else:
    print(f"{n} is not a Carmichael number.")
