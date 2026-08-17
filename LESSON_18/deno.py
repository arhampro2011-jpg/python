from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox

window=Tk()
window.title('deno calc')
window.geometry('400x400')
window.configure(bg='beige')

title=Label(window,text='my denomination calculator',bg='purple',fg='beige',width='50')
title.place(x=10,y=10)

img_1=Image.open('image.jpg')
photo_1=img_1.resize((320,180))
pic=ImageTk.PhotoImage(photo_1)
pic1=Label(window,image=pic)
pic1.place(x=10,y=40)

def bc1():
    a=messagebox.showinfo('alert','do u want to calculate')
    if a=='ok':
        top()

def top():
    tp=Toplevel()
    tp.title('deno calc')
    tp.geometry('400x400')
    
    label1=Label(tp,text='enetr totaal amt',bg='purple',fg='beige',width='50')
    label1.place(x=10,y=10)

    entryu=Entry(tp)
    entryu.place(x=150,y=35)

    l1=Label(tp,text='2000',bg='purple',fg='beige',width='20')
    l1.place(x=10,y=60)

    l2=Label(tp,text='500',bg='purple',fg='beige',width='20')
    l2.place(x=10,y=140)

    l3=Label(tp,text='100',bg='purple',fg='beige',width='20')
    l3.place(x=10,y=220)

    e1=Entry(tp)
    e1.place(x=200,y=60)

    e2=Entry(tp)
    e2.place(x=200,y=140)

    e3=Entry(tp)
    e3.place(x=200,y=220)

    
    def calculate():
        try:
            amt=int(entryu.get())
            n2000=amt//2000
            amt%=2000
            n500=amt//500
            amt%=500
            n100=amt//100
            
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)

            e1.insert(END,str(n2000))
            e2.insert(END,str(n500))
            e3.insert(END,str(n100))

        except:
            messagebox.showerror('alert','you have entered incorrect data')
    b2=Button(tp,text='calculate',bg='red',fg='beige',width='50',command=calculate)
    b2.place(x=10,y=300)





b1=Button(window,text='open denomination calculator',bg='purple',fg='beige',width='50',command=bc1)
b1.place(x=10,y=250)

window.mainloop()
