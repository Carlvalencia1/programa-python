import os
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.optimize import minimize_scalar
import numpy as np
import math

# Ruta de la carpeta de imágenes
CARPETA_IMAGENES = "image"

# Matrícula válida para salir
MATRICULA_CORRECTA = "233428"  # <-- CAMBIA ESTO POR TU MATRÍCULA REAL

def calcular_minimo_funcion():
    print("\nElige la función a minimizar:")
    print("1. Parabólica simple               f(x) = x² - 4x + 3")
    print("2. Función cúbica desplazada       f(x) = (x - 1)³ + x²")
    print("3. Función senoidal                f(x) = sin(x) + 0.1x²")
    print("4. Logarítmica con penalización    f(x) = ln(x) + x²")
    print("5. Función exponencial amortiguada f(x) = e^(-x) + x²")
    print("6. Ingresar mi propia función")

    opcion = input("Opción: ")

    intervalo = (-10, 10)
    if opcion == "1":
        f = lambda x: x**2 - 4*x + 3
    elif opcion == "2":
        f = lambda x: (x - 1)**3 + x**2
    elif opcion == "3":
        f = lambda x: np.sin(x) + 0.1 * x**2
    elif opcion == "4":
        f = lambda x: np.log(x) + x**2 if x > 0 else float('inf')
        intervalo = (0.1, 10)
    elif opcion == "5":
        f = lambda x: np.exp(-x) + x**2
        intervalo = (-5, 5)
    elif opcion == "6":
        expresion = input("Escribe tu función en términos de x (ejemplo: x**2 + 3*x - 1): ")
        try:
            entorno = {
                "x": 0, "sin": math.sin, "cos": math.cos, "tan": math.tan,
                "log": math.log, "exp": math.exp, "sqrt": math.sqrt,
                "pi": math.pi, "e": math.e
            }
            f = lambda x: eval(expresion, {"__builtins__": {}}, {**entorno, "x": x})
        except Exception as e:
            print("❌ Error al interpretar la función:", e)
            return
    else:
        print("⚠️ Opción no válida.")
        return

    resultado = minimize_scalar(f, bounds=intervalo, method='bounded')

    if resultado.success:
        print(f"\n✅ Mínimo encontrado: f({resultado.x:.4f}) = {resultado.fun:.4f}")
    else:
        print("❌ No se pudo calcular el mínimo.")

def mostrar_imagen_aleatoria():
    if not os.path.exists(CARPETA_IMAGENES):
        print(f"⚠️ La carpeta '{CARPETA_IMAGENES}' no existe.")
        return

    imagenes = [img for img in os.listdir(CARPETA_IMAGENES)
                if img.lower().endswith(('.png', '.jpg', '.jpeg'))]

    if not imagenes:
        print("⚠️ No hay imágenes en la carpeta.")
        return

    imagen_elegida = random.choice(imagenes)
    ruta_completa = os.path.join(CARPETA_IMAGENES, imagen_elegida)

    print(f"🖼️ Mostrando imagen: {imagen_elegida}")
    img = mpimg.imread(ruta_completa)
    plt.imshow(img)
    plt.axis('off')
    plt.show()

def menu():
    while True:
        print("\n¿Qué opción eliges?")
        print("1.- Calcular mínimo de la función")
        print("2.- Mostrar imagen aleatoria")
        print("3.- Salir")

        opcion = input("Ingresa una opción: ")

        if opcion == "1":
            calcular_minimo_funcion()
        elif opcion == "2":
            mostrar_imagen_aleatoria()
        elif opcion == "3":
            matricula = input("Teclea tu matrícula completa para salir: ")
            if matricula == MATRICULA_CORRECTA:
                print("✅ Matrícula correcta. ¡Hasta pronto!")
                break
            else:
                print("❌ Matrícula incorrecta.")
        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
