a=int(input('type your no'))
reverse=0
while a>0:
    reverse=reverse*10+(a%10)
    a=a//10

print(reverse)