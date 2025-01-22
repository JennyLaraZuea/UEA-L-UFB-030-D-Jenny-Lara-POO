# Ejemplo de programa en Python con constructores y destructores
# Clase para gestionar archivos
class Archivo:
    def __init__(self, nombre):
        """
        Constructor de la clase Archivo.
        Inicializa el objeto y abre el archivo en modo escritura.
        """
        self.nombre = nombre
        self.archivo = open(nombre, 'w')  # Abre el archivo en modo escritura
        print(f"Archivo '{self.nombre}' creado y listo para escribir.")

    def escribir(self, contenido):
        """
        Método para escribir en el archivo.
        """
        self.archivo.write(contenido + '\n')  # Escribe contenido seguido de un salto de línea
        print(f"Contenido '{contenido}' escrito en '{self.nombre}'.")

    def __del__(self):
        """
        Destructor de la clase Archivo.
        Cierra el archivo cuando el objeto es eliminado.
        """
        if self.archivo:
            self.archivo.close()
            print(f"Archivo '{self.nombre}' cerrado correctamente.")

# Clase para gestionar dispositivos conectados
class Dispositivo:
    def __init__(self, nombre):
        """
        Constructor de la clase Dispositivo.
        Inicializa el dispositivo y establece la conexión simulada.
        """
        self.nombre = nombre
        self.conectado = True  # Indica que el dispositivo está conectado
        print(f"Dispositivo '{self.nombre}' conectado.")

    def usar_dispositivo(self):
        """
        Método para simular el uso del dispositivo.
        """
        if self.conectado:
            print(f"Usando el dispositivo '{self.nombre}'...")
        else:
            print(f"El dispositivo '{self.nombre}' no está disponible.")

    def __del__(self):
        """
        Destructor de la clase Dispositivo.
        Libera la conexión al dispositivo al eliminar el objeto.
        """
        if self.conectado:
            print(f"Dispositivo '{self.nombre}' desconectado.")
            self.conectado = False

# Función principal del programa
def main():
    # Crear y usar un archivo
    nombre_archivo = input("Introduce el nombre del archivo a crear: ")
    mi_archivo = Archivo(nombre_archivo)  # Se inicializa el archivo
    contenido = input("Escribe algo para guardar en el archivo: ")
    mi_archivo.escribir(contenido)  # Se escribe en el archivo

    # Crear y usar un dispositivo
    nombre_dispositivo = input("Introduce el nombre del dispositivo: ")
    mi_dispositivo = Dispositivo(nombre_dispositivo)  # Se inicializa el dispositivo
    mi_dispositivo.usar_dispositivo()  # Se simula el uso del dispositivo

    print("Finalizando el programa...")
    # Aquí, los destructores se activarán automáticamente al finalizar la función.

# Ejecutar el programa principal
if __name__ == "__main__":
    main()