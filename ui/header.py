import customtkinter as ctk
from constants import (COLOR_HEADER, FUENTE_TITULO)


def crear_header(main):
    # ===================================================================
    # Crea el encabezado principal de la aplicacion
    # ===================================================================   
        
        main.header = ctk.CTkFrame(
        main.ventana,
        fg_color=COLOR_HEADER,
        height=80,
        corner_radius=0
        )
        main.header.pack(fill="x")
        main.header.pack_propagate(False)
        
        main.titulo = ctk.CTkLabel(
            main.header,
            text="Organizador de Archivos v2.1",
            font=FUENTE_TITULO,
            text_color="white"
            
        )    
        main.titulo.pack(expand=True)    