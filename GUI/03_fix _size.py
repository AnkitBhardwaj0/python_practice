from tkinter import *
root=Tk()
root.title('my GUI')
root.minsize(100, 100)      # Minimum allowed size
root.maxsize(800, 600)      # Maximum allowed size
root.geometry("300x300")    # Initial size
root.resizable(True, True)  # Allow resizing
root.mainloop()