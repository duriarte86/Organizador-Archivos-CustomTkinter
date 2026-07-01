#  📂 Organizador de archivos v2.1
Aplicación de escritorio desarrollada en **Python** y **CustomTkinter** que organiza automáticamente archivos en carpetas según su tipo.

---
## 📌 Descripción

Este proyecto organiza automáticamente los archivos de una carpeta según su extensión.

Las categorías son configurables mediante un archivo JSON, permitiendo clasificar documentos, imágenes, archivos comprimidos, hojas de cálculo, archivos de texto y otros formatos.

El proyecto fue desarrollado con el objetivo de aprender Python, Programación Orientada a Objetos, arquitectura de software, interfaces gráficas modernas con CustomTkinter y buenas prácticas de desarrollo.

---

## ✨ Características

- ✅ Organización automática de archivos.
- ✅ Clasificación por categorías configurables.
- ✅ Creación automática de carpetas.
- ✅ Barra de progreso en tiempo real.
- ✅ Registro de movimientos.
- ✅ Registro de errores.
- ✅ Exportación del historial.
- ✅ Estadísticas de organización.
- ✅ Interfaz moderna con CustomTkinter.
- ✅ Arquitectura modular.

---

## 🛠 Tecnologías utilizadas

| Tecnología | Uso |
|------------|-----|
| Python 3.12 | Lenguaje principal |
| CustomTkinter | Interfaz gráfica moderna |
| Tkinter | Componentes adicionales |
| JSON | Configuración de categorías |
| Threading | Procesamiento en segundo plano |
| Pillow | Manejo de imágenes e iconos |

Organizador_Archivos_v2_CustomUI/
│
├── main.py
├── funciones.py
├── constants.py
├── README.md
├── requirements.txt
│
├── ui/
│   ├── __init__.py
│   ├── header.py
│   ├── panel_ruta.py
│   ├── panel_progreso.py
│   ├── panel_botones.py
│   └── panel_log.py
│
├── assets/
│   └── icono.ico
│
├── config.json
├── config_categorias.json
└── registro.log
```

---

# ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/Organizador_Archivos_v2_CustomUI.git
```

### 2. Entrar al proyecto

```bash
cd Organizador_Archivos_v2_CustomUI
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación

```bash
python main.py
```
---

# 📖 Uso

1. Presiona **📂 Seleccionar** para elegir una carpeta.
2. Haz clic en **▶ Organizar Archivos**.
3. Espera a que finalice el proceso.
4. Consulta el **Registro de actividad**.
5. Revisa las **📊 Estadísticas** para conocer el resumen de la organización.

---

# 📷 Capturas de pantalla

## Ventana principal

*(Pendiente de agregar imagen)*

## Ventana de estadísticas

*(Pendiente de agregar imagen)*

---

# 🚀 Próximas mejoras

- 🌙 Implementar modo claro y modo oscuro.
- 🖱️ Agregar soporte para arrastrar y soltar carpetas (Drag & Drop).
- ⚙️ Configuración avanzada desde la interfaz.
- 📂 Mayor cantidad de categorías de archivos.
- 🔍 Búsqueda dentro del registro de actividad.
- 🌐 Soporte para múltiples idiomas.

---

# 👨‍💻 Autor

**Dayron Uriarte Agüero**

Ingeniero en Ciencias Informáticas.

Proyecto desarrollado como parte de mi proceso de aprendizaje en Python, Programación Orientada a Objetos, arquitectura de software y desarrollo de aplicaciones de escritorio con CustomTkinter.

---

# 📜 Licencia

Este proyecto fue desarrollado con fines educativos y de aprendizaje.

Su código puede utilizarse como referencia para estudiar Python, CustomTkinter y buenas prácticas de desarrollo de software.

---

# ⭐ Estado del proyecto

**Versión:** 2.1.0

✅ Proyecto estable.

Actualmente todas las funcionalidades principales se encuentran implementadas y el proyecto continúa evolucionando mediante mejoras en la interfaz y la experiencia del usuario.

Poryecto desarrollado por Dayron Uriarte Aguero
Probando los branches 