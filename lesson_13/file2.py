import os
content=''
with open('exam.txt','r') as f:
    print('file is being added')
    content+=f.read()
    for i in f.readlines():
        print(len(i.split()),'words:',i.strip())
    
    
with open('file1.txt','r') as f:
    print('file is being added')
    content+=f.read()

with open('file2.txt','w') as f:
    f.write(content)
if os.path.exists('file2.txt'):
    print('file created succesfully')
else:
    print('error in creating file')

a=input('type delete to remove the file')
if a=='delete':
    os.remove('exam.txt')