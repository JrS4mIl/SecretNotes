from tkinter import *
from tkinter import messagebox
import base64


windows=Tk()
windows.title('Screet Notes')
windows.minsize(width=550,height=800)


parola='samil_44'

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)



logo=PhotoImage(file='topsecret.png')
lbl_image=Label(windows,image=logo)
lbl_image.place(x=220,y=100)


def control():
    global parola
    sifre=key_entry.get()

    if sifre == parola:
        with open('dosya.txt', 'a') as dosya:
            dosya.write(entry_title.get() + ':\n')
            dosya.write(encode(key_entry.get(),myText.get('1.0',END)))

            succes = messagebox.showinfo('Kayit Edildi', 'Tebrikler Yaziniz Yazildi')
            entry_title.delete("0", END)
            myText.delete("1.0", END)
            key_entry.delete("0", END)
    elif entry_title.get() == "" or myText.get("1.0", END) == "":
        uyari = messagebox.showinfo('ERROR!!', 'Text ve Title Boş Geçilemez')
    else:
        message = messagebox.showinfo('Uyari!!', '!!!! Parola Yanlis veya Girilmemis')

def decrypted_notes():
    message_encrypted=myText.get("1.0",END)
    master_key=key_entry.get()
    if len(message_encrypted)==0 or len(master_key)==0:
        messagebox.showinfo('Error','Sifre yanlis veya Girilmemis Kardes')
    else:
        try:
            decode_message=decode(master_key,message_encrypted)
            myText.delete("1.0",END)
            myText.insert("1.0",decode_message)
        except:
            messagebox.showerror('Error','Bu mesaj encrypt e uygun degil kardes')



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

decrypt=Button(text='Decrypt',font=('Arial',9,'bold'),command=decrypted_notes)
decrypt.config(width=10)
decrypt.place(x=240,y=670)


windows.mainloop()