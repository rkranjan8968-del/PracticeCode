def factorial(num):
    result = 1                        # start with 1
    for i in range(1,num+1):          # loop from 1 to n
        result *= i                   # multiply result by i each time 
    return result                     # result the final product

print("Factorial of 5 is",factorial(5))     # Factorial of 5 is 120
    
    
    
    
