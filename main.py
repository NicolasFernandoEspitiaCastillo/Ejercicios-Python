#Ejercicio 3: Calculadora básica

#Utiliza match para implementar una calculadora simple.

#Enunciado:
#Crea una calculadora que solicite dos números y una operación matemática (+, -, *, /). Usa match
#para realizar la operación correspondiente.

def calculadora():
      
      #ingrese los numeros:
      num1 =float(input("Ingrese el primer numero: "))
      num2 =float(input("Ingrese el segundo numero: "))
      
      #operacion que desea realizar:
      Operacion = input("Ingrese la operacion a realizar (+, -, *, /): ")
      
      match Operacion:
          
          case "+":
            resultado = num1 + num2
            print(f"{num1} + {num2} = {resultado}")
          case "-":
            resultado = num1 - num2 
            print(f"{num1} - {num2} = {resultado}") 
          case "*":
            print(f"{num1} * {num2} = {resultado}")
          case "/":
            if num2 == 0:
               print("Error: no se puede divir por cero")
               return
            else: 
               print(f"{num1} / {num2} = {resultado}")
          case _:
            print("Operación no válida. Por favor, elige una operación entre +, -, *, /.")
            return  # Salir de la función si la operación no es válida


calculadora()



