def is_deficient(n):
    if n <= 1:
        return True  # 1 and 0 are considered deficient by convention
    s = 1  # 1 is always a proper divisor
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            s += i
            if i != n // i:
                s += n // i
    return s < n

x = int(input("Enter a number = "))
print(is_deficient(x))
