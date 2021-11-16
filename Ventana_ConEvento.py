import tkinter as tk

def abrir():
    window2=tk.Toplevel(window)
    window2.config(bg="green")
    window2.geometry("200x150")
    window2.title("Ventana 2")
    

window = tk.Tk()
window.config(bg="blue")
window.geometry("200x150")
window.title("ventana 1")
botton=tk.Button(window,text="Abrir ventana 2",command=abrir)
botton.grid(row=1,column=1)
window.mainloop()