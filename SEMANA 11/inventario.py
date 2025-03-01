import json
from producto import Producto

# Definición de la clase Inventario
class Inventario:
    def __init__(self):
        """Inicializa un inventario como un diccionario vacío."""
        self.productos = {}

    def agregar_producto(self, producto):
        """Añade un nuevo producto al inventario."""
        self.productos[producto.id_producto] = producto

    def eliminar_producto(self, id_producto):
        """Elimina un producto por su ID."""
        if id_producto in self.productos:
            del self.productos[id_producto]
            return True
        return False

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Actualiza la cantidad o precio de un producto."""
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].actualizar_precio(precio)
            return True
        return False

    def buscar_producto(self, nombre):
        """Busca productos por nombre y devuelve una lista de coincidencias."""
        return [prod for prod in self.productos.values() if nombre.lower() in prod.nombre.lower()]

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        for producto in self.productos.values():
            print(producto)

    def guardar_en_archivo(self, archivo="inventario.json"):
        """Guarda el inventario en un archivo JSON."""
        with open(archivo, "w") as f:
            json.dump({k: vars(v) for k, v in self.productos.items()}, f, indent=4)

    def cargar_desde_archivo(self, archivo="inventario.json"):
        """Carga el inventario desde un archivo JSON."""
        try:
            with open(archivo, "r") as f:
                datos = json.load(f)
                self.productos = {k: Producto(**v) for k, v in datos.items()}
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Iniciando nuevo inventario.")