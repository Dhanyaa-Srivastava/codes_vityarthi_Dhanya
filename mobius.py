def mobius(n):
    if n == 1:  # Base case
        return 1
        
    p = 0  # Count of distinct primes
    i = 2
    while i * i <= n:
        if n % i == 0:
            p += 1
            n //= i
            if n % i == 0:
                return 0  # Found a squared prime factor
        i += 1
    if n > 1:  # If the remaining number is a prime
        p += 1
    return 1 if p % 2 == 0 else -1

# Examples
print(mobius(19))  # -1
print(mobius(36))  # 0
print(mobius(6))   # 1