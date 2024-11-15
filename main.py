#Ejercicio 5: Días de la semana
#Escribe un programa que, dado un número del 1 al 7, imprima el día correspondiente de la
#semana usando match .

#Enunciado:
#Solicita al usuario un número del 1 al 7 y muestra el día de la semana correspondiente (1 = Lunes, 7 = Domingo).

# Solicitar al usuario un número del 1 al 7
numero = int(input("Introduce un número del 1 al 7: "))

# Usar match para determinar el día de la semana
match numero:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _:
        print("Número inválido, por favor ingresa un número entre 1 y 7.")
