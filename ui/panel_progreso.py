import customtkinter as ctk
from constants import (COLOR_PRIMARIO, RADIO_PANEL, FUENTE_SUBTITULO)


def crear_panel_progreso(main):
    #====================================================================================
    #Se crean y oranizan todo lo que tiene q ver con el progreso ejemplo la barra de progreso
    #====================================================================================
        
        main.frame_progreso = ctk.CTkFrame(
            main.ventana,
            corner_radius=RADIO_PANEL
        )        
       
        main.frame_progreso.grid_columnconfigure(0, weight=1)        
        
        main.titulo_progreso = ctk.CTkLabel(
            main.frame_progreso,
            text="Progreso",
            font=FUENTE_SUBTITULO
        )        
        main.titulo_progreso.grid(row=0, column=0, padx=20, sticky="ew")
        
        main.barra = ctk.CTkProgressBar(
            main.frame_progreso,
            width=500,
            height=20,
            progress_color=COLOR_PRIMARIO,
            fg_color=COLOR_PRIMARIO,
            border_width=1,
            corner_radius=RADIO_PANEL
            
        )
        main.barra.grid(row=1, column=0,padx= 20, sticky= "ew")
        main.barra.set(0)
        
        
        main.porcentaje_label = ctk.CTkLabel(
            main.frame_progreso,
            text="0%"
        )
        main.porcentaje_label.grid(row=2, column=0, pady= 5)
        
        main.archivo_label = ctk.CTkLabel(
            main.frame_progreso,
            text="Esperando...."
        )
        main.archivo_label.grid(row=3, column=0, pady= 5)
        
        main.progreso_label = ctk.CTkLabel(
            main.frame_progreso,
            text="Procesando: 0 / 0 archivos"
        )
        main.progreso_label.grid(row=4, column=0, pady= (0,10))