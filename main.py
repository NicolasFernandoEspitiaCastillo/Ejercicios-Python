#Ejercicio 13: Comparación de tres números
#Escribe un programa que determine el mayor de tres números usando if .
#Enunciado:
#Solicita al usuario que ingrese tres números y determina cuál es el mayor.


# Solicitar tres números al usuario
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
numero3 = float(input("Introduce el tercer número: "))

# Determinar el mayor de los tres números usando if-elif-else
if numero1 >= numero2 and numero1 >= numero3:
    mayor = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    mayor = numero2
else:
    mayor = numero3

# Mostrar el resultado
print(f"El mayor de los tres números es: {mayor}")
