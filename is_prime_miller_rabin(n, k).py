import random
def is_prime_miller_rabin(n, k):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

test_numbers = [2, 17, 18, 19, 20, 7919, 7920]
k = 5 
for num in test_numbers:
    if is_prime_miller_rabin(num, k):
        print(f"{num} is probably prime.")
    else:
        print(f"{num} is composite.")
