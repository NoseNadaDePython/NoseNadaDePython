from tkinter import *
from tkinter import ttk
root=Tk()

e1 = StringVar()
root.title("que onda mundo")
root.resizable(13,13)
frame=Frame(root,width="480",height=320)
frame.pack()
frame.config(cursor="pirate",bg="blue",bd=30,relief="solid")
frame.grid(row=0,column=2000)
et=Label(root,text="prueva")
et.grid()

root.mainloop()