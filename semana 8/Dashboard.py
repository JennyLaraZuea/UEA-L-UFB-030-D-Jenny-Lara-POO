import os
import subprocess

def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix-based systems
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")

def mostrar_menu():
    rutas_semanas = {
        '2': "C:/Users/Win-10/fp/fudamento de programacion/UEA-L-UFB-030-D-Jenny-Lara-POO/SEMANA 2/Técnicas de programacion",
        '3': "C:/Users/Win-10/fp/fudamento de programacion/UEA-L-UFB-030-D-Jenny-Lara-POO/SEMANA3",
        '4': "C:/Users/Win-10/fp/fudamento de programacion/UEA-L-UFB-030-D-Jenny-Lara-POO/Semana4",
        '5': "C:/Users/Win-10/fp/fudamento de programacion/UEA-L-UFB-030-D-Jenny-Lara-POO/semana 5",
        '6': "C:/Users/Win-10/fp/fudamento de programacion/UEA-L-UFB-030-D-Jenny-Lara-POO/semana 6",
        '7': "C:/Users/Win-10/fp/fudamento de programacion/UEA-L-UFB-030-D-Jenny-Lara-POO/semana 7",
    }

    while True:
        print("\nMenu Principal - Dashboard")
        for key, ruta in rutas_semanas.items():
            print(f"{key} - {os.path.basename(os.path.normpath(ruta))}")
        print("0 - Salir")

        eleccion_semana = input("Elige una semana o '0' para salir: ").strip()
        if eleccion_semana == '0':
            print("Saliendo del programa.")
            break

        if eleccion_semana in rutas_semanas:
            ruta_semana = rutas_semanas[eleccion_semana]
            if os.path.exists(ruta_semana):
                mostrar_sub_menu(ruta_semana)
            else:
                print("La carpeta de la semana no existe. Por favor, revisa la estructura del proyecto.")
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def mostrar_sub_menu(ruta_semana):
    try:
        sub_carpetas = [f.name for f in os.scandir(ruta_semana) if f.is_dir()]
        scripts = [f.name for f in os.scandir(ruta_semana) if f.is_file() and f.name.endswith('.py')]

        if not sub_carpetas and scripts:
            print("\nNo hay subcarpetas. Mostrando scripts directamente.")
            mostrar_scripts(ruta_semana)
            return

        while True:
            print("\nSubmenú - Selecciona una subcarpeta")
            for i, carpeta in enumerate(sub_carpetas, start=1):
                print(f"{i} - {carpeta}")
            print("0 - Regresar al menú principal")

            eleccion_carpeta = input("Elige una subcarpeta o '0' para regresar: ").strip()
            if eleccion_carpeta == '0':
                break
            else:
                try:
                    eleccion_carpeta = int(eleccion_carpeta) - 1
                    if 0 <= eleccion_carpeta < len(sub_carpetas):
                        mostrar_scripts(os.path.join(ruta_semana, sub_carpetas[eleccion_carpeta]))
                    else:
                        print("Opción no válida. Por favor, intenta de nuevo.")
                except ValueError:
                    print("Opción no válida. Por favor, intenta de nuevo.")
    except FileNotFoundError:
        print("La carpeta de la semana no existe. Por favor, revisa la estructura del proyecto.")

def mostrar_scripts(ruta_sub_carpeta):
    try:
        scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

        if not scripts:
            print("\nNo se encontraron scripts en esta carpeta.")
            return

        while True:
            print("\nScripts - Selecciona un script para ver y ejecutar")
            for i, script in enumerate(scripts, start=1):
                print(f"{i} - {script}")
            print("0 - Regresar al submenú anterior")

            eleccion_script = input("Elige un script o '0' para regresar: ").strip()
            if eleccion_script == '0':
                break
            else:
                try:
                    eleccion_script = int(eleccion_script) - 1
                    if 0 <= eleccion_script < len(scripts):
                        ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion_script])
                        codigo = mostrar_codigo(ruta_script)
                        if codigo:
                            ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ").strip()
                            if ejecutar == '1':
                                ejecutar_codigo(ruta_script)
                            elif ejecutar == '0':
                                print("No se ejecutó el script.")
                            else:
                                print("Opción no válida. Regresando al menú de scripts.")
                            input("\nPresiona Enter para volver al menú de scripts.")
                    else:
                        print("Opción no válida. Por favor, intenta de nuevo.")
                except ValueError:
                    print("Opción no válida. Por favor, intenta de nuevo.")
    except FileNotFoundError:
        print("La carpeta de scripts no existe. Por favor, revisa la estructura del proyecto.")

if __name__ == "__main__":
    mostrar_menu()6