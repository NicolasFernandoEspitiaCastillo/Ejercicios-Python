#Ejercicio 1: Verificación de números pares e impares

#Escribe un programa que verifique si un número es par o impar utilizando if .


#Enunciado:
#Solicita al usuario que ingrese un número y verifica si es par o impar.

numero = int(input("ingrese el numero: "))
if numero % 2 == 1:
    print(f"Par")
else:
    print(f"Impar") 
    1