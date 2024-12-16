# Creamos la clase
class ClimaSemanal:
    def __init__(self):
        # Inicializamos una lista
        self.temperaturas = [22.7,28,30,27.5,14.5,15.5,20]
        # Creamos la lista de los días de la semana
        self.dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

    def calcular_promedio(self):
        # Si la lista de temperaturas está vacía, retorna 0 para evitar división por cero
        if not self.temperaturas:
            return 0
        # Calculamos el promedio sumando las temperaturas y dividiendo por el número de temperaturas
        return sum(self.temperaturas) / len(self.temperaturas)

    def mostrar_promedio(self):
        # Calcula el promedio de las temperaturas
        promedio = self.calcular_promedio()
        # Muestra el promedio formateado con dos decimales
        print(f"El promedio semanal de las temperaturas es: {promedio:.2f}")

def main():
    # Creamos un objeto de instancia
    clima = ClimaSemanal()
    # Llamamos al metodo
    clima.mostrar_promedio()

# Este bloque asegura que el código dentro de él solo se ejecuta si el script se ejecuta directamente
if __name__ == "__main__":
    main()
