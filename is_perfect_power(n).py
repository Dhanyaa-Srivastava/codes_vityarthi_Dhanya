import math

def is_perfect_power(n):
    if n < 2:
        return False
    
    max_exponent = int(math.log2(n)) + 1 
    for b in range(2, max_exponent + 1):
        a = int(round(n ** (1 / b)))  
        if a > 1 and a ** b == n:
            return True
    return False

num = int(input("Enter a number to check: "))
if is_perfect_power(num):
    print(f"{num} is a perfect power.")
else:
    print(f"{num} is not a perfect power.")
