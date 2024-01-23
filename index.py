from tkinter import *
import pyscreenrec

root=Tk()
root.geometry("400x600")
root.title("Python Screen Recorder")
root.config(bg="#fff")
root.resizeable(False,False)

rec=pyscreenrec.ScreenRecorder()

#icon
image_icon = PhotoImage(file="record.png")
root.iconphoto(False, image_icon)

#background images

root.mainloop()