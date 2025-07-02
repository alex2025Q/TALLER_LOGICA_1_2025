# Un sistema digital restringido solicita al usuario ingresar un nombre de usuario y una
# contraseña. Si ambos coinciden exactamente con los valores esperados ('admin' y '1234'), se
# debe mostrar 'Acceso concedido'. En caso contrario, mostrar 'Acceso denegado'. Crea el
# algoritmo para esta validación.



print("Sistema de Acceso Restringido")

usuario = input("Ingresa el nombre de usuario: ")
contrasena = input("Ingresa la contraseña: ")

if usuario == "admin" and contrasena == "1234":
    print("Acceso concedido")
else:
    print("Acceso denegado, mi hermano quien es usted")

print("Fin del proceso de validación.")