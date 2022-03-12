import tkinter
from tkinter import messagebox as mbox
from tkinter import *
from Alexa import run_nandini

top = tkinter.Tk()

top.geometry("700x300")
click_btn= PhotoImage(file='mic.png')
B = tkinter.Button(top, image=click_btn, command = run_nandini, borderwidth=0)

B.pack(pady=30)
top.mainloop()