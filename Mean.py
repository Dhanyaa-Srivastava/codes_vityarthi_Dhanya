def mean_of_digits(n):
    total = 0   # This will hold the sum of all digits
    count = 0   # This will count the number of digits
    
    n = abs(n)  # If n is negative, convert it to positive (so -123 works too)
    
    while n > 0:
        digit = n % 10      # Get the last digit
        total += digit      # Add it to the running total
        count += 1          # Increase the count by one
        n = n // 10         # Remove the last digit from n
    
    if count == 0:          # Prevent division by zero (for n=0)
        return 0
    return total / count    # Calculate mean (average)
print(mean_of_digits(642))   