# Algoritmo para generar la serie de Fibonacci

# Pedir al usuario la cantidad de numeros de la serie de fibo que desea
n = int(input("Introduce la cantidad de numeros de la serie de Fibo que desea"))

# Asignar los dos primeros valores de la serie
a, b = 0, 1

# Imprimir texto
print("Serie de Fibonacci:")

# Imprimir por completo la serie de fibo hasta el limite puesto por el usuario
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b 
