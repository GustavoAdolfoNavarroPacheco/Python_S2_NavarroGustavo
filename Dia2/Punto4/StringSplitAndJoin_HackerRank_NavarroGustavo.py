# Entrada: Texto ingresado por el usuario
# Salida: Texto ingresado por el usuario pero separado por una linea(-)

def split_and_join(line):
    palabras = line.split(" ")
    resultado = "-".join(palabras) 
    return resultado

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# Desarrollado por Gustavo Adolfo Navarro Pacheco T.I 1.127.599.969