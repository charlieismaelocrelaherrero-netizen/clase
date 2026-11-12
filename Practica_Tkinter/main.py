
import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))


usuario_correcto = os.getenv("APP_USER")
password_correcto = os.getenv("APP_PASSWORD")


def capturar_credenciales():
    usuario = entrada_usuario.get().strip()
    password = entrada_password.get()

    validar_credenciales(usuario, password)


def validar_credenciales(usuario, password):

    if usuario_correcto is None or password_correcto is None:
        mostrar_mensaje("Error: revisa el archivo .env", "red")

    elif usuario == usuario_correcto and password == password_correcto:
        mostrar_mensaje("Acceso correcto", "green")

    else:
        mostrar_mensaje("Usuario o contraseña incorrectos", "red")


def mostrar_mensaje(texto, color):
    etiqueta_mensaje.config(text=texto, fg=color)


ventana = tk.Tk()
ventana.title("Inicio de sesión")
ventana.geometry("350x250")
ventana.resizable(False, False)

titulo = tk.Label(
    ventana,
    text="INICIO DE SESIÓN",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=15)

tk.Label(ventana, text="Usuario:").pack()

entrada_usuario = tk.Entry(ventana, width=30)
entrada_usuario.pack(pady=5)

tk.Label(ventana, text="Contraseña:").pack()

entrada_password = tk.Entry(ventana, width=30, show="*")
entrada_password.pack(pady=5)

boton = tk.Button(
    ventana,
    text="Iniciar sesión",
    command=capturar_credenciales
)
boton.pack(pady=10)

etiqueta_mensaje = tk.Label(
    ventana,
    text="",
    font=("Arial", 10, "bold")
)
etiqueta_mensaje.pack(pady=5)

ventana.mainloop()
