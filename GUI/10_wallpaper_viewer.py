from tkinter import *
from PIL import Image, ImageTk
import os
counter=1
def rotate_image():
    global counter
    counter=(counter) % len(img_array)
    img_label.config(image=img_array[counter])
    counter+=1

root=Tk()
root.title('wallpaper viewer')
root.iconbitmap(r'GUI\star.ico')
root.geometry("250x400")
root.config(background='black')

files=os.listdir("GUI\image_folder")
img_array=[]
for file in files:
    img=Image.open(os.path.join("GUI\image_folder",file))
    resized_image=img.resize((200,300))
    img_array.append(ImageTk.PhotoImage(resized_image))

img_label = Label(root, image=img_array[0])
img_label.pack(pady=(15,10))

next_button=Button(root,text='next',fg='black',bg='white',width=28,height=2,command=rotate_image)
next_button.pack()

root.mainloop()