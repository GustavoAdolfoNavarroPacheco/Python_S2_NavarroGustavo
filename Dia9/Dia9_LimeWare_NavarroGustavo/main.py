from gestorDatos import cargarDatos
from reportes import (
    artistasPorPaisYPeriodo,
    artistasPorGenero,
    artistasUltimos10Años,
    conteoArtistasPorAño,
    unidadesCertificadasPorPaisEn2023
)

artistas = cargarDatos("datos/artistas.json")

print("1. Artistas del Reino Unido entre 1960 y 1970:")
for artista in artistasPorPaisYPeriodo(artistas, "United Kingdom", 1960, 1970):
    print(artista["Artist name"], "-", artista["Release year of first charted record"])

print("2. Artistas del género Rock/pop:")
for artista in artistasPorGenero(artistas, "rock/pop"):
    print(artista["Artist name"], "-", artista["Genre"])

print("3. Artistas de los últimos 10 años:")
for artista in artistasUltimos10Años(artistas):
    print(artista["Artist name"], "-", artista["Release year of first charted record"])

print("4. Conteo de artistas por año:")
conteo = conteoArtistasPorAño(artistas)
for año in sorted(conteo):
    print(año, "→", conteo[año])

print("5. Unidades certificadas por país (según datos):")
ventas = unidadesCertificadasPorPaisEn2023(artistas)
for pais in ventas:
    print(pais, "→", ventas[pais], "unidades")
