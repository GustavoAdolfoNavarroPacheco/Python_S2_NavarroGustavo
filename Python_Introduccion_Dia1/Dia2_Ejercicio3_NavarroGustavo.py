# Algoritmo para sacar el factorial de un numero

# Pedir el numero al cual desea sacarle factorial
numero = int(input("Ingresa el numero al cual deseas sacarle factorial"))

# Se verifica que el numero sea positivo
if numero < 0:
    print("Ingresa un numero POSITIVO!")
# Se hace el proseso de sacar el factorial
else:
    factorial = 1
    max = 1

    while max <= numero:
        factorial = factorial * max
        max = max + 1
# Se imprime el factorial del numero
print("El factorial de ",numero," es ",factorial)

#Desarrollado por Gustavo Adolfo Navarro Pacheco T.I 1.127.599.969
