#Ejercicio 8: Determinación de año bisiesto
#Escribe un programa que determine si un año es bisiesto o no.
#Enunciado:
#Solicita al usuario que ingrese un año y determina si es bisiesto (divisible entre 4, pero no entre
#100, salvo que sea divisible entre 400).


# Solicitar al usuario que ingrese un año
año = int(input("Introduce un año: "))

# Determinar si el año es bisiesto
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")
