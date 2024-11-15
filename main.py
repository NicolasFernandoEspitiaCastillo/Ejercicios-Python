#Ejercicio 1: Suma de los primeros N números enteros
#Enunciado:
#Escribe un programa que solicite al usuario un número entero positivo n y calcule la suma de los
#primeros n números enteros. Utiliza un ciclo for para realizar la suma.



# Solicitar al usuario el número entero positivo n
n = int(input("Introduce un número entero positivo: "))

# Verificar que el número sea positivo
if n <= 0:
    print("Por favor, introduce un número entero positivo mayor que 0.")
else:
    # Inicializar la suma en 0
    suma = 0
    
    # Usar un ciclo for para sumar los primeros n números enteros
    for i in range(1, n + 1):
        suma += i  # Acumulamos la suma
    
    # Mostrar el resultado
    print(f"La suma de los primeros {n} números enteros es: {suma}")
