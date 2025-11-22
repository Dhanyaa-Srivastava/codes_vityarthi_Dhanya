def factorial(n):
    if n>1:
        fact = 1
        for i in range (1,x+1,1):
            fact=fact*i
        
        return fact
    else:
        return "Does not exist"

x = int(input("Enter a number = "))
    
print("Factorial = ", factorial(x))