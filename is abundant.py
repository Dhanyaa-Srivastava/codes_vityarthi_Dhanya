def is_abundant(n):
    if n < 1:
        return False
    
    total = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != 1 and i != n // i:
                total += n // i
                
    return total > n

x = int(input("Enter a number = "))
print(is_abundant(x))