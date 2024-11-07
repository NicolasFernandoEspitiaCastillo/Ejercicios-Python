#Ejercicio 2: Calificación de una nota

#Escribe un programa que determine si una nota numérica es "Aprobado" o "Reprobado" usando if.

#Enunciado:
#Solicita al usuario una calificación y determina si la nota es aprobatoria (>= 60) o reprobatoria (<60).


Nota = int(input("Ingrese la nota: "))
if Nota >=60:
    print(f"Aprobado")
else: 
    print(f"Reprobado")
