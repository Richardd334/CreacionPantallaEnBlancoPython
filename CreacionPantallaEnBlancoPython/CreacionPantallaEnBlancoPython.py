# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import tkinter as tk

aplicacion=tk.Tk()
aplicacion.title("siiii")
entry=tk.Entry(aplicacion).pack()

etiqueta=tk.Label(aplicacion, text="Hola mundo") 
etiqueta.pack()

boton=tk.Button(aplicacion, text="soy boton")
boton.pack()


aplicacion.mainloop()
