import os
import sys

def obtener_ruta_recurso(nombre_archivo):
    #====================================================================
    # Devuelve la ruta correcto de un recurso tanto en modo de desarrollo
    # como en un ejecutable (.exe)
    #====================================================================
    
    if getattr(sys, "frozen",False):
        base_path = sys.MEIPASS

    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
        
    return os.path.join(base_path, nombre_archivo)