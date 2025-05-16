import re
from datetime import datetime

def limpiarAños(actividad):
    actividad = actividad.replace("\\u2013", "-").replace("–", "-")
    partes = actividad.split("-")
    try:
        inicio = int(partes[0])
        fin = int(partes[1]) if len(partes) > 1 and partes[1].isdigit() else datetime.now().year
        return inicio, fin
    except:
        return None, None

def normalizarGenero(texto):
    return texto.replace("\\/", "/").lower()

def ventasPorPais(texto):
    ventas = {}
    matches = re.findall(r'([A-Z]{2,3}):\s*([\d.,]+)', texto)
    for pais, cantidad in matches:
        try:
            ventas[pais] = float(cantidad.replace(",", ""))
        except:
            continue
    return ventas

def artistasPorPaisYPeriodo(artistas, paisBuscado, desde, hasta):
    resultado = []
    for artista in artistas:
        if artista.get("Country", "").lower() == paisBuscado.lower():
            año = artista.get("Release year of first charted record", 0)
            if desde <= año <= hasta:
                resultado.append(artista)
    return resultado

def artistasPorGenero(artistas, generoBuscado):
    resultado = []
    for artista in artistas:
        if generoBuscado.lower() in normalizarGenero(artista.get("Genre", "")):
            resultado.append(artista)
    return resultado

def artistasUltimos10Años(artistas):
    actual = datetime.now().year
    resultado = []
    for artista in artistas:
        if artista.get("Release year of first charted record", 0) >= (actual - 10):
            resultado.append(artista)
    return resultado

def conteoArtistasPorAño(artistas):
    conteo = {}
    for artista in artistas:
        año = artista.get("Release year of first charted record", 0)
        if año:
            conteo[año] = conteo.get(año, 0) + 1
    return conteo

def unidadesCertificadasPorPaisEn2023(artistas):
    resumen = {}
    for artista in artistas:
        ventasTexto = artista.get("Total certified units", "")
        ventas = ventasPorPais(ventasTexto)
        for pais, cantidad in ventas.items():
            resumen[pais] = resumen.get(pais, 0) + cantidad
    return resumen
