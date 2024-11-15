#Ejercicio 11: Conversión de temperaturas
#Escribe un programa que convierta grados Celsius a Fahrenheit o Fahrenheit a Celsius usando
#match .
#Enunciado:
#Solicita al usuario que ingrese una temperatura y una escala (C o F). Convierte la temperatura a la
#escala opuesta usando match .

# Solicitar la temperatura y la escala al usuario
temperatura = float(input("Introduce la temperatura: "))
escala = input("Introduce la escala (C para Celsius, F para Fahrenheit): ").upper()

# Usar match para realizar la conversión según la escala proporcionada
match escala:
    case 'C':
        # Convertir de Celsius a Fahrenheit
        fahrenheit = (temperatura * 9/5) + 32
        print(f"{temperatura} grados Celsius equivalen a {fahrenheit} grados Fahrenheit.")
    case 'F':
        # Convertir de Fahrenheit a Celsius
        celsius = (temperatura - 32) * 5/9
        print(f"{temperatura} grados Fahrenheit equivalen a {celsius} grados Celsius.")
    case _:
        print("Escala no válida. Por favor, ingresa 'C' para Celsius o 'F' para Fahrenheit.")
