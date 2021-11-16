from tkinter import *#Importando librerias de Tkinter
#creando la raiz principal 

root = Tk()#Declarando objeto de tipo tk
menubar=Menu(root)#Declarando menubar de tipo menu indicando que root es su padre
root.config(menu=menubar)

#Generando los menu de la ventna 
###############################################
menu_archivo=Menu(menubar,tearoff=0)
#Generando submeno archivo
menu_archivo.add_command(label="Nuevo")
menu_archivo.add_command(label="Abrir")
menu_archivo.add_command(label="Guardar")
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir",command=root.quit)#Agregando la acion quit (cerrar)

#Generando menus editar con submenus
menu_editar=Menu(menubar,tearoff=0)
menu_editar.add_command(label="Copiar",font=("calibri",10))
menu_editar.add_command(label="Cortar")
menu_editar.add_command(label="Pegar")


menu_ayuda=Menu(menubar,tearoff=0)
menu_ayuda.add_command(label="Acerca de")
menu_ayuda.add_separator()
menu_ayuda.add_command(label="Soporte")

#Menu´s principales
menubar.add_cascade(label="Archivo",menu=menu_archivo)#Añadiendo etiquetas al menu
menubar.add_cascade(label="Editar",menu=menu_editar)
menubar.add_cascade(label="Ayuda",menu=menu_ayuda)
print("hola")
#Creando el LoopFinal
root.mainloop()
