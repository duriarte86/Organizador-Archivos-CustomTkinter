import tkinter as tk
import threading
import os
import customtkinter as ctk
import json

from funciones import organizar_los_archivos
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from tkinter import filedialog
from ui import (crear_header, crear_panel_botones, crear_panel_log, crear_panel_progreso, crear_panel_ruta)
from constants import (ALTO_VENTANA,ANCHO_VENTANA, FUENTE_SUBTITULO, RADIO_PANEL, FUENTE_NUMERO)

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class OrganizadorApp:     
    
#=================================================================================================#
#                           CONFIGURACION                                                         #

       
    def guardar_config(self):
        
        """
          Guarda la ultima carpeta que se selecciono
        """
        
        config = {
            "ultima_carpeta": self.carpeta_selecc
        }
        
        try:
            
            ruta_config = os.path.join(os.path.dirname(__file__), "config.json")
            with open(ruta_config, "w", encoding="utf-8") as archivo:
                
                json.dump(
                 config,
                 archivo,
                 indent=4
            )
        except Exception as error:
            
            self.registrar_error(f"No se pudo guardar la configuración\n\n{error}")            
            
    def cargar_config(self):
        
        """
         Carga la ultima carpeta seleccionada
        """
        ruta_config = os.path.join(os.path.dirname(__file__), "config.json")        
        
        if not os.path.exists(ruta_config):
            return
        
        try:
            with open(ruta_config, "r", encoding="utf-8") as archivo:
                config = json.load(archivo)
                         
            self.carpeta_selecc = config.get("ultima_carpeta", "")
        
        except Exception as error:
            
            self.registrar_error(f"No se pudo cargar la configuración\n\n{error}")
    
    def cargar_log(self): 
        
        """
        Carga el contenido del archivo registro.log
        y lo muestra en el log visual.
        """
           
        if not os.path.exists("registro.log"):
           return
       
        try:
            with open("registro.log", "r", encoding="utf-8")as archivo:
                contenido = archivo.read()
       
                self.log_visual.configure(state="normal")    
       
                self.log_visual.insert("end", contenido)
       
                self.log_visual.see("end")
       
                self.log_visual.configure(state="disabled")
            
        except Exception as error:
            
            self.registrar_error(f"No se puede cargar el historial\n\n{error}")
#-------------------------------------------------------------------------------------------------#

#=================================================================================================#
#                                           CONSTRUCTOR                                           #
    
    def __init__(self): 
        
        self.ventana = ctk.CTk()        
        self.ventana.title("Organizador de Archivos v2.0")        
        self.ventana.geometry(f"{ALTO_VENTANA}X{ANCHO_VENTANA}")
        
        crear_header(self)     
        
        self.carpeta_selecc = ""        
        self.estadisticas = {}  
        
        crear_panel_ruta(self) 
        
        crear_panel_progreso(self)
        
        crear_panel_botones(self)
        
        crear_panel_log(self)
        
        self.cargar_log()    
    
