# Algoritmo para generar la serie de Fibonacci

# Pedir al usuario la cantidad de numeros de la serie de fibo que desea
cantidadMax = int(input("Introduce la cantidad de numeros de la serie de Fibo que desea"))

# Asignar los dos primeros valores de la serie
a = 0
b = 1
# Imprimir texto
print("Serie de Fibonacci:")

# Imprimir por completo la serie de fibo hasta el limite puesto por el usuario
for i in range(cantidadMax):
    print(a, end=" ")
    a, b = b, a + b 

#Desarrollado por Gustavo Adolfo Navarro Pacheco T.I 1.127.599.969