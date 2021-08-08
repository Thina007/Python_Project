import tkinter
import pytube



#impot the lib:

from tkinter import *
from pytube import YouTube



#Creat Window:

root=Tk()
root.geometry("500x300")
root.resizable(0,0)
root.title("YouTube Downloder")

Label(root,text="YouTube Downloder",font="arial 20 bold").pack()



#Creat YouTube Enter Link Path:

link=StringVar()
Label(root,text="Enter The YouTube Link",font="arial 15").place(x=160,y=60)
Entry(root,bd=1,width=70,textvariable=link,bg="light blue").place(x=32,y=100)


#function for Download Video's:

def download():
    url=YouTube(str(link.get()))
    video=url.streams.first()
    video.download()
    Label(root,text="Your Video is Downloaded...",font="arial 15 ").place(x=130,y=210)

Button(root,text="DOWNLOAD",font="arial 15 bold",command=download,bg="pale violet red").place(x=180,y=150)

root.mainloop()