#=================================================================================================#
#                                           CREACION DE INTERFAZ                                  #
    
    
            
    
        
           
    
    
#=================================================================================================#
#                                           EVENTOS                                               #   
    
    def seleccionar_carpeta(self):
        carpeta = filedialog.askdirectory()
        
        if carpeta:
            self.carpeta_selecc = carpeta
            
            self.guardar_config()
            
            self.ruta_label.configure(text=carpeta)
            
    def organizar(self):
    #==================================================================================
    # Se lleva a cabo la accion de organizar los archivos
    #=================================================================================
        
        if not self.carpeta_selecc:
            messagebox.showwarning(
                "Atencion",
                "Primero seleccione una carpeta"
            )
            return
            
        self.boton_organizar.configure(state="disabled")
        self.boton_selecc.configure(state="disabled")
        self.boton_limpiar.configure(state="disabled")
        self.boton_exportar.configure(state="disabled")
        self.boton_estadisticas.configure(state="disabled")
            
        hilo = threading.Thread(            
             target=self.ejecutar_org           
        )
            
        hilo.start()                    
        
    def ejecutar_org(self):
    #===================================================================
    #= Llamada a la funcion para organizar los archivos
    #=======================================================================
        
        self.estadisticas={}
        
        try:
            total, errores = organizar_los_archivos(self.carpeta_selecc, self.actualizar_barra)
        
        except Exception as error:
            mensaje_error = f"Error durante la organización:\n\n{error}"
            
            self.ventana.after(0, lambda msg = mensaje_error: self.registrar_error(msg))
            
            total = 0
            errores = mensaje_error
        
        def finalizado():
            if total == 0:
                messagebox.showinfo(
                    "Información", 
                    "No hay archivos que organizar"
                )
            else:
                resumen = ""
                
                for categoria, cantidad in self.estadisticas.items():
                    resumen += f"{categoria}: {cantidad}\n"
                    
                mensaje = (f"Se organizaron {total} archivos correctamente\n\n" f"Resumen:\n\n {resumen}")
                
                if errores:
                    mensaje += ("\nErrores encontrados:\n\n")
                    
                    for error in errores:
                        mensaje += f"- {error}\n"
                
                messagebox.showinfo("Proceso completado", mensaje)
                
                            
            self.boton_organizar.configure(state="normal")            
            self.boton_selecc.configure(state="normal")            
            self.boton_limpiar.configure(state="normal")            
            self.boton_exportar.configure(state="normal")
            self.boton_estadisticas.configure(state="normal")
            
            self.archivo_label.configure(text="Proceso Terminado")
            
        self.ventana.after(0, finalizado)
#=================================================================================================#
#                                           UTILIDADES                                            #     
    def actualizar_barra(
        self, 
        valor,
        actual = None,
        total = None,
        archivo = None,
        destino = None,
        categoria =None,
        exito = True
        ):
        
        self.barra.set(valor / 100)
                
        self.porcentaje_label.configure(
            text=f"{valor}%"
        )
        
        if archivo:
            self.archivo_label.configure(
                text=f"Archivo: {archivo}"
            )
        
        if actual is not None and total is not None:
            self.progreso_label.configure(
                text=f"Procesando: {actual} / {total}"
            )
            
        if archivo and destino:
            
            fecha_hora = datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            )
            nombre_archivo = os.path.basename(archivo)
            
            if exito:
                
                mensaje = (
                    f"[{fecha_hora}]"
                    f"MOVIDO | "
                    f"ARCHIVO: {nombre_archivo} | "
                    f"CATEGORIA: {categoria} | "
                    f"DESTINO: {destino}"
                )
                
            else:
                mensaje = (
                f"[{fecha_hora}] "
                f"ERROR | "
                f"ARCHIVO: {nombre_archivo} | "
                f"DESTINO: {destino}"
            )
                
            self.agregar_log(mensaje)
            
        if categoria and exito:
                     
            if categoria not in self.estadisticas:
            
                self.estadisticas[categoria]= 0
            
            self.estadisticas[categoria] += 1
        
        self.ventana.update_idletasks()
    
    def agregar_log(self, texto):
        
        self.log_visual.configure(state="normal")
        
        self.log_visual.insert(
            "end",
            texto + "\n"
        )
        
        self.log_visual.see("end")
        
        self.log_visual.configure(
            state="disabled"
        )
        
        with open ("registro.log", "a", encoding="utf-8") as archivo:
            archivo.write(texto + "\n")
    
    def registrar_error(self, mensaje):
    #=========================================================================
    # Registrar los errores que ocurran
    #=========================================================================
    
        fecha_hora = datetime.now().strftime("%d/%m/%y  %H: %M:%S")
        
        texto = f"[{fecha_hora}] ERROR: {mensaje}"
        
        with open("registro.log","a", encoding="utf-8") as archivo:
            archivo.write(texto + "\n")
            
        messagebox.showerror("Error", mensaje)
