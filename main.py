#Ejercicio 22: Clasificación de triángulos por sus ángulos
#Escribe un programa que clasifique un triángulo en agudo, obtuso o rectángulo según sus ángulos
#internos usando if .
#Enunciado:
#Solicita al usuario los tres ángulos de un triángulo y clasifícalo en:
#Agudo: Todos los ángulos son menores a 90°.
#Rectángulo: Un ángulo es exactamente 90°.
#Obtuso: Un ángulo es mayor a 90°.



# Solicitar los tres ángulos del triángulo
angulo1 = float(input("Introduce el primer ángulo (en grados): "))
angulo2 = float(input("Introduce el segundo ángulo (en grados): "))
angulo3 = float(input("Introduce el tercer ángulo (en grados): "))

# Verificar si la suma de los ángulos es 180°
if angulo1 + angulo2 + angulo3 != 180:
    print("Los ángulos no forman un triángulo válido. La suma de los ángulos debe ser 180°.")
else:
    # Clasificación según los ángulos
    if angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
        print("El triángulo es Rectángulo.")
    elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
        print("El triángulo es Obtuso.")
    else:
        print("El triángulo es Agudo.")
