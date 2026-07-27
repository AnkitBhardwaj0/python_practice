from tkinter import *
from PIL import Image, ImageTk
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
root.mainloop()