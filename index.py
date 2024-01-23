from tkinter import *
import pyscreenrec

# Create the main Tkinter window
root = Tk()
root.geometry("400x600")
root.title("Python Screen Recorder")
root.config(bg="#fff")
root.resizable(False, False)

# Function to start the recording
def start_rec():
    file = Filename.get()
    rec.start_recording(str(file + ".mp4"), 5)

# Function to pause the recording
def pause_rec():
    rec.pause_recording()

# Function to resume the recording
def resume_rec():
    rec.resume_recording()

# Function to stop the recording
def stop_rec():
    rec.stop_recording()

# Create an instance of ScreenRecorder from pyscreenrec library
rec = pyscreenrec.ScreenRecorder()

# Set the application icon
image_icon = PhotoImage(file="record.png")
root.iconphoto(False, image_icon)

# GUI elements
lbl = Label(root, text="Python Screen Recorder", bg="#fff", font="arial 15 bold")
lbl.pack(pady=20)

# Image for the recording icon
image3 = PhotoImage(file="recording.png")
Label(root, image=image3, bd=0).pack(pady=30)

# Entry for the recording filename
Filename = StringVar()
entry = Entry(root, textvariable=Filename, width=18, font="arial 15")
entry.place(x=100, y=350)
Filename.set("recording filename")

# Buttons for various recording actions
start = Button(root, text="Start", font="arial 22", bd=0, command=start_rec)
start.place(x=140, y=250)

image4 = PhotoImage(file="pause.png")
pause = Button(root, image=image4, bd=0, bg="#fff", command=pause_rec)
pause.place(x=50, y=450)

image5 = PhotoImage(file="play.png")
play = Button(root, image=image5, bd=0, bg="#fff", command=resume_rec)
play.place(x=150, y=450)

image6 = PhotoImage(file="stop.png")
stop = Button(root, image=image6, bd=0, bg="#fff", command=stop_rec)
stop.place(x=250, y=450)

# Start the Tkinter event loop
root.mainloop()