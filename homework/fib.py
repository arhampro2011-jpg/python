total=0

def fib(num):
    if num ==1:
        return 0
    elif num==2:
        return 1
    total=total+fib(num+1)
    return total
a=int(input("input number"))
print(fib(a))
    
