# Clase base: Vehiculo
class Vehiculo:
    # Atributo privado (encapsulado)
    def __init__(self, marca, modelo, color):
        self.__marca = marca  # Atributo privado, no se debe acceder directamente
        self.modelo = modelo
        self.color = color

    # Método para mostrar información del vehículo
    def mostrar_info(self):
        # Usamos el método obtener_marca() para acceder a la marca privada
        print(f"Marca: {self.obtener_marca()}, Modelo: {self.modelo}, Color: {self.color}")

    # Método para obtener la marca (encapsulamiento)
    def obtener_marca(self):
        return self.__marca

    # Método para cambiar la marca (encapsulamiento)
    def cambiar_marca(self, nueva_marca):
        self.__marca = nueva_marca


# Clase derivada: Automovil (herencia)
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, color, tipo_motor):
        super().__init__(marca, modelo, color)  # Llamamos al constructor de la clase base
        self.tipo_motor = tipo_motor

    # Método sobrescrito (polimorfismo)
    def mostrar_info(self):
        # Llamamos al método de la clase base y agregamos información adicional
        super().mostrar_info()
        print(f"Tipo de motor: {self.tipo_motor}")


# Clase derivada: Moto (herencia)
class Moto(Vehiculo):
    def __init__(self, marca, modelo, color, cilindrada):
        super().__init__(marca, modelo, color)
        self.cilindrada = cilindrada

    # Método sobrescrito (polimorfismo)
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Cilindrada: {self.cilindrada}")


# Función para crear un vehículo de tipo Automóvil o Moto
def crear_vehiculo():
    print("\nOpciones de vehículos disponibles:")
    print("1. Automóvil")
    print("2. Moto")

    # Solicitar la elección del tipo de vehículo
    tipo = input("\n¿Escoge un tipo de vehículo por el número (1 para Automóvil, 2 para Moto): ")

    # Opciones de marcas predefinidas
    marcas_disponibles = ["Toyota", "Honda", "Ford", "Chevrolet", "BMW", "Yamaha", "Harley-Davidson"]

    print("\nOpciones de marcas disponibles:")
    for i, marca in enumerate(marcas_disponibles, 1):
        print(f"{i}. {marca}")

    marca_elegida = int(input("\nElige una marca por el número: ")) - 1
    marca = marcas_disponibles[marca_elegida] if 0 <= marca_elegida < len(marcas_disponibles) else "Marca no válida"

    # Opciones de modelos por marca
    modelos_por_marca = {
        "Toyota": ["Corolla", "Camry", "Hilux", "Rav4"],
        "Honda": ["Civic", "Accord", "CR-V", "HR-V"],
        "Ford": ["Focus", "Fiesta", "Mustang", "Explorer"],
        "Chevrolet": ["Malibu", "Cruze", "Tahoe", "Silverado"],
        "BMW": ["X5", "M3", "3 Series", "5 Series"],
        "Yamaha": ["YZF-R3", "MT-09", "FZ-07"],
        "Harley-Davidson": ["Street 750", "Iron 883", "Fat Boy"]
    }

    print("\nOpciones de modelos disponibles:")
    if marca in modelos_por_marca:
        for i, modelo in enumerate(modelos_por_marca[marca], 1):
            print(f"{i}. {modelo}")
    else:
        print("No hay modelos disponibles para esta marca.")
        return None

    modelo_elegido = int(input("\nElige un modelo por el número: ")) - 1
    modelo = modelos_por_marca[marca][modelo_elegido] if 0 <= modelo_elegido < len(
        modelos_por_marca[marca]) else "Modelo no válido"

    color = input("Introduce el color: ")

    # Crear vehículo según la selección
    if tipo == "1":  # Opción para automóvil
        tipo_motor = input("Introduce el tipo de motor (Gasolina/Eléctrico/otro): ")
        return Automovil(marca, modelo, color, tipo_motor)
    elif tipo == "2":  # Opción para moto
        cilindrada = input("Introduce la cilindrada (por ejemplo: 250cc, 500cc): ")
        return Moto(marca, modelo, color, cilindrada)
    else:
        print("Opción no válida, se creará un vehículo vacío.")
        return None


# Crear vehículo basado en los datos del usuario
vehiculo = crear_vehiculo()

# Verificar si el vehículo fue creado correctamente
if vehiculo:
    # Llamada al método para mostrar información del vehículo
    print("\nInformación del vehículo creado:")
    vehiculo.mostrar_info()

    # Modificación de atributo usando el método encapsulado
    nueva_marca = input("\nIntroduce la nueva marca para el vehículo: ")
    vehiculo.cambiar_marca(nueva_marca)
    print("\nMarca modificada del vehículo:")
    vehiculo.mostrar_info()
else:
    print("No se pudo crear el vehículo debido a una selección incorrecta.")
1