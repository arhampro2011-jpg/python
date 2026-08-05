n=[4,3,5,6,3,3,3,8,67,5,35,6,7,3,3,3]
frequency={}
for i in range(len(n)):
    if n[i] in frequency:
        frequency[n[i]]+=1
    else:
        frequency[n[i]]=1

print(frequency)
maxcount=0
mostf=0
for i in frequency:
    if frequency[i]>maxcount:
        maxcount=frequency[i]
        mostf=i

print(f'most frequent numer is {mostf} and frequency is {maxcount}')