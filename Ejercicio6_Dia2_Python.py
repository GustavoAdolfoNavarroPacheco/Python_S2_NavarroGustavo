# Algortimo para saber si un numero es par o no

# Se le pide al usuario el numero que desea probar
numero = int(input("Introduce un numero"))

# Proseso de verificacion e impresion de resultado
if numero % 2 == 0:
    print("El numero ",numero,"Es PAR")
else:
    print("El numero ",numero,"Es Impar")
