# Una campaña de donación requiere filtrar a los posibles donantes. Para ser apto, la persona
# debe tener entre 18 y 65 años y pesar al menos 50 kg. Escribe un algoritmo que reciba la
# edad y el peso de una persona, y determine si está apta o no para donar sangre, mostrando
# un mensaje adecuado.



print("Campaña de Donación de Sangre")

edad = int(input("Ingresa tu edad: "))
peso = float(input("Ingresa tu peso en kilogramos: "))

if 18 <= edad <= 65 and peso <= 50:
    print("Estás apto para donar sangre.")
else:
    print("No estás apto para donar sangre.")

print("Gracias por participar en la campaña.")