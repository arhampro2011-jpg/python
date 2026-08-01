file=open('file1.txt','r')
a=file.readlines()
for i in range(len(a)):
    print(a[i].strip())
file.close()