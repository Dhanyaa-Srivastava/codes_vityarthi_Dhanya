def aliquot_sum(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total

x = int(input("Enter a number = "))
print(aliquot_sum(x))
