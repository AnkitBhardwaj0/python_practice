from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

def handle_login():
    email=Email_input.get()
    password=password_input.get()
    if email=="ankit@gmail.com" and password=="helloankit":
        messagebox.showinfo('success','login successful')
    else:
        messagebox.showinfo('error','login failed')

root=Tk()
root.title('my GUI')
root.iconbitmap(r'GUI\star.ico')
root.geometry("300x500+100+50")
root.config(background='blue')

img=Image.open(r'GUI\image_folder\mfsd9q.jpg')
resized_img=img.resize((100,100))
img=ImageTk.PhotoImage(resized_img)
label = Label(root, image=img)
label.pack(pady=(10,10))

text_label = Label(root, text="Jay Shree Ganesh")
text_label.config(
    font=("Arial", 10, "bold"),
    fg="yellow",bg="blue"
)
text_label.pack()
Email_label=Label(root,text='enter Email',fg='white',bg='blue')
Email_label.pack(pady=(20,5))
Email_label.config(font=('verdana',12))
Email_input=Entry(root,width=30)
Email_input.pack(ipady=6,pady=(1,15))

password_label=Label(root,text='enter password',fg='white',bg='blue')
password_label.pack(pady=(20,5))
password_label.config(font=('verdana',12))
password_input=Entry(root,width=30,show='*')
password_input.pack(ipady=6,pady=(1,15))

login_button=Button(root,text='login here',fg='black',bg='yellow',command=handle_login)
login_button.pack(pady=(10,20))
login_button.config(font=("verdana",10))

root.mainloop()