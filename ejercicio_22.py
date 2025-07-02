# Un sistema de reservas permite elegir entre 3 tipos de evento:
# 1. Cine ($20.000)
# 2. Teatro ($35.000)
# 3. Concierto ($50.000)
# Luego debe ingresar la cantidad de entradas deseadas. Si el total supera los $100.000, se
# aplica un 10% de descuento. Calcula el total a pagar.



print("Tipos de evento:")
print("1. Cine ($20.000)")
print("2. Teatro ($35.000)")
print("3. Concierto ($50.000)")

opcion = int(input("Elige el tipo de evento (1-3): "))
cantidad = int(input("Ingresa la cantidad de entradas: "))

if opcion == 1:
    precio = 20000
elif opcion == 2:
    precio = 35000
elif opcion == 3:
    precio = 50000
