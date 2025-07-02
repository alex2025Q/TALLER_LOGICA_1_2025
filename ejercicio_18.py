# Desarrolla un algoritmo que muestre un menú con las siguientes opciones:
# 1. Sumar
# 2. Restar
# 3. Multiplicar
# 4. Dividir
# El usuario elige una opción e ingresa dos números. El programa debe realizar la operación
# seleccionada y mostrar el resultado. Si la división es por cero, indicar 'No se puede dividir
# por cero'. 




print("MENÚ DE OPERACIONES")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = int(input("Elige una opción (1-4): "))
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if opcion == 1:
    print("Resultado:", num1 + num2)
elif opcion == 2:
    print("Resultado:", num1 - num2)
elif opcion == 3:
    print("Resultado:", num1 * num2)
elif opcion == 4:
    if num2 == 0:
        print("No se puede dividir por cero.")
    else:
        print("Resultado:", num1 / num2)
else:
    print("Opción no válida.")