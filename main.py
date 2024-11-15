#Ejercicio 18: Sistema de evaluación de créditos universitarios
#Escribe un programa que calcule el número de créditos totales de un estudiante en base a las
#materias cursadas y el puntaje obtenido en cada una. El puntaje debe ser evaluado como
#aprobado o no aprobado.
#Enunciado:
#Solicita al usuario ingresar el número de materias que ha cursado. Para cada materia, solicita el
#puntaje y determina si ha aprobado o no (>= 60). Luego, calcula el número total de créditos del
#estudiante (cada materia aprobada otorga 3 créditos).


# Solicitar el número de materias cursadas
num_materias = int(input("¿Cuántas materias has cursado? "))

# Inicializar el contador de créditos
creditos_totales = 0

# Iterar sobre cada materia
for i in range(num_materias):
    puntaje = float(input(f"Introduce el puntaje de la materia {i+1}: "))
    
    # Verificar si el puntaje es aprobado (mayor o igual a 60)
    if puntaje >= 60:
        creditos_totales += 3  # Cada materia aprobada otorga 3 créditos
        print(f"Materia {i+1}: Aprobado. Créditos ganados: 3")
    else:
        print(f"Materia {i+1}: No aprobado. Créditos ganados: 0")

# Mostrar el total de créditos obtenidos
print(f"\nTotal de créditos obtenidos: {creditos_totales}")
