#Ejercicio 14: Adivinanza de letras
#Escribe un programa que permita al usuario adivinar una letra secreta usando match .
#Enunciado:
#El programa contiene una letra secreta (por ejemplo, "A"). El usuario debe adivinar la letra, y el
#programa le indicará si acertó o no.


# Definir la letra secreta
letra_secreta = 'A'

# Solicitar al usuario que adivine la letra
letra_adivinada = input("Adivina la letra secreta: ").upper()  # Convertir la entrada a mayúsculas

# Usar match para comparar la letra adivinada con la letra secreta
match letra_adivinada:
    case 'A':
        print("¡Felicidades! Has adivinado la letra secreta.")
    case 'B':
        print("¡Lo intentaste con 'B'!")
    case _:
        print("¡Intenta de nuevo! No acertaste la letra secreta.")


