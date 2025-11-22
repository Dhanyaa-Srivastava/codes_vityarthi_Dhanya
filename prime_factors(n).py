def prime_factors(n):
    factors = []
    # Handle 2 separately to allow increments of 2 in further steps
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # Check odd numbers
    p = 3
    while p * p <= n:
        while n % p == 0:
            factors.append(p)
            n //= p
        p += 2
    # If n is greater than 1, then n itself is a prime
    if n > 1:
        factors.append(n)
    return factors

x = int(input("Enter a number = "))
print(prime_factors(x))