from tkinter import *

windows=Tk()
windows.title('Screet Notes')
windows.minsize(width=550,height=800)

logo=PhotoImage(file='topsecret.png')
lbl_image=Label(windows,image=logo)
lbl_image.place(x=220,y=100)

lb_title=Label(text='Enter your Title',font=('Arial',13,'bold'))
lb_title.config(fg='black')
lb_title.place(x=220,y=250)

entry_title=Entry()
entry_title.place(x=190,y=280)
entry_title.config(width=30)

lbl_secret=Label(text='Enter your Secret Note',font=('Arial',13,'bold'))
lbl_secret.place(x=190,y=310)


myText=Text(width=30,height=14)
myText.place(x=170,y=340)

key=Label(text='Enter Master Key',font=('Arial',13,'bold'))
key.place(x=210,y=580)

key_entry=Entry()
key_entry.place(x=175,y=610)
key_entry.config(width=35)

save=Button(text='Save & Encrypt',font=('Arial',9,'bold'))
save.config(width=15)
save.place(x=230,y=635)

decrypt=Button(text='Decrypt',font=('Arial',9,'bold'))
decrypt.config(width=10)
decrypt.place(x=240,y=670)


windows.mainloop()