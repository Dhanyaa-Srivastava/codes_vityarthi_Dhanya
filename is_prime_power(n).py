def is_prime_power(n):
    if n <= 1:
        return False

    def is_prime(x):
        if x <= 1:
            return False
        if x <= 3:
            return True
        if x % 2 == 0 or x % 3 == 0:
            return False
        i = 5
        while i * i <= x:
            if x % i == 0 or x % (i + 2) == 0:
                return False
            i += 6
        return True

    for k in range(1, int(n.bit_length()**0.5) + 2):
        p = int(round(n ** (1 / k)))
        for candidate in [p-1, p, p+1]:
            if candidate > 1 and is_prime(candidate) and candidate ** k == n:
                return True
    return False

x = int(input("Enter  a number = "))
print(is_prime_power(x))