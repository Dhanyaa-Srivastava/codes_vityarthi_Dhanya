def multiplicative_persistence(n):
    steps = 0
    while n >= 10:  # while n has more than one digit
        product = 1
        for digit in str(n):
            product *= int(digit)
        n = product
        steps += 1
    return steps

x = int(input("Enter a number = "))
print(multiplicative_persistence(x))