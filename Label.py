from  tkinter import *#importar librerias de tkinter
#configuracion de la ventana raiz
root = Tk ()

label=Label(root,text="No se programar :(")#etiqueta
label.pack()
label.config(bg="yellow",foreground="black",font=("arial black",20))
#configurando propiedades de la etiqueta 1, color, fuente y color de fuente
Label(root,text="En Python").pack(anchor="sw")#etiqueta 2

Label(root,text="Sorry").pack(anchor="ne")#etiqueta 3

root.mainloop()#bucle final