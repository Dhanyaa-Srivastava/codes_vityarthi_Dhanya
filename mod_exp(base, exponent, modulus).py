def mod_exp(base, exponent, modulus):
    if modulus == 1:
        return 0
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:  # If exponent is odd
            result = (result * base) % modulus
        exponent = exponent >> 1  # Divide exponent by 2
        base = (base * base) % modulus
    return result

x = int(input("Enter a number = "))
y = int(input("Enter a number = "))
z = int(input("Enter a number = "))
print(mod_exp(x, y, z))