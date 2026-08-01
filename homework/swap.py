num1=int(input('what is no'))
num2=int(input('what is second no'))
i=10
while num1/i>1:
    i=i*10

num2+=num1/i
num1=num2//1
num2=(num2-(num2//1))*i

print(f'first no is now {num1} and second no is now{num2}')