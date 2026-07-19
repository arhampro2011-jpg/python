def factorial(num):
    if num==1:
        return num
    return num*factorial(num-1) 
    


n=int(input("enter number"))

print(factorial(n))
