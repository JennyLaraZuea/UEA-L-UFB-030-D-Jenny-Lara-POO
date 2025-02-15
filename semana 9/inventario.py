# Definición de la clase Producto
# Esta clase representa un producto en el inventario con ID único, nombre, cantidad y precio.
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.
        :param id_producto: Identificador único del producto.
        :param nombre: Nombre del producto.
        :param cantidad: Cantidad disponible en stock.
        :param precio: Precio unitario del producto.
        """
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        """ Representación en cadena del objeto Producto. """
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


# Definición de la clase Inventario
# Esta clase maneja la gestión de productos en la tienda
class Inventario:
    def __init__(self):
        """
        Constructor de la clase Inventario.
        Inicializa un diccionario vacío para almacenar los productos por su ID único.
        """
        self.productos = {}

    def agregar_producto(self, producto):
        """
        Agrega un nuevo producto al inventario.
        :param producto: Objeto de la clase Producto.
        """
        if producto.id_producto in self.productos:
            print("Error: El ID del producto ya existe en el inventario.")
        else:
            self.productos[producto.id_producto] = producto
            print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto del inventario por su ID.
        :param id_producto: ID del producto a eliminar.
        """
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """
        Actualiza la cantidad o el precio de un producto en el inventario.
        :param id_producto: ID del producto a actualizar.
        :param cantidad: Nueva cantidad (opcional).
        :param precio: Nuevo precio (opcional).
        """
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
            print("Producto actualizado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        """
        Busca productos en el inventario por nombre (incluye coincidencias parciales).
        :param nombre: Nombre o parte del nombre del producto a buscar.
        """
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if encontrados:
            print("Productos encontrados:")
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        """
        Muestra todos los productos en el inventario.
        """
        if self.productos:
            print("Inventario actual:")
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")


# Definición de la interfaz de usuario en la consola
# Proporciona un menú interactivo para gestionar el inventario

def menu():
    inventario = Inventario()  # Se crea una instancia de la clase Inventario
    while True:
        print("\nMenú de Gestión de Inventario:")
        print("1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad disponible: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == '2':
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (presione Enter para omitir): ")
            precio = input("Ingrese el nuevo precio (presione Enter para omitir): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            inventario.mostrar_inventario()

        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


# Verifica si el script se ejecuta directamente
if __name__ == "__main__":
    menu()