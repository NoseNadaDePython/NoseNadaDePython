from tkinter import *#Importando librerias de Tkinter
#creando la raiz principal 

root = Tk()#Declarando objeto de tipo tk
menubar=Menu(root)#Declarando menubar de tipo menu indicando que root es su padre
root.config(menu=menubar)

#Añadiendo etiquetas al menu
menubar.add_cascade(label="Archivo")
menubar.add_cascade(label="Editar")
menubar.add_cascade(label="Ayuda")

#Creando el LoopFinal
root.mainloop()


