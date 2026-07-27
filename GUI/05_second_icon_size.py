from tkinter import * 

root = Tk()
root.title("my gui")

icon =PhotoImage(file="GUI\computer.png")
root.iconphoto(True, icon)
root.geometry('300x500')

root.mainloop()