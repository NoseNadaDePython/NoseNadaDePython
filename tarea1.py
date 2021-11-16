from tkinter import *
import mariabd 

root=Tk()
root.title("Ventana principal")
root.resizable(0,0)

try:
    conexion =mariabd.connect(
        user="root",
        password="",
host
    )