#Ejercicio 15: Cálculo del salario neto
#Escribe un programa que calcule el salario neto de un empleado después de aplicar impuestos.
#Enunciado:
#Solicita al usuario su salario bruto y su país de residencia. Calcula el salario neto aplicando
#impuestos: el 20% para residentes de "País A", el 15% para "País B" y el 10% para "País C". Si el
#país no está en la lista, aplica un 25% de impuestos.


# Solicitar el salario bruto y el país de residencia
salario_bruto = float(input("Introduce tu salario bruto: "))
pais = input("Introduce tu país de residencia: ").strip().title()  # Limpiar espacios y capitalizar el nombre del país

# Determinar el porcentaje de impuestos según el país
if pais == "País A":
    porcentaje_impuesto = 0.20
elif pais == "País B":
    porcentaje_impuesto = 0.15
elif pais == "País C":
    porcentaje_impuesto = 0.10
else:
    porcentaje_impuesto = 0.25  # Para países no listados, aplicar el 25% de impuestos

# Calcular el salario neto
impuesto = salario_bruto * porcentaje_impuesto
salario_neto = salario_bruto - impuesto

# Mostrar el salario neto
print(f"Tu salario neto después de impuestos es: {salario_neto:.2f} unidades monetarias.")
