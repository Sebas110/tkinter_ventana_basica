#importar la libreria tkinter
from tkinter import *

#creacion de ventana
ventana= Tk()
ventana.geometry("200x200+550+100")
ventana.config(bg="black")
ventana.title("ventana")

#texto inicial
text_inicial= Label(ventana,text=("ingrese nombre"),bg="black",fg="white",font="arial 11")
text_inicial.place(x=50, y=10)


ventana.mainloop()