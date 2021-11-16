from tkinter import *#importando librerias 

#evento sumar
def sumar ():
  r.set(float(n1.get()) +float(n2.get()))
  borrar()

def borrar():
    n1.set("")
    n2.set("")

def restar():
     r.set(float(n1.get()) -float(n2.get()))
     borrar()

def multiplicacion():
     r.set(float(n1.get())*float(n2.get()))
     borrar()



root = Tk()#creando la raiz
root.title("Casio 3000")

#Declarando variabless
n1=StringVar()
n2=StringVar()
r=StringVar()


Label(root,text="Numero 1").pack()
Entry(root,justify="center",textvariable=n1).pack()

  
Label(root,text="Numero 2").pack()
Entry(root,justify="center",textvariable=n2).pack()

Label(root,text="\nResultado",foreground="red",font=("arial black",10)).pack()
Entry(root,justify="center",textvariable=r,state="disabled",relief="raised").pack()

Button(root,text="sumar",command=sumar,bd="3").pack(side="left")

Button(root,text="restar",command=restar,bd="3").pack(side="left")
Button(root,text="multiplicar",command=multiplicacion,bd="3").pack(side="right")

root.mainloop()#ciclo inicial