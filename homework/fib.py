def fib(num):
    if num ==1:
        return 0
    elif num==2:
        return 1
    else:
        pass 
    return fib(num-1)+fib(num-2)
a=int(input("input number"))
print(fib(a))
    
