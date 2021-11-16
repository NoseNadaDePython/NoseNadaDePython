from tkinter import *#importando librerias tkinter

root = Tk ()#creando la raiz

Imagen = PhotoImage(file="rana1.gif")
Label(root,image=Imagen, bd=10).pack()

#loop final 
root.mainloop()

