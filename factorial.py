def Factorial(num):
    if num==0:
        return 1
    else:
        return num*Factorial(num-1)
         
num = int(input("Enter number here: "))
print(Factorial(num))    
    
    
