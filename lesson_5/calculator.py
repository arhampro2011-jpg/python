error=False
def addition(x,y):
    return x+y
def multiplication(x,y):
    return x*y
def div(x,y):
    return x/y
def sub(x,y):
    return x-y
while True:
    a=float(input("input first  num"))
    b=float(input("input second num"))
    dec=int(input("enter 1/addition 2/division 3/multipliaction 4/subtraction"))

    if dec==1:
        print("addition of two num is", addition(a,b))
    elif dec==2:
        if b!=0:
            print("division of two num is", div(a,b))
        else:
            print("cannot divide bby 0")
    elif dec==3:
        print("multiplication of two num is", multiplication(a,b))
    elif dec==4:
        print("subtraction of two num is", sub(a,b))
    else:
        print("invalid choice")

