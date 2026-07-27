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
label.pack()
root.mainloop()