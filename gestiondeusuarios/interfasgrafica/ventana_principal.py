import tkinter as tk
from tkinter import messagebox

# Diccionario para almacenar usuarios
usuarios = {}


# Función para guardar usuario
def guardar_usuario():
    nombre = entry_nombre.get()
    correo = entry_correo.get()
    contrasena = entry_contrasena.get()

    if nombre and correo and contrasena:
        usuarios[nombre] = {"Correo": correo, "Contraseña": contrasena}
        messagebox.showinfo("Éxito", "Usuario guardado correctamente.")
        entry_nombre.delete(0, tk.END)
        entry_correo.delete(0, tk.END)
        entry_contrasena.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Todos los campos son obligatorios.")


# Función para mostrar usuarios guardados en otra ventana
def visualizar_usuarios():
    ventana_visualizar = tk.Toplevel(ventana)
    ventana_visualizar.title("Usuarios Guardados")
    ventana_visualizar.geometry("400x300")
    ventana_visualizar.configure(bg="lightgray")

    tk.Label(ventana_visualizar, text="Lista de Usuarios", font=("Arial", 14, "bold"), bg="lightgray").pack(pady=10)

    if usuarios:
        for nombre, datos in usuarios.items():
            tk.Label(ventana_visualizar, text=f"Nombre: {nombre}, Correo: {datos['Correo']}", bg="lightgray").pack()
    else:
        tk.Label(ventana_visualizar, text="No hay usuarios registrados.", bg="lightgray").pack()


# Función para mostrar mensaje de bienvenida
def mostrar_bienvenida():
    messagebox.showinfo("Bienvenido", "¡Bienvenido al sistema de gestión de usuarios!")


# Función para cerrar sesión
def cerrar_sesion():
    confirmacion = messagebox.askyesno("Cerrar sesión", "¿Seguro que quieres cerrar sesión?")
    if confirmacion:
        ventana.destroy()


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Gestión de Usuarios")
ventana.geometry('500x450')
ventana.configure(bg='#f0f0f0')

# Frame para organizar elementos
frame_principal = tk.Frame(ventana, bg='lightblue', padx=20, pady=20)
frame_principal.pack(pady=20)

tk.Label(frame_principal, text="Gestión de Usuarios", font=("Arial", 16, "bold"), bg='lightblue').pack(pady=10)

# Entradas para usuario
tk.Label(frame_principal, text="Nombre:", bg='lightblue').pack()
entry_nombre = tk.Entry(frame_principal, width=30)
entry_nombre.pack(pady=5)

tk.Label(frame_principal, text="Correo Electrónico:", bg='lightblue').pack()
entry_correo = tk.Entry(frame_principal, width=30)
entry_correo.pack(pady=5)

tk.Label(frame_principal, text="Contraseña:", bg='lightblue').pack()
entry_contrasena = tk.Entry(frame_principal, width=30, show="*")
entry_contrasena.pack(pady=5)

# Botones
btn_guardar = tk.Button(frame_principal, text="Guardar Usuario", command=guardar_usuario, width=25, bg="#008CBA",
                        fg="white")
btn_guardar.pack(pady=5)

btn_visualizar = tk.Button(frame_principal, text="Visualizar Usuarios", command=visualizar_usuarios, width=25,
                           bg="#f39c12", fg="white")
btn_visualizar.pack(pady=5)

btn_bienvenida = tk.Button(frame_principal, text="Mostrar Bienvenida", command=mostrar_bienvenida, width=25,
                           bg="#4CAF50", fg="white")
btn_bienvenida.pack(pady=5)

btn_salir = tk.Button(frame_principal, text="Cerrar Sesión", command=cerrar_sesion, width=25, bg="red", fg="white")
btn_salir.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()