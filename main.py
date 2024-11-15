#Ejercicio 2: Contador de vocales en una cadena
#Enunciado:
#Escribe un programa que solicite al usuario una cadena de texto y cuente cuántas vocales 
#(a, e, i, o, u) contiene. Usa un ciclo for para recorrer la cadena y realizar la cuenta.


# Solicitar al usuario una cadena de texto
texto = input("Introduce una cadena de texto: ")

# Inicializar el contador de vocales
contador_vocales = 0

# Definir las vocales (tanto minúsculas como mayúsculas)
vocales = "aeiouAEIOU"

# Usar un ciclo for para recorrer cada carácter en la cadena
for char in texto:
    if char in vocales:
        contador_vocales += 1  # Incrementar el contador si el carácter es una vocal

# Mostrar el número de vocales
print(f"La cadena tiene {contador_vocales} vocales.")
