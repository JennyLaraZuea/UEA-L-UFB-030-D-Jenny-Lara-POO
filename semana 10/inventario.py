import json
import os

def cargar_datos():
    """Carga los datos del inventario desde un archivo JSON."""
    if os.path.exists("inventario.json"):
        with open("inventario.json", "r") as archivo:
            return json.load(archivo)
    return {}

def guardar_datos(inventario):
    """Guarda los datos del inventario en un archivo JSON."""
    with open("inventario.json", "w") as archivo:
        json.dump(inventario, archivo, indent=4)

def agregar_producto(inventario):
    """Agrega un producto nuevo al inventario."""
    codigo = input("Ingrese el código del producto: ")
    if codigo in inventario:
        print("El producto ya existe en el inventario.")
        return
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio = float(input("Ingrese el precio del producto: "))
    inventario[codigo] = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
    guardar_datos(inventario)
    print("Producto agregado correctamente.")

def mostrar_inventario(inventario):
    """Muestra los productos en el inventario."""
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("\nInventario Actual:")
        for codigo, datos in inventario.items():
            print(f"Código: {codigo}, Nombre: {datos['nombre']}, Cantidad: {datos['cantidad']}, Precio: ${datos['precio']}")

def modificar_producto(inventario):
    """Modifica los datos de un producto en el inventario."""
    codigo = input("Ingrese el código del producto a modificar: ")
    if codigo not in inventario:
        print("El producto no existe en el inventario.")
        return
    print("Datos actuales del producto:")
    print(inventario[codigo])
    nombre = input("Ingrese el nuevo nombre (o presione Enter para no cambiar): ") or inventario[codigo]["nombre"]
    cantidad = input("Ingrese la nueva cantidad (o presione Enter para no cambiar): ")
    cantidad = int(cantidad) if cantidad else inventario[codigo]["cantidad"]
    precio = input("Ingrese el nuevo precio (o presione Enter para no cambiar): ")
    precio = float(precio) if precio else inventario[codigo]["precio"]
    inventario[codigo] = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
    guardar_datos(inventario)
    print("Producto modificado correctamente.")

def eliminar_producto(inventario):
    """Elimina un producto del inventario."""
    codigo = input("Ingrese el código del producto a eliminar: ")
    if codigo in inventario:
        del inventario[codigo]
        guardar_datos(inventario)
        print("Producto eliminado correctamente.")
    else:
        print("El producto no existe en el inventario.")

def menu():
    """Muestra el menú de opciones y gestiona la interacción con el usuario."""
    inventario = cargar_datos()
    while True:
        print("\n--- MENÚ DE INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Modificar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            mostrar_inventario(inventario)
        elif opcion == "3":
            modificar_producto(inventario)
        elif opcion == "4":
            eliminar_producto(inventario)
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()