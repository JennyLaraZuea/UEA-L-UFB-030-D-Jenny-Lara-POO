import tkinter as tk
from tkinter import messagebox

# Función para añadir una nueva tarea
def add_task():
    add_button.config(text="Añadiendo...", bg="#FFD700")  # Amarillo
    entry.config(state=tk.NORMAL)
    entry.focus_set()
    entry.bind("<Return>", confirm_add_task)

def confirm_add_task(event=None):
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        listbox.selection_clear(0, tk.END)
        listbox.selection_set(tk.END)
        update_complete_button()
    else:
        messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía")
    entry.config(state=tk.DISABLED)
    add_button.config(text="Añadir", bg="#FF69B4")  # Rosa

# Función para marcar una tarea como completada
def complete_task():
    try:
        selected_index = listbox.curselection()[0]
        task_text = listbox.get(selected_index)
        if not task_text.startswith("✔ "):
            listbox.delete(selected_index)
            listbox.insert(selected_index, f"✔ {task_text}")
        update_complete_button()
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcarla como completada")

# Función para eliminar una tarea
def delete_task():
    selected_index = listbox.curselection()  # Verifica si hay una tarea seleccionada
    if selected_index:  # Si se ha seleccionado una tarea
        listbox.delete(selected_index[0])
        update_complete_button()
    else:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar")

# Función para cerrar la aplicación
def close_app():
    root.quit()

# Función para actualizar el botón completar según la tarea seleccionada
def update_complete_button(event=None):
    try:
        selected_index = listbox.curselection()[0]
        task_text = listbox.get(selected_index)
        if task_text.startswith("✔ "):
            complete_button.config(text="Tarea Completada", state=tk.DISABLED, bg="#9370DB")  # Morado
        else:
            complete_button.config(text="Completar", state=tk.NORMAL, bg="#00BFFF")  # Celeste
    except IndexError:
        complete_button.config(text="Completar", state=tk.NORMAL, bg="#00BFFF")

# Función para cambiar colores de los botones
def on_enter(event):
    event.widget.config(bg="#FF69B4")  # Rosa bajo

def on_leave(event):
    event.widget.config(bg="#FFD700")  # Amarillo bajo

def on_click(event):
    event.widget.config(bg="#8A2BE2")  # Fucsia
    root.after(200, lambda: event.widget.config(bg="#FFD700"))

# Crear la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas")
root.geometry("400x400")

# Crear un campo de entrada (deshabilitado hasta presionar "Añadir")
entry = tk.Entry(root, width=40, state=tk.DISABLED)
entry.pack(pady=10)

# Crear lista para mostrar tareas
listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=10)
listbox.bind("<<ListboxSelect>>", update_complete_button)

# Crear botones con efectos visuales
add_button = tk.Button(root, text="Añadir", command=add_task, bg="#FF69B4")
add_button.pack(pady=5)
add_button.bind("<Enter>", on_enter)
add_button.bind("<Leave>", on_leave)
add_button.bind("<Button-1>", on_click)

complete_button = tk.Button(root, text="Completar", command=complete_task, bg="#00BFFF")
complete_button.pack(pady=5)
complete_button.bind("<Enter>", on_enter)
complete_button.bind("<Leave>", on_leave)
complete_button.bind("<Button-1>", on_click)

delete_button = tk.Button(root, text="Eliminar", command=delete_task, bg="#FFD700")
delete_button.pack(pady=5)
delete_button.bind("<Enter>", on_enter)
delete_button.bind("<Leave>", on_leave)
delete_button.bind("<Button-1>", on_click)

# Asignar atajos de teclado solo si no estamos en el campo de entrada
def on_key(event):
    if entry.get() == "":  # Verifica si el campo de entrada está vacío o no está siendo usado
        if event.char == "c":
            complete_task()
        elif event.char == "d":
            delete_task()
        elif event.keysym == "Delete":
            delete_task()
        elif event.keysym == "Escape":
            close_app()

root.bind("<Key>", on_key)

# Iniciar la aplicación
root.mainloop()



