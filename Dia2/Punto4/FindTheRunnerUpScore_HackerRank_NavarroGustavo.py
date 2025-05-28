# Entrada: Numero de Participantes(np) y Lista con las puntuaciones de estos
# Salida: Segunda puntuacion mas alta segun las lista de puntuaciones ingresada por el usuario

nP = int(input())  
puntuaciones = list(map(int, input().split()))  
puntuacionesUnicas = list(set(puntuaciones))  
puntuacionesUnicas.sort()  

print(puntuacionesUnicas[-2])  

# Desarrollado por Gustavo Adolfo Navarro Pacheco T.I 1.127.599.969