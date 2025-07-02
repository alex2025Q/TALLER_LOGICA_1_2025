# Una empresa de energía desea categorizar a sus clientes en tres rangos tarifarios según el
# consumo mensual de kilovatios-hora (kWh): - Menor a 100 kWh → 'Estrato bajo' - Entre 100 y 200 kWh → 'Estrato medio' - Mayor a 200 kWh → 'Estrato alto'
# Desarrolla un algoritmo que reciba el consumo y muestre la categoría correspondiente. 


print("Sistema de Clasificación de Consumo Energético")

consumo = float(input("Ingresa el consumo mensual en kWh: "))

if consumo < 100:
    print("Categoría: Estrato bajo")
elif consumo <= 200:
    print("Categoría: Estrato medio")
else:
    print("Categoría: Estrato alto")

print("Gracias por utilizar el sistema de clasificación.")