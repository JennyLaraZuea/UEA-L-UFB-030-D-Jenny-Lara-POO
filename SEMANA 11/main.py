from inventario import Inventario
from producto import Producto

# Creación del inventario
inventario = Inventario()
inventario.cargar_desde_archivo()

# Menú interactivo
def menu():
    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Guardar y salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            if inventario.eliminar_producto(id_producto):
                print("Producto eliminado.")
            else:
                print("Producto no encontrado.")

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deje en blanco para no modificar): ")
            precio = input("Nuevo precio (deje en blanco para no modificar): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            if inventario.actualizar_producto(id_producto, cantidad, precio):
                print("Producto actualizado.")
            else:
                print("Producto no encontrado.")

        elif opcion == "4":
            nombre = input("Ingrese nombre del producto: ")
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos.")

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            inventario.guardar_en_archivo()
            print("Inventario guardado. Saliendo...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

# Ejecutar menú
menu()
