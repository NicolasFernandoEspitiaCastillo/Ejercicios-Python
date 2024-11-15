#Ejercicio 9: Clasificación de edades
#Escribe un programa que clasifique a una persona en función de su edad.
#Enunciado:
#Solicita la edad de la persona e indica si es niño (0-12 años), adolescente (13-17 años), adulto (18-
#64 años) o anciano (65 años o más).


# Solicitar la edad de la persona
edad = int(input("Introduce tu edad: "))

# Clasificar la persona según su edad
if 0 <= edad <= 12:
    print("Eres un niño.")
elif 13 <= edad <= 17:
    print("Eres un adolescente.")
elif 18 <= edad <= 64:
    print("Eres un adulto.")
else:
    print("Eres un anciano.")
