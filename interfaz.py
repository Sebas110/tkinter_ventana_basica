#importar las librerias 
from tkinter import *
from openpyxl import * 
#creacion de ventana
ventana= Tk()
ventana.geometry("200x100+550+100")
ventana.config(bg="black")
ventana.title("ventana")

#texto inicial
text_inicial= Label(ventana,text=("ingrese nombre"),bg="black",fg="white",font="arial 11")
text_inicial.place(x=50, y=10)

#agregamos cuadro de entrada
entrada_text= Entry(ventana,font="arial 9")
entrada_text.place(x=33,y= 35)

#agregamos boton
boton1= Button(text="OK")
boton1.place(x=90,y=60)
ventana.mainloop()