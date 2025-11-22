def is_harshad(n):
    # Convert the number to a string to get each digit
    digits = [int(d) for d in str(n)]
    
    # Find the sum of all digits
    digit_sum = sum(digits)
    
    # To avoid dividing by zero
    if digit_sum == 0:
        return False
        
    # Check if the number is divisible by the sum of its digits
    return n % digit_sum == 0
    
print(is_harshad(18))  # True
print(is_harshad(19))  # False