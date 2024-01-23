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
start=Button(root,text="Start",font="arial 22",bd=0)
start.place(x=140,y=250)

image4=PhotoImage(file="pause.png")
pause=Button(root,image=image4,bd=0,bg="#fff")
pause.place(x=50,y=450)

image5=PhotoImage(file="play.png")
play=Button(root,image=image5,bd=0,bg="#fff")
play.place(x=50,y=450)

image6=PhotoImage(file="stop.png")
stop=Button(root,image=image6,bd=0,bg="#fff")
stop.place(x=50,y=450)

root.mainloop()