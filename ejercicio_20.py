# Un parqueadero cobra según el tipo de vehículo: - Carro → $5.000/hora - Moto → $2.000/hora - Bicicleta → $500/hora
# Diseña un algoritmo que reciba el tipo de vehículo y el número de horas y calcule el total a pagar.



tipo = input("Ingresa el tipo de vehículo (carro, moto, bicicleta): ").lower()
horas = int(input("Ingresa el número de horas: "))

if tipo == "carro":
    tarifa = 5000
elif tipo == "moto":
    tarifa = 2000
elif tipo == "bicicleta":
    tarifa = 500
else:
    tarifa = 0

if tarifa == 0:
    print("Tipo de vehículo no válido.")
else:
    total = tarifa * horas
    print("Total a pagar: $", total)