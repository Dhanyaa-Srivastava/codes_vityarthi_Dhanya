import math

def prime_pi(n):
    if n < 2:
        return 0
    return int(n / math.log(n))   # approximation using Prime Number Theorem

# Example
print(prime_pi(10))    # Output: 4 (approx)
print(prime_pi(100))   # Output: 21 (actual is 25)
print(prime_pi(1000))  # Output: 145 (actual is 168)