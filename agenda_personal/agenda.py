import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import re


class AgendaPersonal:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("700x500")
        self.root.configure(bg="#FFFACD")  # Fondo amarillo claro

        # Marco principal
        main_frame = tk.Frame(self.root, bg="#FFFACD")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Sección de Entrada de Datos
        entrada_frame = tk.LabelFrame(main_frame, text="Nuevo Evento", bg="#FFFACD", font=("Arial", 10, "bold"))
        entrada_frame.pack(fill=tk.X, padx=5, pady=5)

        tk.Label(entrada_frame, text="Fecha:", bg="#FFFACD", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=5)
        self.fecha = DateEntry(entrada_frame, width=12, background="darkblue", foreground="white", borderwidth=2)
        self.fecha.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(entrada_frame, text="Hora (HH:MM):", bg="#FFFACD", font=("Arial", 10)).grid(row=0, column=2, padx=5, pady=5)
        self.hora = tk.Entry(entrada_frame, width=10)
        self.hora.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(entrada_frame, text="Descripción:", bg="#FFFACD", font=("Arial", 10)).grid(row=1, column=0, padx=5, pady=5)
        self.descripcion = tk.Entry(entrada_frame, width=50)
        self.descripcion.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        # Botones de Acción
        botones_frame = tk.Frame(main_frame, bg="#FFFACD")
        botones_frame.pack(fill=tk.X, padx=5, pady=5)

        tk.Button(botones_frame, text="Agregar Evento", command=self.agregar_evento, bg="#FFD700", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        tk.Button(botones_frame, text="Eliminar Evento", command=self.eliminar_evento, bg="#FF6347", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        tk.Button(botones_frame, text="Salir", command=self.root.quit, bg="#B22222", fg="white", font=("Arial", 10)).pack(side=tk.RIGHT, padx=5)

        # Sección de Visualización de Eventos (TreeView)
        tree_frame = tk.Frame(main_frame)
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.tree = ttk.Treeview(tree_frame, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")

        for col in ("Fecha", "Hora", "Descripción"):
            self.tree.column(col, width=200, anchor="center", stretch=False)

        self.tree.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.tree.configure(yscrollcommand=scrollbar.set)

        tree_frame.columnconfigure(0, weight=1)
        tree_frame.rowconfigure(0, weight=1)

    def agregar_evento(self):
        fecha = self.fecha.get().strip()
        hora = self.hora.get().strip()
        descripcion = self.descripcion.get().strip()

        # Validar campos vacíos
        if not (fecha and hora and descripcion):
            messagebox.showwarning("Advertencia", "Todos los campos deben estar completos.")
            return

        # Validar formato de hora
        if not re.match(r"^(?:[01]\d|2[0-3]):[0-5]\d$", hora):
            messagebox.showerror("Error", "Formato de hora inválido. Debe ser HH:MM (24h).")
            return

        # Insertar en TreeView
        self.tree.insert("", "end", values=(fecha, hora, descripcion))
        self.limpiar_campos()

    def eliminar_evento(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "No se ha seleccionado ningún evento.")
            return

        if messagebox.askyesno("Confirmar", "¿Desea eliminar el evento seleccionado?"):
            for item in seleccion:
                self.tree.delete(item)

    def limpiar_campos(self):
        """Limpia los campos de entrada después de agregar un evento."""
        self.hora.delete(0, tk.END)
        self.descripcion.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()
