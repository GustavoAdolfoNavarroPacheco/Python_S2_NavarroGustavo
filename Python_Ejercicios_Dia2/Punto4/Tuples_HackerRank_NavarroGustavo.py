# Entrada: Numero que indica cuantos elementos se ingresaran para formar una tupla
# Salida: Hash que corresponde a la tupla formada con esos elementos

n = int(input())

tupla = tuple(map(int, input().split()))
print(hash(tupla))

# Desarrollado por Gustavo Adolfo Navarro Pacheco T.I 1.127.599.969
