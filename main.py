#Ejercicio 6: Juego de adivinanza de números
#Escribe un programa que implemente un juego de adivinanza de números.
#Enunciado:
#El programa genera un número aleatorio entre 1 y 10. El usuario debe adivinar el número, y el
#programa indica si el número ingresado es mayor, menor o igual al número generado.

import random

# Generar un número aleatorio entre 1 y 10
numero_aleatorio = random.randint(1, 10)

# Variable para controlar si el usuario adivinó correctamente
adivinado = False

# Iniciar el juego
print("¡Bienvenido al juego de adivinanza de números!")
print("Estoy pensando en un número entre 1 y 10. ¡Intenta adivinarlo!")

# Bucle hasta que el usuario adivine el número
while not adivinado:
    # Solicitar al usuario que ingrese un número
    intento = int(input("Introduce tu número: "))
    
    # Comparar el intento del usuario con el número aleatorio
    if intento < numero_aleatorio:
        print("El número es mayor. Intenta de nuevo.")
    elif intento > numero_aleatorio:
        print("El número es menor. Intenta de nuevo.")
    else:
        print(f"¡Felicidades! Has adivinado el número {numero_aleatorio}.")
        adivinado = True
