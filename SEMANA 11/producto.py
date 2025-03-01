# Definición de la clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """Inicializa un producto con ID, nombre, cantidad y precio."""
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, nueva_cantidad):
        """Actualiza la cantidad del producto."""
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        """Actualiza el precio del producto."""
        self.precio = nuevo_precio

    def __str__(self):
        """Representación en cadena del producto."""
        return f"{self.id_producto}: {self.nombre} - {self.cantidad} unidades - ${self.precio:.2f}"