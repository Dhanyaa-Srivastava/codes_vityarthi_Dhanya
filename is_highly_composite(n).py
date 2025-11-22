def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 2 if i != n // i else 1
    return count

def is_highly_composite(n):
    n_divisors = count_divisors(n)
    for i in range(1, n):
        if count_divisors(i) >= n_divisors:
            return False
    return True

x = int(input("Enter a number = "))
print(is_highly_composite(x))