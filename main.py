#Ejercicio 4: Determinación del tipo de triángulo

#Escribe un programa que determine el tipo de triángulo en función de sus lados usando if .

#Enunciado:

#Solicita al usuario que ingrese las longitudes de los tres lados de un triángulo. Determina si el
#triángulo es equilátero, isósceles o escaleno.

# Solicitar las longitudes de los tres lados del triángulo
lado1 = float(input("Ingresa el primer lado del triángulo: "))
lado2 = float(input("Ingresa el segundo lado del triángulo: "))
lado3 = float(input("Ingresa el tercer lado del triángulo: "))

# Determinar el tipo de triángulo
if lado1 == lado2 == lado3:
    print("El triángulo es equilátero.")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("El triángulo es isósceles.")
else:
    print("El triángulo es escaleno.")