#=================================================================================================#
#                                           ESTADISTICAS                                          #
    def mostrar_estadisticas(self):
    #====================================================================================
    # Muestra en una ventana aparte un resumen por categorias de la cantidad de archivos que se movieron
    #====================================================================================
        
        if not self.estadisticas:
            messagebox.showinfo(
                "Estadísticas",
                "Todavía no hay datos para mostrar."
            )
            return
        
        #Crear la ventana de estadisticas
        ventana_stats = ctk.CTkToplevel(self.ventana)
        ventana_stats.title("📊 Estadísticas de Organización")
        ventana_stats.geometry("420x420")
        
        #Crear la tabla para mostrar los datos
        frame_stats = ctk.CTkFrame(
            ventana_stats,
            corner_radius=RADIO_PANEL
        )
        frame_stats.pack(fill="both", expand=True, padx=20, pady=20)
        
        #Crear el titulo
        titulo = ctk.CTkLabel(
            frame_stats,
            text=("📊 Estadísticas de Organización"),
            font=FUENTE_SUBTITULO
        )
        titulo.pack(pady=(15,20))
        
        encabezado = ctk.CTkFrame(
            frame_stats,
            fg_color="transparent"
        )
        encabezado.pack(fill="x", padx=20)
        
        ctk.CTkLabel(
            encabezado,
            text="Categoría",
            font=FUENTE_SUBTITULO
        ).pack(side="left")
        
        ctk.CTkLabel(
            encabezado,
            text="Total",
            font=FUENTE_SUBTITULO
        ).pack(side="right")
        
        total_general = 0
        
        iconos = {
            "PDF": "📄",
            "IMAGEN": "🖼️",
            "DOCUMENTO": "📝",
            "EXCEL": "📊",
            "ZIP": "🗜️",
            "TXT": "📃"
        }
        
        for categoria, cantidad in self.estadisticas.items():
            fila = ctk.CTkFrame(
                frame_stats,
                fg_color="transparent",
            )
            fila.pack(fill="x", padx=20, pady=3)
            
            icono = iconos.get(categoria, "📁")
            
            ctk.CTkLabel(
                fila,               
                text=f"{icono} {categoria}",
                font=FUENTE_NUMERO
            ).pack(side="left")  
            
            ctk.CTkLabel(
                fila,
                text=str(cantidad)
            ).pack(side="right")   
            
            total_general += cantidad        
            
        ctk.CTkLabel(
            frame_stats,
            text="--------------------------------------------------------------",
            font=FUENTE_SUBTITULO
        ).pack(pady=10)
        
        ctk.CTkLabel(
            frame_stats,
            text=f"TOTAL: {total_general}",
            font=FUENTE_SUBTITULO
        ).pack(pady=(0,15))
#=================================================================================================#
#                                           INICIO                                                #          
    def ejecutar(self):
        self.ventana.mainloop()
#=================================================================================================#
#                                           LIMPIAR Y EXPORTAR                                    #         
    def limpiar_log(self):
    #====================================================================================
    #Limpia el registro o archivo log que se creo
    #====================================================================================
        
        respuesta = messagebox.askyesno(
            "Limpiar Log",
            "Desea borrar todo el historial del Log?"
        )
        
        if respuesta:
            
            #Limpiar pantalla
            self.log_visual.configure(state="normal")
        
            self.log_visual.delete("1.0", "end")
        
            self.log_visual.configure(state="disabled")
            
            #Limpiar archivo permanente
            if os.path.exists("registro.log"):
                
                with open("registro.log", "w", encoding="utf-8") as archivo:
                    archivo.write("")
            messagebox.showinfo("Log", "Historial eliminado correctamente")
        
    def exportar_log(self):
    #====================================================================================
    #Se crean un registro tipo log con todos los detalles de los movimientos
    #====================================================================================
        
        self.log_visual.configure(state="normal")
        
        contenido = self.log_visual.get("1.0", "end")
        
        self.log_visual.configure(state="disabled")
        
        try:
            with open("registro.txt", "w", encoding="utf-8") as archivo:
                archivo.write(contenido)
            
            messagebox.showinfo("Exportación", "Log exportado correctamente")  
        
        except Exception as error:
            
            self.registrar_error(f"No se pudo exportar el log.\n\n{error}")            
        
app = OrganizadorApp()
app.ejecutar()