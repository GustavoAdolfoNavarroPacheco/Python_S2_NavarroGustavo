# Entrada: Primer Nombre y primer apellido ingresado por el usuario
# Salida: Primer nombre y apellido agregandole: (Hello! You just delved into python)

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

# Desarrollado por Gustavo Adolfo Navarro Pacheco T.I 1.127.599.969