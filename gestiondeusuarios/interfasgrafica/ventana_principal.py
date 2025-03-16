import tkinter as tk
from tkinter import messagebox

# Diccionario para almacenar usuarios
usuarios = {}


# Función para agregar usuario
def agregar_usuario():
    # Obtener datos ingresados por el usuario
    nombre = entry_nombre.get()
    correo = entry_correo.get()
    contrasena = entry_contrasena.get()

    # Verificar que todos los campos estén llenos
    if nombre and correo and contrasena:
        usuarios[nombre] = {"Correo": correo, "Contraseña": contrasena}  # Guardar usuario en el diccionario
        actualizar_lista()  # Actualizar la lista visual
        entry_nombre.delete(0, tk.END)  # Limpiar campos
        entry_correo.delete(0, tk.END)
        entry_contrasena.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Todos los campos son obligatorios.")  # Mostrar alerta


# Función para actualizar la lista de usuarios
def actualizar_lista():
    lista_usuarios.delete(0, tk.END)  # Limpiar lista antes de actualizarla
    for nombre, datos in usuarios.items():
        lista_usuarios.insert(tk.END, f"{nombre} - {datos['Correo']}")  # Agregar usuarios a la lista


# Función para limpiar la lista de usuarios
def limpiar_lista():
    lista_usuarios.delete(0, tk.END)  # Borrar todos los elementos de la lista
    usuarios.clear()  # Vaciar el diccionario
    messagebox.showinfo("Éxito", "Lista de usuarios limpiada correctamente.")  # Mostrar mensaje de éxito


# Función para visualizar usuarios en una nueva ventana
def visualizar_usuarios():
    ventana_visualizar = tk.Toplevel(ventana)  # Crear nueva ventana
    ventana_visualizar.title("Usuarios Registrados")
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


# Función para cerrar la aplicación
def cerrar_sesion():
    confirmacion = messagebox.askyesno("Cerrar sesión", "¿Seguro que quieres cerrar sesión?")  # Confirmar acción
    if confirmacion:
        ventana.destroy()  # Cerrar ventana principal


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Usuarios")  # Título de la ventana
ventana.geometry('500x500')  # Tamaño de la ventana
ventana.configure(bg='#f0f0f0')  # Color de fondo

# Etiqueta principal
tk.Label(ventana, text="Gestión de Usuarios", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

# Lista de usuarios
tk.Label(ventana, text="Usuarios Registrados", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=5)
lista_usuarios = tk.Listbox(ventana, width=50, height=10)  # Crear lista para mostrar usuarios
lista_usuarios.pack(pady=10)

# Botones principales
btn_registro = tk.Button(ventana, text="Registrar Usuario", command=mostrar_bienvenida, bg="#4CAF50",
                         fg="white")  # Botón para registrar usuario
btn_registro.pack(pady=5)

btn_visualizar = tk.Button(ventana, text="Visualizar Usuarios", command=visualizar_usuarios, bg="#f39c12",
                           fg="white")  # Botón para ver usuarios
btn_visualizar.pack(pady=5)

btn_limpiar = tk.Button(ventana, text="Limpiar Lista", command=limpiar_lista, bg="red",
                        fg="white")  # Botón para limpiar lista
btn_limpiar.pack(pady=5)

btn_salir = tk.Button(ventana, text="Cerrar Sesión", command=cerrar_sesion, bg="red",
                      fg="white")  # Botón para cerrar sesión
btn_salir.pack(pady=10)


# Ventana de registro
def abrir_ventana_registro():
    ventana_registro = tk.Toplevel(ventana)  # Crear ventana secundaria
    ventana_registro.title("Registro de Usuario")
    ventana_registro.geometry("300x300")
    ventana_registro.configure(bg="lightblue")

    tk.Label(ventana_registro, text="Nombre:", bg="lightblue").pack(pady=5)
    global entry_nombre
    entry_nombre = tk.Entry(ventana_registro, width=30)  # Campo de entrada para el nombre
    entry_nombre.pack(pady=5)

    tk.Label(ventana_registro, text="Correo:", bg="lightblue").pack(pady=5)
    global entry_correo
    entry_correo = tk.Entry(ventana_registro, width=30)  # Campo de entrada para el correo
    entry_correo.pack(pady=5)

    tk.Label(ventana_registro, text="Contraseña:", bg="lightblue").pack(pady=5)
    global entry_contrasena
    entry_contrasena = tk.Entry(ventana_registro, width=30, show="*")  # Campo de entrada para la contraseña
    entry_contrasena.pack(pady=5)

    btn_guardar = tk.Button(ventana_registro, text="Agregar", command=agregar_usuario, bg="#008CBA",
                            fg="white")  # Botón para agregar usuario
    btn_guardar.pack(pady=10)


btn_registro.config(command=abrir_ventana_registro)  # Asignar la función al botón de registro

# Ejecutar la ventana principal
ventana.mainloop()