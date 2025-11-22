def count_divisors(n):
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            # If divisors are equal, count only once
            if i * i == n:
                count += 1
            else:
                # Count both divisors i and n//i
                count += 2
        i += 1
    return count

x = int(input("Enter a number = "))
print(count_divisors(x))