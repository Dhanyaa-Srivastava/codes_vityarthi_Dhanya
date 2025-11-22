import random
import math
def pollard_rho(n):
    if n % 2 == 0:
        return 2
    def g(x):
        return (x * x + 1) % n
    x = 2
    y = 2
    d = 1
    while d == 1:
        x = g(x)
        y = g(g(y))
        d = math.gcd(abs(x - y), n)
    if d == n:
        return None  
    else:
        return d
    
n = 8051
factor = pollard_rho(n)
if factor is None:
    print(f"Failed to find a non-trivial factor of {n}")
else:
    print(f"A non-trivial factor of {n} is {factor}")
