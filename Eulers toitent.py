import math
import time

start_time = time.perf_counter()

def euler_phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def bytes_needed(n):
    if n == 0:
        return 1
    return (n.bit_length() + 7) // 8   

n = int(input("Enter a number: "))
phi = euler_phi(n)

end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"Execution time",(execution_time),"seconds")
print(f"Euler's Totient φ({n}) = {phi}")
print(f"Bytes needed to store φ({n}) = {bytes_needed(phi)}")