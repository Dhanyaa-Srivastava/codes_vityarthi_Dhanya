def twin_primes(limit):
    if limit < 3:
        return []

    # Sieve of Eratosthenes to find primes up to limit
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False

    # Collect twin prime pairs
    twins = []
    for p in range(3, limit - 1):
        if sieve[p] and sieve[p + 2]:
            twins.append((p, p + 2))

    return twins

n = int(input("Enter a number = "))
print(twin_primes)