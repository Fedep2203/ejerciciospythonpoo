import json
from pathlib import Path
from models.lista import Lista

class ObjectEncoder:
    def guardar_json(self, archivo: str, diccionario: dict):
        with Path(archivo).open('w', encoding='utf-8') as destino:
            json.dump(diccionario, destino, indent = 4)