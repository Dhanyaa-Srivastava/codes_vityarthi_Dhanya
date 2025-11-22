def is_pronic(num):
    for i in range (num+1):
        if i*(i+1)==num:
            return True 
    return False 

number=int(input("enter a number :"))    
if is_pronic(number):
    print(f"{number} is a pronic number")
else:
    print(f"{number}is not a pronic number ")    