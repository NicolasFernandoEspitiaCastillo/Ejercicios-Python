#Ejercicio 20: Conversión de calificaciones numéricas a letras
#Escribe un programa que convierta una calificación numérica en una letra de acuerdo a un
#sistema de calificación específico, usando match .
#Enunciado:
#Solicita una calificación numérica (0-100) y convierte esa calificación a una letra usando el
#siguiente esquema:
#A: 90-100
#B: 80-89
#C: 70-79
#D: 60-69
#F: 0-59



# Solicitar la calificación numérica
calificacion = int(input("Introduce la calificación numérica (0-100): "))

# Usar match para convertir la calificación numérica a una letra
match calificacion:
    case calificacion if 90 <= calificacion <= 100:
        letra = "A"
    case calificacion if 80 <= calificacion <= 89:
        letra = "B"
    case calificacion if 70 <= calificacion <= 79:
        letra = "C"
    case calificacion if 60 <= calificacion <= 69:
        letra = "D"
    case _:
        letra = "F"

# Mostrar la calificación en letra
print(f"La calificación en letra es: {letra}")
