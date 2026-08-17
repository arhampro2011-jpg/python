n=int(input('what is num'))
rn=0
on=n
while n>0:
    rn=rn*10+n%10
    n=n//10

if rn==on:
    print('numm is palindrome')
else:
    print('not a palindrome')
    

