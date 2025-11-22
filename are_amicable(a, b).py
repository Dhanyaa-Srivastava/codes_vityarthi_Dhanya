def sum_of_divisors(n):
    result = 0
    for i in range(1, n):
        if n % i == 0:
            result += i
    return result

def are_amicable(a, b):
    return sum_of_divisors(a) == b and sum_of_divisors(b) == a

x = int(input("Enter a number = "))
y = int(input("Enter a number = "))
print(are_amicable(x, y))