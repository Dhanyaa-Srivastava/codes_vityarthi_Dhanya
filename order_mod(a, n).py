def order_mod(a, n):
    if gcd(a, n) != 1:
        return -1  # Order does not exist if a and n are not coprime
    
    k = 1
    current = a % n
    while current != 1:
        current = (current * a) % n
        k += 1
    
    return k

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# Example usage:
a = int(input("Enter base a: "))
n = int(input("Enter modulus n: "))
result = order_mod(a, n)
if result == -1:
    print(f"No order exists since {a} and {n} are not coprime.")
else:
    print(f"The order of {a} modulo {n} is {result}.")
