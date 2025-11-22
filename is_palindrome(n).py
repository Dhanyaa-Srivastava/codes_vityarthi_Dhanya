def is_palindrome(n):
    return str(n) == str(n)[::-1]

try:
    user_input = int(input("Enter a number: "))
    if is_palindrome(user_input):
        print(f"{user_input} is a palindrome.")
    else:
        print(f"{user_input} is not a palindrome.")
except ValueError:
    print("Invalid input. Please enter an integer.")