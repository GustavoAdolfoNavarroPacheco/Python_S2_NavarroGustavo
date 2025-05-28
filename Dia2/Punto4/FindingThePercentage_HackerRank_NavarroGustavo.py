# Entrada: Numero de estudiantes, nombre y calificaciones, estudiante a Consultar
# Salida: Promedio del Estudiante consultado por el user

n = int(input())
estudiantes = {}

for i in range(n):
    entrada = input().split()
    nombre = entrada[0]
    calificaciones = list(map(float, entrada[1:]))
    estudiantes[nombre] = calificaciones
    
estConsulta = input()
promedio = sum(estudiantes[estConsulta]) / len(estudiantes[estConsulta])

print("{:.2f}".format(promedio))


# Desarrollado por Gustavo Adolfo Navarro Pacheco T.I 1.127.599.969