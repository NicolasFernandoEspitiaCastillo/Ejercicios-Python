#Ejercicio 12: Calculadora de IMC (Índice de Masa Corporal)
#Escribe un programa que calcule el IMC y determine el estado de peso.
#Enunciado:
#Solicita al usuario su peso (en kg) y su altura (en metros). Calcula el IMC y clasifícalo en bajo peso
#(<18.5), peso normal (18.5-24.9), sobrepeso (25-29.9), o obesidad (>=30).



# Solicitar el peso y la altura del usuario
peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))

# Calcular el IMC
imc = peso / (altura ** 2)

# Clasificar el IMC
if imc < 18.5:
    estado = "Bajo peso"
elif 18.5 <= imc <= 24.9:
    estado = "Peso normal"
elif 25 <= imc <= 29.9:
    estado = "Sobrepeso"
else:
    estado = "Obesidad"

# Mostrar el IMC y el estado de peso
print(f"Tu IMC es {imc:.2f}, lo que indica que tienes {estado}.")
