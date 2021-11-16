import tkinter as tk#Importanto librerias de tkinter

def abrir():#Evento lo que hace esta funcion es abrir otra ventana (ventana 2)
      window2 = tk.Toplevel(window)
      window2.config(bg="green")#configurando el volor de la ventana 2
      window2.geometry("150x100")   #ancho, alto
      window2.title("Ventana 2")#Agregando titulo 

window = tk.Tk()#Creando pantalla principal
window.config(bg="red")#Configurando color de ventana 1
window.geometry("200x150")#Establecienod dimensiones de la ventana
window.title("Ventana 1")#Agregando titulo 
button = tk.Button(window,background="green",foreground="pink",font="vernada",text="Abrir Ventana2",
 command=abrir)#Boton enlazado con la funcion
#que llamara a la ventana 2
button.grid(row=1, column=1)
print ("hola")
window.mainloop()#Ciclo 




