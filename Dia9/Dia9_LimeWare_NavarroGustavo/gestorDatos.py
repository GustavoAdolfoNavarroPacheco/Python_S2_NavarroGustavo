import json

def cargarDatos(rutaArchivo):
    try:
        with open(rutaArchivo, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except Exception as e:
        print("❌ Error al cargar el JSON:", e)
        return []
