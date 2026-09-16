f=open('file.txt','w') 
content=''
for i in range(5):
    a=input('what do u want to write')
    content+=a
    
f.write(content)
f.close()
f=open('file.txt','r') 
print(f.readlines())
f.close()

