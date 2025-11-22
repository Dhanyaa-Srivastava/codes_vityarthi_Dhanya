def collatz_length(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2  
        else:
            n = 3 * n + 1  
        steps += 1
    return steps

number = int(input("Enter a positive integer: "))
print(f"Number of steps for {number} to reach 1:", collatz_length(number))
