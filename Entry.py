from tkinter import *
import tkinter#importando librerias
#creando ventana raiz
root=Tk()


label = Label(root, text="Nombre")
label.grid(row=0, column=0, sticky="e", padx=8)

entry = Entry(root)
entry.grid(row=0, column=1, padx=8, pady=5)
entry.config(justify="center")

labe2 = Label(root, text="Apellidos")
labe2.grid(row=1, column=0, sticky="e", padx=8)

entry2 = Entry(root)
entry2.grid(row=1, column=1, padx=8)
entry2.config(justify="center")




#creando ciclo principal
root.mainloop()