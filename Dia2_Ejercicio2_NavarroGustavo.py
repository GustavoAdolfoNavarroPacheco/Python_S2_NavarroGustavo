# Algoritmo para Encontrar el mayor de tres numeros

# El usuario ingresa el primer numero
numero1 = float(input("Ingrese el primer numero"))
# El usuario ingresa el segundo numero
numero2 = float(input("Ingrese el segundo numero"))
# El usuario ingresa el tercer numero
numero3 = float(input("Ingrese el tercer numero"))
# Se hace la logica para saber cual es el numero mayor e imprimirlo
if (numero1 > numero2 and numero1 > numero3): 
    print("El numero mayor es", numero1)
elif(numero2 > numero1 and numero2 > numero3): 
    print("El numero mayor es", numero2)
else: print("El numero mayor es", numero3)

#Desarrollado por Gustavo Adolfo Navarro Pacheco T.I 1.127.599.969