# Entrada: El Usuario ingresa un texto, el usuario ingresa dos valores en la segunda línea un índice (un numero)  y un caracter (una letra o símbolo)
# Salida: Texto modificada donde el caracter en la posición especificada ha sido reemplazado por el nuevo caracter

def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# Desarrollado por Gustavo Adolfo Navarro Pacheco T.I 1.127.599.969