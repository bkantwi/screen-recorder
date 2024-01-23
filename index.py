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

#heading
lbl=Label(root,text="Python Screen REcorder",bg="#fff",font="arial 15 bold")
lbl.pack(pady=20)

image3=PhotoImage(file="recording.png")
Label(root,image=image3,bd=0).pack(pady=30)

#buttons


root.mainloop()