import tkinter as tk
from tkinter import messagebox
import os

# Archivo donde se guardarán las tareas
TASKS_FILE = "tareas.txt"

# Crear la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("400x400")
root.configure(bg="#FFF5CC")  # Color amarillo bajito

# Marco para organizar los elementos
frame = tk.Frame(root, bg="#FFD1DC")  # Color rosado bajo
frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Campo de entrada para agregar tareas
task_entry = tk.Entry(frame, width=40, bg="#FFFACD", fg="black", font=("Arial", 12))
task_entry.pack(pady=10, padx=10)

# Lista de tareas
task_listbox = tk.Listbox(frame, width=50, height=10, bg="#FFE4E1", fg="black", font=("Arial", 12))
task_listbox.pack(pady=10, padx=10)

# Función para cargar tareas desde el archivo
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            tasks = file.readlines()
            for task in tasks:
                task_listbox.insert(tk.END, task.strip())

# Función para guardar tareas en el archivo
def save_tasks():
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        tasks = task_listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")

# Función para añadir una tarea
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Advertencia", "Debes escribir una tarea.")

# Función para marcar una tarea como completada
def mark_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(selected_task_index, f"✔ {task}")
        save_tasks()
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

# Función para eliminar una tarea
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

# Función para manejar la tecla Enter
def on_enter_pressed(event):
    add_task()

task_entry.bind("<Return>", on_enter_pressed)

# Marco para botones
button_frame = tk.Frame(root, bg="#FFF5CC")
button_frame.pack(pady=10)

# Botones con estilos
add_button = tk.Button(button_frame, text="Añadir Tarea", command=add_task, bg="#C1FFC1", font=("Arial", 10, "bold"))
add_button.pack(pady=5, padx=5, fill=tk.X)

complete_button = tk.Button(button_frame, text="Marcar como Completada", command=mark_completed, bg="#ADD8E6", font=("Arial", 10, "bold"))
complete_button.pack(pady=5, padx=5, fill=tk.X)

delete_button = tk.Button(button_frame, text="Eliminar Tarea", command=delete_task, bg="#FFB6C1", font=("Arial", 10, "bold"))
delete_button.pack(pady=5, padx=5, fill=tk.X)

# Cargar las tareas al iniciar el programa
load_tasks()

# Iniciar la aplicación
root.mainloop()

