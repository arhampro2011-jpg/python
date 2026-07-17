num_string=str(input("what is your number "))
length=len(num_string)
total=0
for i in range(0,length):
    num_int=int(num_string[i])
    total=total+num_int**length
if total==int(num_string):
    print("number is armstrong number")
else:
    print("number is not armstrong number")
