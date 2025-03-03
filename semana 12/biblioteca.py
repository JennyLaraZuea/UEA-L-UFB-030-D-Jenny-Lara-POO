class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Categoría: {self.categoria}, ISBN: {self.isbn}"

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros prestados: {len(self.libros_prestados)}"

class Biblioteca:
    def __init__(self):
        self.libros = {}  # Clave: ISBN, Valor: Objeto Libro
        self.usuarios = {}  # Clave: ID usuario, Valor: Objeto Usuario

    def agregar_libro(self):
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        categoria = input("Ingrese la categoría del libro: ")
        isbn = input("Ingrese el ISBN del libro: ")

        if isbn not in self.libros:
            nuevo_libro = Libro(titulo, autor, categoria, isbn)
            self.libros[isbn] = nuevo_libro
            print(f"Libro agregado: {nuevo_libro}")
        else:
            print("El libro ya está en la biblioteca.")

    def ver_libros(self):
        if self.libros:
            print("\nLibros disponibles:")
            for libro in self.libros.values():
                print(libro)
        else:
            print("No hay libros en la biblioteca.")

    def registrar_usuario(self):
        nombre = input("Ingrese el nombre del usuario: ")
        id_usuario = input("Ingrese el ID del usuario: ")

        if id_usuario not in self.usuarios:
            nuevo_usuario = Usuario(nombre, id_usuario)
            self.usuarios[id_usuario] = nuevo_usuario
            print(f"Usuario registrado: {nuevo_usuario}")
        else:
            print("El usuario ya está registrado.")

    def prestar_libro(self):
        id_usuario = input("Ingrese el ID del usuario: ")
        isbn = input("Ingrese el ISBN del libro a prestar: ")

        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros.pop(isbn)
            usuario.libros_prestados.append(libro)
            print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
        else:
            print("Usuario no registrado o libro no disponible.")

    def devolver_libro(self):
        id_usuario = input("Ingrese el ID del usuario: ")
        isbn = input("Ingrese el ISBN del libro a devolver: ")

        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros[isbn] = libro
                    print(f"Libro '{libro.titulo}' devuelto a la biblioteca.")
                    return
        print("Libro no encontrado en los préstamos del usuario.")

    def buscar_libro(self):
        criterio = input("Buscar por (titulo, autor, categoria): ").lower()
        valor = input("Ingrese el valor a buscar: ").lower()

        resultados = [libro for libro in self.libros.values() if valor in getattr(libro, criterio).lower()]
        if resultados:
            print("\nLibros encontrados:")
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros con ese criterio.")

# Menú interactivo
def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n--- SISTEMA DE BIBLIOTECA ---")
        print("1. Agregar libro")
        print("2. Ver libros disponibles")
        print("3. Registrar usuario")
        print("4. Prestar libro")
        print("5. Devolver libro")
        print("6. Buscar libro")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            biblioteca.agregar_libro()
        elif opcion == "2":
            biblioteca.ver_libros()
        elif opcion == "3":
            biblioteca.registrar_usuario()
        elif opcion == "4":
            biblioteca.prestar_libro()
        elif opcion == "5":
            biblioteca.devolver_libro()
        elif opcion == "6":
            biblioteca.buscar_libro()
        elif opcion == "7":
            print("¡Hasta luego gracias por su visita !")
            break
        else:
            print("Opción no válida, intente de nuevo.")

# Ejecutar el menú
menu()

