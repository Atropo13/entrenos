

from collections import namedtuple
from datetime import datetime
import csv
Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')
def formatear_fechas(cadena):
    return datetime.strptime(cadena, "%d/%m/%Y %H:%M")
def formatear_bool(cadena):
    if cadena == "S":
     return True
    else:
        return False
def lee_entrenos(ruta):
    with open(ruta, encoding = 'utf-8') as f:
     resultado = [ ]
     lector = csv.reader(f)
     for campos in lector:
        registro = Entreno(campos[0],
                           formatear_fechas(campos[1]),
                             campos[2],
                              int(campos[3]),
                            int(campos[4]),
                            float(campos[5]),
                             int(campos[6]),
                            formatear_bool(campos[7]))
        resultado.append(registro)
    return resultado
def tipos_entreno(entrenos):
   pass


entreno1 = ("Correr","2/11/2021 9:16","Córdoba","32","261","19.68","96","N")
entrenostipos = Entreno("Correr",
                 formatear_fechas("2/11/2021 9:16"),
                 "Córdoba",
                 int("32"),
                 int("261"),
                 float("19.68"),
                 int("96"),
                 formatear_bool("N"))
print(entrenostipos)
print(formatear_fechas("2/11/2021 9:16"))