import customtkinter as ctk
from constants import (RADIO_PANEL, FUENTE_SUBTITULO)

def crear_panel_ruta(main):
    
    #=============================================================================
    # Se crea un panel o frame y dentro va la ruta de la carpeta que se seleccionó
    #=============================================================================
        
    main.cargar_config()
        
    main.frame_ruta = ctk.CTkFrame(
        main.ventana,
        corner_radius=RADIO_PANEL
        )
    main.frame_ruta.pack(fill="x", padx=20, pady=15)
        
    espacio =ctk.CTkFrame(main.ventana, height=10, fg_color="transparent")
    espacio.pack(fill="x")
        
    main.titulo_ruta = ctk.CTkLabel(
        main.frame_ruta,
        text="Carpeta Seleccionada",
        font=(FUENTE_SUBTITULO)
    )
    main.titulo_ruta.pack(anchor="w", padx=20)
        
    main.ruta_label = ctk.CTkLabel(
        main.frame_ruta,
        text="No hay carpeta seleccionada",
        wraplength=680,
        justify="left"
    )
    main.ruta_label.pack(anchor="w", padx= 15, pady=(0,10))
        
    if main.carpeta_selecc:
        main.ruta_label.configure(text= main.carpeta_selecc) 