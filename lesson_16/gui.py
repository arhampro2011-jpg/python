from tkinter import *
window=Tk()
window.title('profile card')
window.geometry('400x400')
title=Label(window, text='my profile card', bg='blue', fg='orange', width=40)
title.grid(row=0, column=0, columnspan=2, padx=50, pady=10)

namel=Label(window, text='name:', bg='blue', fg='orange', width=15)
namel.grid(row=1, column=0, padx=10, pady=10)

hobbyl=Label(window, text='hobby:', bg='blue', fg='orange', width=15)
hobbyl.grid(row=2, column=0, padx=10, pady=10)

namee=Entry(window, fg='black', bg='beige',width=25)
namee.grid(row=1, column=1,padx=10,pady=10)

hobbye=Entry(window, fg='black', bg='beige',width=25)
hobbye.grid(row=2, column=1,padx=10,pady=10)

abtme=Frame(window)
abtme.grid(row=3,column=0,columnspan=2,padx=10,pady=10)
abtl=Label(abtme, text='About me', bg='blue', fg='orange', width=40)
abtl.pack()

abtt=Text(abtme, fg='black', bg='beige',width=40, height=4)
abtt.pack()

submit= Button(window, text='show profile card', bg='blue', fg='orange', width=15)
submit.grid(row=4,column=0,columnspan=2,padx=10,pady=10)
window.mainloop()
