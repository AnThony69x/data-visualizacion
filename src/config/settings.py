"""
⚙️ CONFIGURACIÓN GENERAL DEL PROYECTO
====================================
Rutas, configuraciones y mensajes del sistema
"""
from pathlib import Path
import matplotlib.pyplot as plt

# === DIRECTORIOS DEL PROYECTO ===
BASE_DIR = Path(__file__).parent.parent.parent
DATA_DIR = BASE_DIR / 'data'
RAW_DATA_DIR = DATA_DIR / 'raw'
PROCESSED_DATA_DIR = DATA_DIR / 'processed'
OUTPUT_DIR = BASE_DIR / 'output'
IMAGES_DIR = OUTPUT_DIR / 'images'
INTERACTIVE_DIR = OUTPUT_DIR / 'interactive'

# Crear directorios si no existen
for directory in [DATA_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR, 
                  OUTPUT_DIR, IMAGES_DIR, INTERACTIVE_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# === ARCHIVOS DE DATOS ===
RAW_DATA_FILE = RAW_DATA_DIR / 'spotify_data.csv'
CLEAN_DATA_FILE = PROCESSED_DATA_DIR / 'spotify_data_limpio.csv'

# === CONFIGURACIÓN DE VISUALIZACIONES ===
FIGURE_SIZE = (12, 6)        # ← REDUCIDO para pantalla normal
FIGURE_DPI = 100             # ← DPI para pantalla (300 solo para guardar)
SAVE_DPI = 300               # ← DPI alto solo para archivos guardados
FONT_SCALE = 1.0             # ← Reducido de 1.2 a 1.0
PLOT_STYLE = 'whitegrid'

# === CONFIGURACIÓN DE MATPLOTLIB (OPTIMIZADA) ===
MPL_CONFIG = {
    'figure.figsize': FIGURE_SIZE,
    'figure.dpi': FIGURE_DPI,           # ← Para ventana
    'savefig.dpi': SAVE_DPI,            # ← Para archivo guardado
    'savefig.bbox': 'tight',
    'font.size': 10,                    # ← Reducido
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'DejaVu Sans', 'Liberation Sans'],
    'axes.titlesize': 13,               # ← Reducido
    'axes.labelsize': 11,               # ← Reducido
    'axes.unicode_minus': False,
    'xtick.labelsize': 9,               # ← Reducido
    'ytick.labelsize': 9,               # ← Reducido
    'legend.fontsize': 9,               # ← Reducido
    'figure.titlesize': 14,             # ← Reducido
    'figure.autolayout': True,
    'savefig.format': 'png',
    'savefig.pad_inches': 0.2,
    'text.usetex': False,
    
    # === CONFIGURACIÓN DE VENTANA ===
    'figure.max_open_warning': 0,       # No advertir de muchas ventanas
    'figure.constrained_layout.use': True,  # Layout automático mejorado
}

# Aplicar configuración global
plt.rcParams.update(MPL_CONFIG)

# Configurar backend para mejor renderizado
try:
    plt.switch_backend('TkAgg')  # Backend más compatible
except:
    pass

# === MENSAJES DEL SISTEMA ===
MESSAGES = {
    'welcome': """
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║        🎵 SISTEMA DE VISUALIZACIÓN DE DATOS SPOTIFY      ║
║                                                           ║
║        📊 Análisis Avanzado de Datos Musicales           ║
║        🎨 Visualizaciones Profesionales                  ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
    """,
    'processing': '⏳ Procesando datos...',
    'generating': '🎨 Generando visualización...',
    'success': '✅ Gráfico generado exitosamente',
    'error': '❌ Error al generar el gráfico',
    'exit': '\n👋 ¡Gracias por usar el sistema! Hasta pronto.\n'
}