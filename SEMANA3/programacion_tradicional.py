def ingresar_temperaturas():
    # Cargamos la lista de los días de la semana
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    # Creamos la lista para almacenar las temperaturas ingresadas
    temperaturas = []
    # Iteramos sobre cada día de la semana
    for dia in dias_semana:
        while True:
            try:
                # Solicitamos al usuario que ingrese la temperatura para el día actual
                temp = float(input(f"Ingrese la temperatura del {dia}: "))

                # Agregamos la temperatura a la lista
                temperaturas.append(temp)
                break
            except ValueError:
                # Mostramos un mensaje de error si el usuario ingresa un valor no válido
                print("Por favor, ingrese un número válido.")

    # Devolvemos la lista de temperaturas
    return temperaturas

def calcular_promedio(temperaturas):
    # Calculamos y devolvemos el promedio de las temperaturas
    return sum(temperaturas) / len(temperaturas)
