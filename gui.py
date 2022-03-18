import tkinter
from tkinter import *
from Alexa import run_nandini

top = tkinter.Tk()

top.geometry("700x500")

micImage = PhotoImage(file='mic.png')  #importing pic to gui

B = tkinter.Button(top, image=micImage, command = run_nandini, borderwidth=0 )

B.pack(pady=30)
top.mainloop()