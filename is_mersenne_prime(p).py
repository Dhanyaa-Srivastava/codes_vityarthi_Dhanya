def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_mersenne_prime(p):
    if not is_prime(p):
        return False

    mersenne_number = (2**p) - 1
    return is_prime(mersenne_number)

n = int(input("Enter The Prime Number = "))
print(f"Is 2^n - 1 a Mersenne prime? {is_mersenne_prime(n)}")