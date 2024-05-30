import string
import random
import sys
import os
import tkinter as tk
from tkinter import messagebox as MessageBox
from tkinter.filedialog import askdirectory as AskDirectory
from PIL import Image, ImageTk


caracteres = string.ascii_letters + string.digits + string.punctuation

def resource_path(relative_path):

    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def generador(longitud=8):

	clave = ""
	for i in range(longitud):
		clave += random.choice(caracteres)

	return clave

def mostrar_contraseña():

	contraseña_generada = generador()
	clave.set(contraseña_generada) # Actualiza la variable StringVar con la contraseña generada

def guardar_contraseña():

	result = MessageBox.askquestion("Guardar", "¿Quieres guardar la contraseña?")

	if result == "yes":
		carpeta_elegida = AskDirectory(title="Elige una carpeta para guardar la contraseña")
			
		if carpeta_elegida: # Guarda la contraseña en un archivo de texto
			fichero_destino = carpeta_elegida + "/contraseña.txt"
			
			with open(fichero_destino, "w") as file:
				contraseña = clave.get() # Usa la contraseña generada
				file.write(contraseña)

			global contraseña_guardada
			contraseña_guardada = True

def confirmar_salida():	

	if contraseña_guardada:
		root.destroy()
	
	else:
		result = MessageBox.askquestion("Salir", "¿Estás seguro de que quieres salir sin guardar la contraseña?")
		if result == "no":
			carpeta_elegida = AskDirectory(title="Elige una carpeta para guardar la contraseña")
			
			if carpeta_elegida: # Guarda la contraseña en un archivo de texto
				fichero_destino = carpeta_elegida + "/contraseña.txt"
			
				with open(fichero_destino, "w") as file:
					contraseña = clave.get() # Usa la contraseña generada
					file.write(contraseña)

		else:
			root.destroy()


root = tk.Tk()
root.title("Generador de contraseñas")
root.iconbitmap(resource_path("resources/generador_contraseñas.ico"))

app = tk.Frame(root).pack(padx=20, pady=10)

tk.Label(root, text="GENERADOR DE CONTRASEÑAS", font=("Arial", 20, "bold"), fg="grey", bg="lightgreen").pack()

tk.Label(app, text="").pack()

img = Image.open(resource_path("resources/generador_contraseñas.png"))
ancho, alto = 150, 175
# Image.LANCZOS: Suaviza los bordes de las imágenes y reduce la destorsión causado por la reducción de la imagen
img_resize = img.resize((ancho, alto), Image.LANCZOS)
img_tk = ImageTk.PhotoImage(img_resize)
tk.Label(root, image=img_tk).pack()

tk.Label(app, text="").pack()

clave = tk.StringVar()

tk.Button(app, text="Click aquí", command=mostrar_contraseña).pack()

tk.Entry(app, justify="center", textvariable=clave).pack()

tk.Label(app, text="").pack()

tk.Button(app, text="Guardar contraseña", command=guardar_contraseña).pack()

contraseña_guardada = False

root.protocol("WM_DELETE_WINDOW", confirmar_salida)

root.mainloop()