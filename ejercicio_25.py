# Recibe una nota entre 0 y 5 y una letra entre A y F. - Si la nota es menor a 3, debe coincidir con una letra D o F - Si la nota es 3 o más, debe coincidir con una letra A, B o C
# Si hay inconsistencia entre número y letra, se muestra un mensaje de advertencia: 'Nota y
# letra no coinciden'.

nota = float(input("Ingrese la nota (0 a 5): "))
letra = input("Ingrese la letra (A a F): ").upper()

if nota < 0 or nota > 5:
    print("Nota fuera de rango")

elif nota < 3:
    if letra in ["C", "D", "F"]:
        print("Nota y letra son coherentes")
    else:
        print("Nota y letra no coinciden, favor revisar")

else:  # nota >= 3
    if letra in ["A", "B"]:
        print("Nota y letra son coherentes")
    else:
        print("Nota y letra no coinciden, favor revisar")
