def divisor_sum(n):
  if n < 1:
    return 0
    
  total = 0
  for i in range(1, n + 1):
    if n % i == 0:
      total += i
  return total

try:
  num_input = input("Enter a positive integer: ")
  number = int(num_input)
  result = divisor_sum(number)
  print(f"The sum of the divisors for {number} is: {result}")
except ValueError:
  print("Invalid input. Please enter a whole number.")

