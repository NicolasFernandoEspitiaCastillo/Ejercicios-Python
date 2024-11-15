#Ejercicio 6: Adivina el número (con while )
#Enunciado: (random.randint(1, 100))
#Escribe un programa que genere un número aleatorio entre 1 y 100 y permita al usuario
#adivinarlo. El programa debe dar pistas si el número ingresado es mayor o menor que el número
#secreto. Usa un ciclo while para permitir al usuario seguir intentando hasta que adivine el
#número

import random

# Generar un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# Inicializar la variable que almacenará el intento del usuario
intento = None

# Usar un ciclo while para seguir pidiendo al usuario hasta que adivine el número
while intento != numero_secreto:
    # Solicitar al usuario que ingrese un número
    intento = int(input("Adivina el número (entre 1 y 100): "))
    
    # Dar pistas si el número ingresado es mayor o menor que el número secreto
    if intento < numero_secreto:
        print("El número secreto es mayor. Intenta nuevamente.")
    elif intento > numero_secreto:
        print("El número secreto es menor. Intenta nuevamente.")
    else:
        print(f"¡Felicidades! Has adivinado el número {numero_secreto}.")
