# Programa para calcular el área de un rectángulo con opciones de conversión.
# Funcionalidad:
# Este programa calcula el área de un rectángulo según las dimensiones ingresadas por el usuario.
# Permite convertir el área calculada a diferentes unidades: centímetros cuadrados, pies cuadrados e pulgadas cuadradas.
# Además, incluye validaciones para asegurar la entrada correcta de datos.

# Bienvenida al programa
print("¡Bienvenido al programa de cálculo de área!\n")
print("Este programa calcula el área de un rectángulo y te permite convertirla a otras unidades.\n")

# Función para solicitar un número válido al usuario
def solicitar_numero(mensaje):
    """
    Solicita al usuario un número positivo, repitiendo la solicitud hasta que sea válido.

    Args:
        mensaje (str): Mensaje que se muestra al usuario.

    Returns:
        float: Número válido ingresado por el usuario.
    """
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("Por favor, ingresa un valor mayor a 0.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Asegúrate de ingresar un número.")

# Solicitar las dimensiones del rectángulo al usuario
print("Por favor, ingresa las dimensiones del rectángulo:")
base = solicitar_numero("Ingresa la base del rectángulo en metros: ")  # Base (float)
altura = solicitar_numero("Ingresa la altura del rectángulo en metros: ")  # Altura (float)

# Calcular el área en metros cuadrados
area_metros = base * altura  # Área (float)

# Mostrar el área calculada
print("\nEl área del rectángulo es:")
print(f"- {area_metros:.2f} metros cuadrados.")

# Opciones adicionales de conversión
print("\nAhora vamos a convertir el área a otras unidades. Elige las opciones que prefieras.")

# Función para mostrar el menú de opciones
def mostrar_menu():
    """
    Muestra las opciones disponibles para convertir el área.
    """
    print("\nOpciones de conversión:")
    print("1. Convertir a centímetros cuadrados")
    print("2. Convertir a pies cuadrados")
    print("3. Convertir a pulgadas cuadradas")
    print("4. Todas las conversiones")
    print("5. Salir")

# Función para realizar conversiones
def realizar_conversion(opcion):
    """
    Realiza la conversión del área a la unidad seleccionada.

    Args:
        opcion (int): Opción seleccionada por el usuario.
    """
    if opcion == 1 or opcion == 4:
        area_centimetros = area_metros * 10000  # 1 metro cuadrado = 10,000 cm²
        print(f"- {area_centimetros:.2f} centímetros cuadrados.")
    if opcion == 2 or opcion == 4:
        area_pies = area_metros * 10.7639  # 1 metro cuadrado ≈ 10.7639 pies cuadrados
        print(f"- {area_pies:.2f} pies cuadrados.")
    if opcion == 3 or opcion == 4:
        area_pulgadas = area_metros * 1550.003  # 1 metro cuadrado ≈ 1550.003 pulgadas cuadradas
        print(f"- {area_pulgadas:.2f} pulgadas cuadradas.")

# Ciclo para que el usuario elija opciones
while True:
    mostrar_menu()
    try:
        opcion = int(input("\nElige una opción (1-5): "))  # Opción (integer)
        if opcion in [1, 2, 3, 4]:
            print("\nRealizando la conversión:")
            realizar_conversion(opcion)
        elif opcion == 5:
            print("\nGracias por usar el programa. ¡Hasta pronto!")
            break
        else:
            print("Por favor, ingresa una opción válida.")
    except ValueError:
        print("Entrada inválida. Asegúrate de ingresar un número del 1 al 5.")