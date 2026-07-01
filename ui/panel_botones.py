import customtkinter as ctk
from constants import(RADIO_BUTTON, COLOR_HEADER, ANCHO_BOTON, ALTO_BOTON)

def crear_panel_botones(main):
    #====================================================================================
    #Crea el panel que contiene todos los botones principales de la aplicación.
    #====================================================================================
        main.frame_botones = ctk.CTkFrame(main.ventana, fg_color="transparent")
        main.frame_botones.pack(pady=15)
        main.frame_botones.grid_columnconfigure(0, weight=1)
        main.frame_botones.grid_columnconfigure(1, weight=1)
        
        main.boton_selecc = ctk.CTkButton(
            main.frame_botones,
            text="📂 Seleccionar",
            height=ALTO_BOTON,
            width=ANCHO_BOTON,
            corner_radius=RADIO_BUTTON,
            command=main.seleccionar_carpeta
        )
        main.boton_selecc.grid(row=0, column=0, padx=10, pady=8)
        
        main.boton_organizar = ctk.CTkButton(
            main.frame_botones,
            text="▶ Organizar",
            width=ANCHO_BOTON,
            height=ALTO_BOTON,
            corner_radius=RADIO_BUTTON,
            fg_color=COLOR_HEADER,
            command=main.organizar
        )
        main.boton_organizar.grid(row=0, column=1, padx=10, pady=8)
        
        main.boton_limpiar = ctk.CTkButton(
            main.frame_botones,
            text="🗑 Limpiar Log",
            height=ALTO_BOTON,
            width=ANCHO_BOTON,
            corner_radius=RADIO_BUTTON,
            command=main.limpiar_log
        )
        main.boton_limpiar.grid(row=2, column=0, columnspan=2, pady=(15,5))
        
        main.boton_exportar = ctk.CTkButton(
            main.frame_botones, 
            text="📝 Exportar Log",
            height=ALTO_BOTON,
            width=ANCHO_BOTON,
            corner_radius=RADIO_BUTTON,
            command=main.exportar_log
        )
        main.boton_exportar.grid(row=1, column=0, padx=10, pady=8)
        
        main.boton_estadisticas = ctk.CTkButton(
            main.frame_botones,
            text="📊 Estadísticas",
            height=ALTO_BOTON,
            width=ANCHO_BOTON,
            corner_radius=RADIO_BUTTON,
            command=main.mostrar_estadisticas
        )
        main.boton_estadisticas.grid(row=1, column=1, padx=10, pady=8) 