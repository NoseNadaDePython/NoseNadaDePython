from tkinter import * #Importanto librerias de Tkinter
#configuracion de la ventana raiz
root = Tk()#Declarmos la raiz
#StringVar son variables dinamicas que se crean despues de la raiz

texto= StringVar () # Declara variable de tipo cadena
texto.set("Un nuevo texto por StringVar")

label = Label(root, text="Otra Etiqueta")#Etiqueta 1
label.config(bg="green",fg="blue",font=("cooper black",20))
label.config(textvariable=texto)
label.pack()
root.mainloop()# Comenzamos el bucle de aplicación