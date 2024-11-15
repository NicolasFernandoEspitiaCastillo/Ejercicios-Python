#Ejercicio 21: Sistema de estacionamiento con tarifas
#progresivas
#Escribe un programa que calcule el costo de estacionamiento basado en el número de horas, con
#tarifas progresivas.
#Enunciado:
#El costo de estacionamiento se calcula de la siguiente manera:
#Primera hora: $5
#Segunda a cuarta hora: $4 por hora
#Más de cuatro horas: $3 por cada hora adicional
#Solicita al usuario el número de horas de estacionamiento y calcula el costo total.



# Solicitar el número de horas de estacionamiento
horas = int(input("Introduce el número de horas de estacionamiento: "))

# Inicializar el costo
costo_total = 0

# Calcular el costo basado en las tarifas progresivas
if horas <= 1:
    costo_total = 5  # Primera hora
elif 2 <= horas <= 4:
    costo_total = 5 + (horas - 1) * 4  # Primera hora + 2 a 4 horas
else:
    costo_total = 5 + 3 * 4 + (horas - 4) * 3  # Primera hora + 2 a 4 horas + más de 4 horas

# Mostrar el costo total
print(f"El costo total de estacionamiento es: ${costo_total}")
