#Ejercicio 7: Número positivo, negativo o cero
#Escribe un programa que determine si un número es positivo, negativo o cero usando if .
#Enunciado:
#Solicita al usuario que ingrese un número y determina si es positivo, negativo o cero.


# Solicitar al usuario que ingrese un número
numero = float(input("Introduce un número: "))

# Determinar si el número es positivo, negativo o cero
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
