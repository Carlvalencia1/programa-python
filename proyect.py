import os
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.optimize import minimize_scalar

# Ruta de la carpeta donde están las imágenes
CARPETA_IMAGENES = "image"

# Matricula válida para salir
MATRICULA_CORRECTA = "233428"  

def calcular_minimo_funcion():
    print("Calculando mínimo de la función f(x) = x^2 - 4x + 3")

    # Definimos la función
    f = lambda x: x**2 - 4*x + 3

    # Buscamos el mínimo en el intervalo [-10, 10]
    resultado = minimize_scalar(f, bounds=(-10, 10), method='bounded')

    if resultado.success:
        print(f"Mínimo encontrado: f({resultado.x:.2f}) = {resultado.fun:.2f}")
    else:
        print("No se pudo calcular el mínimo.")

def mostrar_imagen_aleatoria():
    if not os.path.exists(CARPETA_IMAGENES):
        print(f"La carpeta '{CARPETA_IMAGENES}' no existe.")
        return

    imagenes = [img for img in os.listdir(CARPETA_IMAGENES) if img.lower().endswith(('.png', '.jpg', '.jpeg'))]

    if not imagenes:
        print("No hay imágenes en la carpeta.")
        return

    imagen_elegida = random.choice(imagenes)
    ruta_completa = os.path.join(CARPETA_IMAGENES, imagen_elegida)

    print(f"Mostrando imagen: {imagen_elegida}")
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
                print("¡Hasta pronto!")
                break
            else:
                print("Matrícula incorrecta.")
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
