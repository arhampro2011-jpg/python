l=[4,46,485,373,4,59,847,48,129,759]
chigh=l[0]
clow=l[0]
for i in range(len(l)):
    if l[i]>chigh:
        chigh=l[i]
    elif l[i]<clow:
        clow=l[i]

print(chigh,'highest')
print(clow,'lowest')