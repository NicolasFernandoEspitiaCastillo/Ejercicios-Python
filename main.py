#Ejercicio 7: Suma de números pares hasta que se introduce
#un impar
#Enunciado:
#Escribe un programa que solicite al usuario ingresar números enteros indefinidamente. El
#programa debe sumar los números siempre que sean pares, pero debe detenerse si el usuario
#ingresa un número impar. Usa un ciclo while para lograr esto.


# Inicializar la suma en 0
suma_pares = 0

# Usar un ciclo while para ingresar números indefinidamente
while True:
    # Solicitar al usuario que ingrese un número
    numero = int(input("Introduce un número entero (o un impar para detener): "))
    
    # Verificar si el número es impar
    if numero % 2 != 0:
        print("Has ingresado un número impar. El programa se detiene.")
        break  # Detener el ciclo si el número es impar
    else:
        suma_pares += numero  # Sumar el número si es par

# Mostrar la suma de los números pares
print(f"La suma de los números pares ingresados es: {suma_pares}")
