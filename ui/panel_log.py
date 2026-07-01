import customtkinter as ctk
from constants import(RADIO_PANEL, FUENTE_SUBTITULO)

def crear_panel_log(main):
    #====================================================================================
    #Se crean y se muestra en forma de texto el resultado de los movimientos y/o errores que ocurran
    #====================================================================================
        main.frame_log = ctk.CTkFrame(
            main.ventana,
            corner_radius=RADIO_PANEL           
        )
        main.frame_log.pack(
            
            fill="both",
            expand = True,
            padx=20,
            pady=15
        )
        main.titulo_log = ctk.CTkLabel(
            main.frame_log,
            text="Registro de actividad",
            font=(FUENTE_SUBTITULO)
        )
        main.titulo_log.pack(pady=(10,5))
        
        main.log_visual = ctk.CTkTextbox(
            main.frame_log,
            width=650,
            height=250,
            corner_radius=RADIO_PANEL          
        )
        main.log_visual.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )
        
        main.log_visual.configure(state="disabled")