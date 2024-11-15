#Ejercicio 4: Números pares en un rango
#Enunciado:
#Escribe un programa que solicite al usuario dos números enteros, un valor de inicio y un valor de
#fin. El programa debe imprimir todos los números pares en ese rango, incluyendo los límites. Usa
#un ciclo for para recorrer el rango.


# Solicitar al usuario los dos números enteros (inicio y fin)
inicio = int(input("Introduce el valor de inicio: "))
fin = int(input("Introduce el valor de fin: "))

# Usar un ciclo for para recorrer el rango de números
for num in range(inicio, fin + 1):  # range(inicio, fin+1) incluye el valor de fin
    if num % 2 == 0:  # Verificamos si el número es par
        print(num)
