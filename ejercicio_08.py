# Una institución educativa aprueba a un estudiante si cumple dos condiciones: una nota final
# igual o superior a 3.0 y una asistencia igual o superior al 80%. Escribe un algoritmo que
# reciba estos dos datos y determine si el estudiante aprueba o reprueba.


print("Evaluación de Aprobación Estudiantil")

nota_final = float(input("Ingresa la nota final del estudiante: "))
asistencia = float(input("Ingresa el porcentaje de asistencia del estudiante: "))

if nota_final >= 3.0 and asistencia >= 80:
    print("El estudiante APRUEBA.")
else:
    print("El estudiante REPRUEBA.")

print("Fin del proceso de evaluación.")