# 🎵 Sistema de Visualización de Datos de Spotify

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-green)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7%2B-orange)
![Seaborn](https://img.shields.io/badge/Seaborn-0.12%2B-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

Dashboard profesional para análisis y visualización avanzada de datos musicales de Spotify con **Seaborn** y **Matplotlib**.

---

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Instalación](#-instalación)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Uso](#-uso)
- [Gráficos Disponibles](#-gráficos-disponibles)
- [Configuración](#-configuración)
- [Datos](#-datos)
- [Capturas de Pantalla](#-capturas-de-pantalla)
- [Autor](#-autor)

---

## ✨ Características

- 🎨 **10 tipos de visualizaciones profesionales**
- 📊 **Interfaz de menú interactivo**
- 🧹 **Limpieza automática de datos**
- 🎯 **Personalización avanzada de gráficos**
- 💾 **Exportación en alta resolución (PNG + HTML)**
- 📈 **Análisis estadístico integrado**
- 🌈 **Paletas de colores corporativas de Spotify**
- 🔍 **Sistema de logging con colores**

---

## 🚀 Instalación

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

```bash
# 1. Clonar o descargar el proyecto
cd data-visualizacion

# 2. (Opcional) Crear entorno virtual
python -m venv venv

# Activar en Windows
venv\Scripts\activate

# Activar en Linux/Mac
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Verificar instalación
python -c "import pandas, matplotlib, seaborn, plotly; print('✅ Todo listo')"
```

---

## 📁 Estructura del Proyecto

```
data-visualizacion/
│
├── data/                              # 📊 Datos
│   ├── raw/                          # Datos originales
│   │   └── spotify_data.csv
│   └── processed/                    # Datos procesados
│       └── spotify_data_limpio.csv
│
├── src/                              # 🔧 Código fuente
│   ├── config/                       # ⚙️ Configuraciones
│   │   ├── __init__.py
│   │   ├── colors.py                # Paletas de colores
│   │   └── settings.py              # Configuraciones generales
│   │
│   ├── data/                         # 📥 Procesamiento de datos
│   │   ├── __init__.py
│   │   ├── loader.py                # Cargador de datos
│   │   └── cleaner.py               # Limpiador de datos
│   │
│   ├── visualizations/               # 📈 Visualizaciones
│   │   ├── __init__.py
│   │   ├── base.py                  # Clase base
│   │   ├── 01_personalizacion_avanzada.py
│   │   ├── 02_mapa_calor.py
│   │   ├── 03_histogramas.py
│   │   ├── 04_boxplots.py
│   │   ├── 05_kde_densidad.py
│   │   ├── 06_pareto.py
│   │   ├── 07_radar.py
│   │   ├── 08_cascada.py
│   │   ├── 09_enjambre.py
│   │   └── 10_sankey.py
│   │
│   └── utils/                        # 🛠️ Utilidades
│       ├── __init__.py
│       ├── logger.py                # Sistema de logs
│       └── helpers.py               # Funciones auxiliares
│
├── output/                           # 📁 Salida de gráficos
│   ├── images/                      # Imágenes PNG
│   └── interactive/                 # HTML interactivos
│
├── main.py                          # 🚀 Programa principal
├── requirements.txt                 # 📦 Dependencias
└── README.md                        # 📖 Este archivo
```

---

## 💻 Uso

### Ejecución Básica

```bash
python main.py
```

### Menú Interactivo

Al ejecutar, verás un menú como este:

```
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║        🎵 SISTEMA DE VISUALIZACIÓN DE DATOS SPOTIFY      ║
║                                                           ║
║        📊 Análisis Avanzado de Datos Musicales           ║
║        🎨 Visualizaciones Profesionales                  ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝

═══════════════════════════════════════════════════════════
                  🎨 MENÚ DE VISUALIZACIONES
═══════════════════════════════════════════════════════════

📊 GRÁFICOS BÁSICOS:
  1️⃣  Personalización Avanzada (Barras con estilo)
  2️⃣  Mapa de Calor (Correlaciones)

📈 DISTRIBUCIONES:
  3️⃣  Histogramas y Densidad
  4️⃣  Diagramas de Caja y Bigotes
  5️⃣  Gráficos de Densidad KDE

🎯 GRÁFICOS AVANZADOS:
  6️⃣  Gráfico de Pareto (Principio 80/20)
  7️⃣  Gráfico de Radar (Comparación)
  8️⃣  Gráfico de Cascada (Waterfall)
  9️⃣  Gráfico de Enjambre (Swarmplot)

🌊 GRÁFICOS DE FLUJO:
  🔟 Diagrama de Sankey (Flujo de datos)

✨ OPCIONES ESPECIALES:
  11. 🎨 Generar TODOS los gráficos
  12. 📊 Ver resumen de datos
   0. 🚪 Salir

👉 Selecciona una opción:
```

### Uso Programático

También puedes usar los módulos directamente:

```python
from src.data.loader import DataLoader
from src.visualizations import heatmap, histograms

# Cargar datos
loader = DataLoader()
data = loader.load_clean_data()

# Generar gráfico específico
heatmap(data)
histograms(data)
```

---

## 📊 Gráficos Disponibles

### 1️⃣ Personalización Avanzada
**Descripción:** Gráfico de barras horizontales con personalización completa de ejes, colores y etiquetas.

**Datos visualizados:** Top 15 artistas por popularidad

**Cuándo usar:** 
- Presentaciones profesionales
- Reportes ejecutivos
- Destacar datos específicos

```python
from src.visualizations import personalization_advanced
personalization_advanced(data)
```

---

### 2️⃣ Mapa de Calor
**Descripción:** Matriz de correlación entre variables numéricas.

**Datos visualizados:** 
- Popularidad de canciones/artistas
- Seguidores
- Duración
- Tracks por álbum

**Cuándo usar:**
- Análisis exploratorio
- Detectar multicolinealidad
- Identificar variables relacionadas

```python
from src.visualizations import heatmap
heatmap(data)
```

---

### 3️⃣ Histogramas
**Descripción:** Distribución de frecuencias con curvas KDE.

**Datos visualizados:**
- Distribución de popularidad
- Duración por contenido explícito
- Seguidores (escala log)
- Tendencias temporales

**Cuándo usar:**
- Detectar la forma de distribución
- Identificar outliers
- Comparar grupos

```python
from src.visualizations import histograms
histograms(data)
```

---

### 4️⃣ Boxplots (Cajas y Bigotes)
**Descripción:** Visualiza la dispersión y outliers de los datos.

**Datos visualizados:**
- Popularidad por categorías
- Duración por tipo de álbum
- Comparación de artistas

**Cuándo usar:**
- Detectar valores atípicos
- Comparar distribuciones
- Análisis de dispersión

```python
from src.visualizations import boxplots
boxplots(data)
```

---

### 5️⃣ KDE (Densidad Kernel)
**Descripción:** Estimación suave de la distribución de probabilidad.

**Datos visualizados:**
- Densidad univariada
- Densidad bivariada (2D)
- Comparaciones por categorías

**Cuándo usar:**
- Visualizar distribuciones suaves
- Comparar densidades
- Análisis bivariado

```python
from src.visualizations import kde_plots
kde_plots(data)
```

---

### 6️⃣ Pareto (Principio 80/20)
**Descripción:** Gráfico de barras con línea acumulada.

**Datos visualizados:**
- Canciones por artista
- Porcentaje acumulado

**Cuándo usar:**
- Identificar elementos más importantes
- Aplicar principio de Pareto
- Priorización de recursos

```python
from src.visualizations import pareto_chart
pareto_chart(data)
```

---

### 7️⃣ Radar (Comparación Multidimensional)
**Descripción:** Comparación de múltiples métricas simultáneamente.

**Datos visualizados:**
- Top 5 artistas en 5 dimensiones
- Popularidad, seguidores, duración, etc.

**Cuándo usar:**
- Comparar perfiles completos
- Análisis multidimensional
- Benchmarking

```python
from src.visualizations import radar_chart
radar_chart(data)
```

---

### 8️⃣ Cascada (Waterfall)
**Descripción:** Muestra cambios acumulativos a lo largo del tiempo.

**Datos visualizados:**
- Evolución de canciones por año
- Cambios incrementales

**Cuándo usar:**
- Análisis de tendencias temporales
- Visualizar cambios acumulados
- Reportes financieros/temporales

```python
from src.visualizations import waterfall_chart
waterfall_chart(data)
```

---

### 9️⃣ Enjambre (Swarmplot)
**Descripción:** Muestra todos los puntos de datos sin superposición.

**Datos visualizados:**
- Popularidad por contenido explícito
- Duración por tipo de álbum

**Cuándo usar:**
- Datasets pequeños/medianos
- Mostrar distribución completa
- Detectar patrones individuales

```python
from src.visualizations import swarm_plot
swarm_plot(data)
```

---

### 🔟 Sankey (Flujo de Datos)
**Descripción:** Diagrama de flujo interactivo (HTML).

**Datos visualizados:**
- Tipo de álbum → Contenido → Popularidad
- Flujos entre categorías

**Cuándo usar:**
- Visualizar flujos complejos
- Análisis de procesos
- Transiciones entre estados

```python
from src.visualizations import sankey_diagram
sankey_diagram(data)
```

---

## ⚙️ Configuración

### Personalizar Colores

Edita `src/config/colors.py`:

```python
SPOTIFY = {
    'primary': '#1DB954',    # Verde Spotify
    'secondary': '#1ED760',  # Verde claro
    'dark': '#191414',       # Negro
}

CATEGORICAL = [
    '#1DB954',  # Verde
    '#FF6B6B',  # Rojo
    '#4ECDC4',  # Turquesa
    # Agrega más colores...
]
```

### Personalizar Configuraciones

Edita `src/config/settings.py`:

```python
FIGURE_SIZE = (14, 8)      # Tamaño de figura
FIGURE_DPI = 300           # Resolución
FONT_SCALE = 1.2           # Escala de fuente
PLOT_STYLE = 'whitegrid'   # Estilo de seaborn
```

---

## 📂 Datos

### Formato de Datos Requerido

El archivo `spotify_data.csv` debe tener estas columnas:

```csv
track_id,track_name,track_number,track_popularity,explicit,artist_name,artist_popularity,artist_followers,artist_genres,album_id,album_name,album_release_date,album_total_tracks,album_type,track_duration_min
```

### Ubicación de Datos

Coloca tu archivo CSV en:
```
data/raw/spotify_data.csv
```

### Limpieza Automática

El sistema automáticamente:
- ✅ Elimina duplicados
- ✅ Maneja valores faltantes
- ✅ Valida tipos de datos
- ✅ Filtra valores atípicos
- ✅ Guarda datos limpios en `data/processed/`

---

## 🖼️ Capturas de Pantalla

### Menú Principal
```
╔═══════════════════════════════════════════════════════════╗
║        🎵 SISTEMA DE VISUALIZACIÓN DE DATOS SPOTIFY      ║
╚═══════════════════════════════════════════════════════════╝
```

### Ejemplo de Salida
```
ℹ️  [18:07:54] Cargando datos limpios...
✅ [18:07:55] Datos cargados: 8,583 registros
ℹ️  [18:07:56] Generando: Mapa de Calor
✅ [18:07:58] Guardado: 02_mapa_calor.png
```

---

## 🛠️ Solución de Problemas

### Error: No se encuentra el archivo CSV

```bash
FileNotFoundError: spotify_data.csv
```

**Solución:** Coloca tu archivo en `data/raw/spotify_data.csv`

---

### Error: Módulo no encontrado

```bash
ModuleNotFoundError: No module named 'pandas'
```

**Solución:**
```bash
pip install -r requirements.txt
```

---

### Error: Encoding del archivo

```bash
UnicodeDecodeError
```

**Solución:** El sistema detecta automáticamente el encoding. Si persiste, guarda tu CSV como UTF-8.

---

## 📝 Dependencias

```txt
pandas>=2.0.0          # Manipulación de datos
numpy>=1.24.0          # Cálculos numéricos
matplotlib>=3.7.0      # Gráficos base
seaborn>=0.12.0        # Gráficos estadísticos
plotly>=5.14.0         # Gráficos interactivos
kaleido>=0.2.1         # Exportación de Plotly
colorama>=0.4.6        # Colores en terminal
scipy>=1.10.0          # Funciones científicas
```

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/nueva-visualizacion`)
3. Commit tus cambios (`git commit -m 'Añadir nueva visualización'`)
4. Push a la rama (`git push origin feature/nueva-visualizacion`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver archivo `LICENSE` para más detalles.

---

## 👨‍💻 Autores

**Anthony**
- 👤 GitHub: [@AnThony69x](https://github.com/AnThony69x)
- **Emilio**
- 👤 GitHub: [@EmilioSle](https://github.com/EmilioSle)
- 🎓 Universidad: ULEAM (Universidad Laíca de Eloy Alfaro de Manabí)
- 📚 Curso: Visualización de Datos
- 📅 Fecha: Noviembre 23, 2025

---

## 🙏 Agradecimientos

- Seaborn por las visualizaciones estadísticas
- Matplotlib por la base de gráficos
- Plotly por gráficos interactivos
- Spotify por los datos de ejemplo

---

## 📚 Referencias

- [Documentación de Seaborn](https://seaborn.pydata.org/)
- [Documentación de Matplotlib](https://matplotlib.org/)
- [Documentación de Plotly](https://plotly.com/python/)
- [Guía de Visualización de Datos](https://www.data-to-viz.com/)

---

## 🔄 Changelog

### v1.0.0 (2025-11-23)
- ✨ Lanzamiento inicial
- 📊 10 tipos de visualizaciones
- 🎨 Menú interactivo
- 🧹 Sistema de limpieza de datos
- 📝 Sistema de logging

---

## 🚀 Roadmap

- [ ] Agregar más tipos de gráficos
- [ ] Dashboard web con Streamlit
- [ ] Exportación a PDF
- [ ] Análisis predictivo con ML
- [ ] API REST
- [ ] Dockerización

---

<div align="center">

**⭐ Si te gusta este proyecto, dale una estrella ⭐**

Made with ❤️ by Anthony | ULEAM 2025

</div>