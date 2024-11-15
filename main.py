#Ejercicio 16: Cálculo del tiempo de viaje
#Escribe un programa que calcule el tiempo que tarda en llegar un automóvil a su destino.
#Enunciado:
#Solicita al usuario la distancia a recorrer (en km) y la velocidad promedio del automóvil (en km/h).
#Calcula el tiempo de viaje en horas y minutos. Si la velocidad es mayor a 120 km/h, muestra un
#mensaje de advertencia.



# Solicitar la distancia a recorrer y la velocidad promedio
distancia = float(input("Introduce la distancia a recorrer (en km): "))
velocidad = float(input("Introduce la velocidad promedio (en km/h): "))

# Calcular el tiempo de viaje en horas
tiempo_horas = distancia / velocidad

# Convertir la parte decimal de las horas a minutos
horas = int(tiempo_horas)
minutos = int((tiempo_horas - horas) * 60)

# Mostrar advertencia si la velocidad es mayor a 120 km/h
if velocidad > 120:
    print("Advertencia: La velocidad es mayor a 120 km/h. ¡Conduce con precaución!")

# Mostrar el tiempo de viaje en horas y minutos
print(f"El tiempo de viaje es {horas} horas y {minutos} minutos.")
