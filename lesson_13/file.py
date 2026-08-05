file1=open('exam.txt','w')
file=open('file1.txt','r')
n=file.readlines()
for i in range(len(n)):
    print(f'{i+1}. {n[i].strip()}')

for i in n:
    if i.startswith('hello'):
        pass
    else:
        print(i.strip())
file.close()
file1=open('exam.txt','w')
for i in range(len(n)):
    file1.write(n[i])