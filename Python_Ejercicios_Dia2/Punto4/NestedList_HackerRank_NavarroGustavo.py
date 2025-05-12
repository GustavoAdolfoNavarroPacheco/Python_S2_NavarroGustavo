# Entrada: Leer Cantidad de Estudiantes, nombre de cada uno  y calificaciones de estos
# Salida: Estudiante con la segunda calificacion mas baja
cantidadEstudiantes = int(input())

estudiantes = [] 
for i in range(cantidadEstudiantes):
    nombre = input()
    calificacion = float(input())
    estudiantes.append([nombre, calificacion])  

calificaciones = sorted(set([calificacion for nombre, calificacion in estudiantes]))
segundaBaja = calificaciones[1]
estudiantesSegundaBaja = [nombre for nombre, calificacion in estudiantes if calificacion == segundaBaja]
estudiantesSegundaBaja.sort()

for nombre in estudiantesSegundaBaja:
    print(nombre)

# Desarrollado por Gustavo Adolfo Navarro Pacheco T.I 1.127.599.969