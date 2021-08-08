import tkinter
import random

#import library

from tkinter import *
import random


#Create the Window


root = Tk()
root.geometry("500x300")
root.resizable(0,0)
root.title("Stone : Paper : Scissors")
Label(root,text=("Stone,Paper,Scissors"),font=("arial 20 bold"),bg=("gray")).place(x=110,y=0)



user_take=StringVar()
Label(root,text=("Choose any one:Stone,Paper,Scissors"),font=("arial 15 bold"),bg=("gray")).place(x=60,y=70)
Entry(root,textvariable=user_take,width=50,bg="light blue").place(x=90,y=130)


#computer Choice

comp=["stone","paper","scissors"]
comp_pick=random.choice(comp)
 
#comp_pick=random.randint(1,3)
#if comp_pick==1:
     #comp_pick = "stone"
#elif comp_pick==2:
     #comp_pick = "paper"
#else:
     #comp_pick = "scissors"

#function

Result=StringVar()

def Reset():
    user_take.set("")
    Result.set("")

def Exit():
    root.destroy()

def play():
    
 user_pick = user_take.get()  

 if comp_pick==user_pick:
   Result.set("Tie,You both select same "+comp_pick)
 elif comp_pick=="stone" and user_pick=="scisssors":
    Result.set("You Loose,Computer Select "+comp_pick)
 elif comp_pick=="stone" and user_pick=="paper":
   Result.set("You Win,Computer Select "+comp_pick)
 elif comp_pick=="paper" and user_pick=="stone":
   Result.set("You Loose,Computer Select "+comp_pick)
 elif comp_pick=="paper" and user_pick=="scissors":
    Result.set("You Won,Computer Select "+comp_pick)
 elif comp_pick=="scissors" and user_pick=="stone":
    Result.set("You Win,Computer Select "+comp_pick)
 elif comp_pick=="scissors" and user_pick=="paper":
    Result.set("You Loose,Computer Select "+comp_pick)
 else:
    Result.set("Invalid!!!,Computer Select "+comp_pick)

#Button and Result Show

Entry(root,font=("arial 10 bold"),textvariable=Result,width=50,bg=("antiquewhite2")).place(x=70,y=215)
Button(root,text=("PLAY"),bg=("seashell4"),command=play,font=("arial 10 bold")).place(x=220,y=165)
Button(root,text=("RESET"),bg=("seashell4"),command=Reset,font=("arial 10 bold")).place(x=70,y=250)
Button(root,text=("EXIT"),bg=("seashell4"),command=Exit,font=("arial 10 bold")).place(x=380,y=250)

    
