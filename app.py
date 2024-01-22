# Función para sumar dos números
def sumar(num1, num2):
    return num1 + num2

# Función para restar dos números
def restar(num1, num2):
    return num1 - num2

# Función para multiplicar dos números
def multiplicar(num1, num2):
    return num1 * num2

# Función para dividir dos números
def dividir(num1, num2):
    # Manejar la división por cero
    if num2 == 0:
        return "Error: No se puede dividir por cero."
    else:
        return num1 / num2

# Solicitar al usuario que ingrese dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Mostrar opciones de operaciones
print("Operaciones disponibles:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

# Solicitar al usuario que elija una operación
opcion = input("Seleccione una operación (1/2/3/4): ")

# Realizar la operación seleccionada
if opcion == "1":
    resultado = sumar(numero1, numero2)
elif opcion == "2":
    resultado = restar(numero1, numero2)
elif opcion == "3":
    resultado = multiplicar(numero1, numero2)
elif opcion == "4":
    resultado = dividir(numero1, numero2)
else:
    resultado = "Opción no válida"

# Mostrar el resultado
print(f"El resultado de la operación es: {resultado}")
