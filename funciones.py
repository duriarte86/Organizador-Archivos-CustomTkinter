from datetime import datetime
from utils import obtener_ruta_recurso

import os
import shutil
from tkinter import filedialog
import json

        
#Registro de los eventos del proceso               
def registrar_evento(log, tipo, mensaje):
    
    """
     Registra el evento ocurrido y lo escribe en el log
    """    
    
    with open(log, "a", encoding="utf-8") as archivo_log:
        fecha = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
        
        archivo_log.write(f"[{fecha}] {tipo} | {mensaje}\n")    

def mover_archivo(ruta_archivo, destino, archivo):
    
    """
    Mueve un archivo a la carpeta destino.
    Devuelve (True, None) si tuvo éxito o
    (False, mensaje_error) si ocurre un problema.
    """
    
    try:
        if ruta_archivo.endswith("error.pdf"):
            raise Exception("Error de prueba")
        
        shutil.move(ruta_archivo, os.path.join(destino, archivo))
        return True, None
    
    except Exception as error:
        
        mensaje = f"{archivo}: {error}"
        
        
        return False, mensaje
    
def obtener_nombre_unico(destino, nombre_archivo):
    nombre, extension = os.path.splitext(nombre_archivo)
   
    contador = 1
    nuevo_nombre = nombre_archivo
    
    while os.path.exists(os.path.join(destino, nuevo_nombre)):
        nuevo_nombre = (f"{nombre}_{contador}{extension}")
        contador += 1
       
    return nuevo_nombre

def cargar_categorias():
    """
     Lee el archivo config_categorias.json 
     y devuelve las categorias disponibles
    """
    
    ruta_config =obtener_ruta_recurso("config_categorias.json")    
        
    try:
        with open(ruta_config, "r", encoding="utf-8") as archivo:
            categorias = json.load(archivo)
        return categorias
    
    except FileNotFoundError:
        print("No se encontro el archivo config_categorias,json")
        return{}
    
    except json.JSONDecodeError:
        print("Error: el archivo config_categorias.json no tiene formato válido")
        return{}
    
def organizar_los_archivos(ruta, actualizar_progreso = None):
    
    #Cargar categrias desde el archivo json a traves de la funcion cargar_categorias   
    
    categorias = cargar_categorias()
    
    for nombre_carpeta, _ in categorias.values():
        os.makedirs(
            os.path.join(ruta, nombre_carpeta),
            exist_ok=True
        )

    #Creando archivo log.txt
    log = os.path.join(ruta, "registro.log")
    
    registrar_evento(log, "INFO","Inicio de organizacion")
    
    #Archivos que el organizador no debe tocar:
    archivos_excluir = (
        "registro.log", 
        "registro.txt", 
        "log.txt"
    )
    
    #Extensiones permitidas obtenidas del dicionario
    extensiones_validas = categorias.keys()
    
    
    #Recorriendo archvivos
    archivos_validos = []
    
    for a in os.listdir(ruta):
        ruta_a = os.path.join(ruta, a)
        
        extension = os.path.splitext(a)[1].lower()
        
        if os.path.isfile(ruta_a) and a.lower() not in archivos_excluir:
            
            if extension in extensiones_validas:
                archivos_validos.append(a)
        
    total_de_archivos = len(archivos_validos)
    
    procesados = 0
    total = 0 
    errores = []
    
    if total_de_archivos == 0:
        return 0, []
    
    for archivo in archivos_validos:
        
        ruta_archivo = os.path.join(ruta, archivo)    
        
        extension = os.path.splitext(archivo)[1].lower()
        
        datos = categorias[extension]
        nombre_carpeta = datos["carpeta"]
        categoria = datos["categoria"]        
        
        destino = os.path.join(ruta, nombre_carpeta)
        
        nombre_final = obtener_nombre_unico(destino, archivo)
        
        resultado, mensaje_error = mover_archivo(ruta_archivo, destino, nombre_final)
        
        if resultado:
            #registrar_mov(log, archivo, nombre_carpeta)
            registrar_evento(log, "MOVIDO", f"{archivo} --> {nombre_carpeta}")
            
            total += 1
            movido = True
            
        else:
            errores.append(mensaje_error)
            
            #registrar_error(log, mensaje_error)
            registrar_evento(log, "ERROR", mensaje_error)
            
            movido = False
            
        procesados += 1
        
        
        if actualizar_progreso:
            porcentaje =  int(procesados / total_de_archivos * 100)
            
            actualizar_progreso(porcentaje, procesados, total_de_archivos, archivo, nombre_carpeta, categoria, movido)
            
    print(f"Se organizaron {total} archivos")
    
    if errores:
        print("\nErrores encontrados:")
        
        for error in errores:
            print(error)
    
    registrar_evento(log, "INFO", f"Proceso terminado. Organizados: {total}. Errores: {len(errores)}")        
    
    return total, errores    