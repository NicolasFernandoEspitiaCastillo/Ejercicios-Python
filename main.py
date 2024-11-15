#Ejercicio 3: Factorial de un número
#Enunciado:
#Escribe un programa que solicite al usuario un número entero positivo n y calcule el factorial de
#dicho número ( n! = 1 * 2 * 3 * ... * n ). Usa un ciclo for para realizar el cálculo.



# Solicitar al usuario el número entero positivo n
n = int(input("Introduce un número entero positivo: "))

# Verificar que el número sea positivo
if n < 0:
    print("Por favor, introduce un número entero positivo mayor o igual a 0.")
else:
    # Inicializar el resultado en 1 (ya que el factorial de 0 es 1)
    factorial = 1
    
    # Usar un ciclo for para calcular el factorial
    for i in range(1, n + 1):
        factorial *= i  # Multiplicamos el resultado por cada número de 1 a n
    
    # Mostrar el resultado
    print(f"El factorial de {n} es: {factorial}")
