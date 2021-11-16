from tkinter import *#Importando librerias de Tkinter
#creando la raiz principal 

root = Tk()#Declarando objeto de tipo tk
menubar=Menu(root)#Declarando menubar de tipo menu indicando que root es su padre
root.config(menu=menubar)

#Generando los submenos de los menus principales
menu_archivo=Menu(menubar,tearoff=0)
menu_editar=Menu(menubar,tearoff=0)
menu_ayuda=Menu(menubar,tearoff=0)

#Menu´s principales
menubar.add_cascade(label="Archivo",menu=menu_archivo)#Añadiendo etiquetas al menu
menubar.add_cascade(label="Editar",menu=menu_editar)
menubar.add_cascade(label="Ayuda",menu=menu_ayuda)

#Creando el LoopFinal
root.mainloop()

