import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox 
from datetime import datetime


gui = Tk()
gui.geometry("350x100")
gui.title("VLC OneClick Screen Capture !")


def getFolderPath():
    folder_selected  =  filedialog.asksaveasfilename(initialdir = "/",title = "Save file as...",defaultextension='.mp4',filetype=[('*.mp4', 'MP4 Files')])
    folderPath.set(folder_selected)

def GO():
    start_time = datetime.now()
    folder = folderPath.get()
   
    if folder == '':
        messagebox.showerror(title="Error...!", message="Empty Path, Please check your Path.")
   
    else:
        os.system('cmd /c ""C:/Program Files/VideoLAN/VLC/vlc.exe" screen:// --qt-start-minimized :screen-fps=25 :run-time=9999 :quiet :sout=#transcode{vcodec=h264,vb072}:standard{access=file,mux=mp4,dst='+folder+'}"')
        end_time = datetime.now()
        messagebox.showerror(title="Done", message=('Duration: {}'.format(end_time - start_time)))
def ABOUT():
    messagebox.showinfo("ALU DEV TEAM @ 2022", "by nikkpap (nikkpap@gmail.com)")

folderPath = StringVar()

lbl1 = Label(gui ,text="Save as capture...").grid(row=0,column = 0)
entry1 = Entry(gui,textvariable=folderPath, state=DISABLED).grid(row=0,column=1)

btnBrowse = ttk.Button(gui, text="Browse",command=getFolderPath).grid(row=0,column=2)
btnGO = ttk.Button(gui ,text="Go", command=GO).grid(row=4,column=0)
btnAbout = ttk.Button(gui ,text="About", command=ABOUT).grid(row=4,column=1)

gui.mainloop()
