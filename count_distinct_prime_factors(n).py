def count_distinct_prime_factors(n):
    count = 0
    # Check for factor 2
    if n % 2 == 0:
        count += 1
        while n % 2 == 0:
            n //= 2

    # Check for odd factors from 3 to sqrt(n)
    factor = 3
    while factor * factor <= n:
        if n % factor == 0:
            count += 1
            while n % factor == 0:
                n //= factor
        factor += 2

    # If n is still greater than 1, it is a prime factor itself
    if n > 1:
        count += 1

    return count

x = int(input("Enter a number = "))
print(count_distinct_prime_factors(x))

