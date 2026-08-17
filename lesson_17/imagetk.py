from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox

window=Tk()
window.title('image display')
window.geometry('400x400')

title=Label(window,text='this is an image',bg='purple',fg='white',width=40)
title.pack(pady=10)

img_1=Image.open('image.jpg')
photo_1=img_1.resize((320,180))
pic=ImageTk.PhotoImage(photo_1)
pic1=Label(window,image=pic)
pic1.pack()

def btn_f1():
    messagebox.showinfo('great','you liked this image')

btn_1=Button(window,text='click to like',bg='purple',fg='white',command=btn_f1)
btn_1.pack(pady=10)
def btn_f2():
    top=Toplevel()
    top.title('more details')
    top.geometry('200x200')
    text1=Label(top,text='taken on: today',fg='black')
    text1.pack(pady=10)
    text2=Label(top,text='location: my laptop',fg='black')
    text2.pack(pady=10)

btn_2=Button(window,text='see details',bg='purple',fg='white',command=btn_f2)
btn_2.pack(pady=10)


window.mainloop()