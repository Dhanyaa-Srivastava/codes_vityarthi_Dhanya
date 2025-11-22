def is_quadratic_residue(a, p):
    if a % p == 0:
        return True
    result = pow(a, (p - 1) // 2, p)
    return result == 1

a = int(input("Enter a: "))
p = int(input("Enter an odd prime p: "))
if is_quadratic_residue(a, p):
    print(f"{a} is a quadratic residue modulo {p}.")
else:
    print(f"{a} is NOT a quadratic residue modulo {p}.")
