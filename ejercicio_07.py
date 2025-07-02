# En una tienda de tecnología se aplican descuentos por el valor total de la compra: - Sin descuento si es menor a $100.000 - 5% si está entre $100.000 y $200.000 - 10% si supera los $200.000
# Crea un algoritmo que reciba el valor de la compra y muestre qué porcentaje de descuento
# aplica. 



print("Bienvenido a la Tienda de Tecnología")
print("Vamos a calcular el descuento según el valor de tu compra.")

valor_compra = float(input("Ingresa el valor total de tu compra en pesos: "))

if valor_compra < 100000:
    print("No aplica ningún descuento.")
elif valor_compra <= 200000:
    print("Aplica un 5% de descuento.")
else:
    print("Aplica un 10% de descuento.")

print("Gracias por comprar con nosotros.")