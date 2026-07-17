num_input=int(input("what is your number"))
i= True
count=2 
while i and count<num_input:
    
    if num_input%count ==0:
        i=False
    count=count+1

if i:
    print("your number is prime")
else:
    print("your number is not prime")
