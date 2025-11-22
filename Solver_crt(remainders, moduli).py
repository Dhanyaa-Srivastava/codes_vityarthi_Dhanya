def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def mod_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Inverse doesn't exist, moduli might not be coprime.")
    return x % m

def Solver_crt(remainders, moduli):
    M = 1
    for m in moduli:
        M *= m
    result = 0
    for r_i, m_i in zip(remainders, moduli):
        M_i = M // m_i
        inv = mod_inverse(M_i, m_i)
        result += r_i * M_i * inv
    return result % M

# Taking inputs from user
n = int(input("Enter number of congruences: "))
remainders = []
moduli = []

print("Enter the remainders and moduli:")
for i in range(n):
    r = int(input(f"Remainder r[{i+1}]: "))
    m = int(input(f"Modulus m[{i+1}]: "))
    remainders.append(r)
    moduli.append(m)

try:
    solution = Solver_crt(remainders, moduli)
    print(f"The solution x such that x ≡ r[i] mod m[i] is: {solution}")
except ValueError as e:
    print(e)
