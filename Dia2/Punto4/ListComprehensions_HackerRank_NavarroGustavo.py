# Entrada: 4 numeros ingresados por el usuario
# Salida: Una lista de listas con todas las combinaciones posibles de [x, y, z] dentro de los numero ingresado, excepto las que suman exactamente = limite

x_max = int(input())
y_max = int(input())
z_max = int(input())
limite = int(input())

resultado = [[x, y, z] 
           for x in range(x_max + 1) 
           for y in range(y_max + 1) 
           for z in range(z_max + 1) 
           if x + y + z != limite]

print(resultado)

# Desarrollado por Gustavo Adolfo Navarro Pacheco T.I 1.127.599.969