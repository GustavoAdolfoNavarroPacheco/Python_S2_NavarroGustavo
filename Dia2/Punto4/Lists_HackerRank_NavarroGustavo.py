# Entrada: Numero de comandos a ejecutar
# Salida: Lista despues de la ejecucion de los comandos pedidos por el user

lista = []
n = int(input())

for _ in range(n):
    comando = input().split()
    if comando[0] == 'insert':
        i = int(comando[1])
        e = int(comando[2])
        lista.insert(i, e)
    elif comando[0] == 'print':
        print(lista)
    elif comando[0] == 'remove':
        e = int(comando[1])
        lista.remove(e)
    elif comando[0] == 'append':
        e = int(comando[1])
        lista.append(e)
    elif comando[0] == 'sort':
        lista.sort()
    elif comando[0] == 'pop':
        lista.pop()
    elif comando[0] == 'reverse':
        lista.reverse()

# Desarrollado por Gustavo Adolfo Navarro Pacheco T.I 1.127.599.969