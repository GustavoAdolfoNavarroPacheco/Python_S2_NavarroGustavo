# Algoritmo para verificar si un numero es primo

# Se le pide al usuario que ingrese el numero que desea verificar
numero = int(input("Ingresa el numero que desea verificar"))
# Se verifica que sea mayor que uno
if numero <= 1:
    print("ERROR! El numero debe ser mayor que 1")
# Se hace el proseso de verificacion
else:
    primo = True
    divisor = 2

    while divisor < numero:
        if numero % divisor == 0:
            primo = False
            divisor = divisor + 1
# Se imprime el resultado de la verificacion
    if primo:
        print(numero, "Si es primo")
    else:
        print(numero, "No es primo")

#Desarrollado por Gustavo Adolfo Navarro Pacheco T.I 1.127.599.969