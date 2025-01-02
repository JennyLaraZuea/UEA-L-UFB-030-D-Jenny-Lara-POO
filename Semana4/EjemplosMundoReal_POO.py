
# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, precio, stock):
        # Atributos básicos del producto
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def actualizar_stock(self, cantidad):
        # Resta stock cuando se compra algo
        if cantidad > self.stock:
            raise ValueError("No hay suficiente stock disponible.")
        self.stock -= cantidad

    def __str__(self):
        # Para mostrar el producto como texto
        return f"{self.id_producto} - {self.nombre} - ${self.precio:.2f} - Stock: {self.stock}"


# Clase Carrito
class Carrito:
    def __init__(self):
        # El carrito tiene una lista de productos y cantidades
        self.productos = []
        self.cantidades = {}

    def agregar_producto(self, producto, cantidad):
        # Agrega un producto al carrito
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero.")
        if cantidad > producto.stock:
            raise ValueError("No hay suficiente stock para agregar al carrito.")

        producto.actualizar_stock(cantidad)

        if producto in self.productos:
            self.cantidades[producto.id_producto] += cantidad
        else:
            self.productos.append(producto)
            self.cantidades[producto.id_producto] = cantidad

    def calcular_total(self):
        # Calcula el precio total de los productos en el carrito
        total = 0
        for producto in self.productos:
            total += producto.precio * self.cantidades[producto.id_producto]
        return total

    def mostrar_carrito(self):
        # Muestra el contenido del carrito
        if not self.productos:
            print("El carrito está vacío.")
        else:
            print("Carrito de compras:")
            for producto in self.productos:
                cantidad = self.cantidades[producto.id_producto]
                print(f"{producto.nombre} - Cantidad: {cantidad} - Subtotal: ${producto.precio * cantidad:.2f}")
            print(f"Total a pagar: ${self.calcular_total():.2f}")


# Clase Tienda
class Tienda:
    def __init__(self, nombre):
        # Atributos de la tienda
        self.nombre = nombre
        self.inventario = []

    def agregar_producto(self, producto):
        # Agrega un producto al inventario
        self.inventario.append(producto)

    def mostrar_inventario(self):
        # Muestra los productos disponibles en la tienda
        print(f"Inventario de {self.nombre}:")
        for producto in self.inventario:
            print(producto)


# --- Uso del programa ---
if __name__ == "__main__":
    # Crear la tienda y productos
    tienda = Tienda("Tienda Python")
    tienda.agregar_producto(Producto(1, "Laptop", 1500.0, 5))
    tienda.agregar_producto(Producto(2, "Teléfono", 800.0, 10))
    tienda.agregar_producto(Producto(3, "Tablet", 400.0, 7))

    # Mostrar inventario
    print("\nInventario inicial:")
    tienda.mostrar_inventario()

    # Crear el carrito
    carrito = Carrito()

    # Agregar productos al carrito
    print("\nAgregando productos al carrito...")
    try:
        carrito.agregar_producto(tienda.inventario[0], 2)  # Agregar 2 laptops
        carrito.agregar_producto(tienda.inventario[1], 1)  # Agregar 1 teléfono
    except ValueError as e:
        print(f"Error: {e}")

    # Mostrar el carrito
    print("\nCarrito actual:")
    carrito.mostrar_carrito()

    # Mostrar inventario después de agregar al carrito
    print("\nInventario después de la compra:")
    tienda.mostrar_inventario()
