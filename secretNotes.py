from tkinter import *
from tkinter import messagebox
import hashlib
windows=Tk()
windows.title('Screet Notes')
windows.minsize(width=550,height=800)


parola='samil_44'
def hash_text(text):
    return hashlib.sha256(text.encode()).hexdigest()
logo=PhotoImage(file='topsecret.png')
lbl_image=Label(windows,image=logo)
lbl_image.place(x=220,y=100)


def control():
    global parola
    sifre=key_entry.get()

    if sifre == parola:
        with open('dosya.txt', 'a') as dosya:
            dosya.write(entry_title.get() + ':\n')
            dosya.write(hash_text(myText.get("1.0", END)) + '\n')
            succes = messagebox.showinfo('Kayit Edildi', 'Tebrikler Yaziniz Yazildi')
            entry_title.delete("0", END)
            myText.delete("1.0", END)
            key_entry.delete("0", END)
    elif entry_title.get() == "" or myText.get("1.0", END) == "":
        uyari = messagebox.showinfo('ERROR!!', 'Text ve Title Boş Geçilemez')
    else:
        message = messagebox.showinfo('Uyari!!', '!!!! Parola Yanlis veya Girilmemis')
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

save=Button(text='Save & Encrypt',font=('Arial',9,'bold'),command=control)
save.config(width=15)
save.place(x=230,y=635)

decrypt=Button(text='Decrypt',font=('Arial',9,'bold'))
decrypt.config(width=10)
decrypt.place(x=240,y=670)


windows.mainloop()