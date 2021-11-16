import tkinter as tk
ventana=tk.Tk()#declaracion del objeto
ventana.title("Venta de pruebas")#le asignamos un titulo a la ventana
ventana.geometry("400x400")#le configuramos las medidas deseadas
ventana.config(bg="black")# configuracion dl color de fonto
etiqueta=tk.Label(ventana,text="Hola mundo")#se lo agrego una etiqueta
etiqueta.pack()#con el.pack se mostro la etiqueta
ventana.mainloop()
