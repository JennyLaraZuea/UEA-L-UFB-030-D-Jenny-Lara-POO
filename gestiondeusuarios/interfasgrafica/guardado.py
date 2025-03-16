import tkinter as tk
from tkinter import messagebox

def guardar_datos():
    nombre = entrada_nombre.get()
    correo = entrada_correo.get()
    contraseña = entrada_contraseña.get()

    if nombre and correo and contraseña:
        with open("usuarios.txt", "a") as file:
            file.write(f"{nombre},{correo},{contraseña}\n")
        messagebox.showinfo("Éxito", "Datos guardados correctamente.")
        entrada_nombre.delete(0, tk.END)
        entrada_correo.delete(0, tk.END)
        entrada_contraseña.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")

def mostrar_ventana_guardado():
    ventana_guardado = tk.Toplevel()
    ventana_guardado.title("Ingresar Usuario")
    ventana_guardado.geometry('400x300')
    ventana_guardado.configure(bg='lightblue')

    tk.Label(ventana_guardado, text="Nombre de usuario:", bg='lightblue').pack(pady=5)
    global entrada_nombre
    entrada_nombre = tk.Entry(ventana_guardado, width=30)
    entrada_nombre.pack(pady=5)

    tk.Label(ventana_guardado, text="Correo electrónico:", bg='lightblue').pack(pady=5)
    global entrada_correo
    entrada_correo = tk.Entry(ventana_guardado, width=30)
    entrada_correo.pack(pady=5)

    tk.Label(ventana_guardado, text="Contraseña:", bg='lightblue').pack(pady=5)
    global entrada_contraseña
    entrada_contraseña = tk.Entry(ventana_guardado, width=30, show="*")
    entrada_contraseña.pack(pady=5)

    tk.Button(ventana_guardado, text="Guardar", command=guardar_datos).pack(pady=10)