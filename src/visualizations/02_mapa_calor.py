"""
🔥 GRÁFICO 2: MAPA DE CALOR (HEATMAP)
=====================================

📋 DESCRIPCIÓN:
Visualiza la correlación entre variables numéricas usando colores.
Muestra dos versiones: clásica y divergente.

🎯 OBJETIVO:
Identificar relaciones entre variables:
- Correlaciones positivas (verde/rojo)
- Correlaciones negativas (amarillo/azul)
- Detectar variables relacionadas

📊 DATOS QUE VISUALIZA:
- Popularidad de canciones
- Popularidad de artistas
- Seguidores
- Duración de canciones
- Total de tracks en álbum

🎨 ELEMENTOS VISUALES:
- Matriz de correlación con valores
- Colores divergentes centrados en 0
- Anotaciones numéricas
- Dos estilos: RdYlGn y coolwarm

💡 CUÁNDO USAR:
- Para análisis exploratorio de datos
- Detectar multicolinealidad
- Encontrar variables relacionadas
- Análisis de features para ML

Autores: Anthony (@AnThony69x), Emilio (@EmilioSle)
Universidad: ULEAM - Visualización de Datos
Fecha: 2025-11-23
"""

import matplotlib.pyplot as plt
import seaborn as sns
from .base import BasePlot

class MapaCalor(BasePlot):
    
    def __init__(self, data):
        super().__init__(
            data=data,
            title='🔥 Análisis de Correlaciones - Mapa de Calor',
            filename='02_mapa_calor'
        )
    
    def create(self):
        """Crea el mapa de calor"""
        
        # Variables numéricas a correlacionar
        vars_numericas = [
            'track_popularity',      # Popularidad de la canción
            'artist_popularity',     # Popularidad del artista
            'artist_followers',      # Seguidores del artista
            'track_duration_min',    # Duración en minutos
            'album_total_tracks'     # Tracks totales en el álbum
        ]
        
        # Calcular matriz de correlación
        correlacion = self.data[vars_numericas].corr()
        
        # Crear figura con 2 subplots (lado a lado)
        self.fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
        
        # === MAPA DE CALOR 1: ESTILO CLÁSICO ===
        
        sns.heatmap(
            correlacion,
            annot=True,              # Mostrar valores numéricos
            fmt='.2f',               # Formato: 2 decimales
            cmap='RdYlGn',          # Paleta: Rojo-Amarillo-Verde
            center=0,                # Centrar en 0
            square=True,             # Celdas cuadradas
            linewidths=2,            # Grosor de líneas
            cbar_kws={'label': 'Correlación'},  # Etiqueta de barra de color
            ax=ax1,
            vmin=-1,                 # Valor mínimo
            vmax=1                   # Valor máximo
        )
        
        ax1.set_title(
            'Mapa de Calor - Correlaciones\nEstilo Clásico (RdYlGn)',
            fontsize=14,
            fontweight='bold',
            pad=15
        )
        
        # === MAPA DE CALOR 2: ESTILO DIVERGENTE ===
        
        sns.heatmap(
            correlacion,
            annot=True,
            fmt='.2f',
            cmap='coolwarm',         # Paleta: Azul-Blanco-Rojo
            vmin=-1,
            vmax=1,
            center=0,
            square=True,
            linewidths=1,
            cbar_kws={'shrink': 0.8},
            ax=ax2
        )
        
        ax2.set_title(
            'Mapa de Calor - Correlaciones\nEstilo Divergente (Coolwarm)',
            fontsize=14,
            fontweight='bold',
            pad=15
        )
        
        # === INTERPRETACIÓN ===
        
        # Agregar texto explicativo
        interpretacion = (
            "💡 INTERPRETACIÓN:\n"
            "• Verde/Rojo intenso = Correlación fuerte positiva\n"
            "• Amarillo/Blanco = Sin correlación significativa\n"
            "• Valores cercanos a 1 = Relación directa\n"
            "• Valores cercanos a -1 = Relación inversa"
        )
        
        self.fig.text(
            0.5, -0.05,
            interpretacion,
            ha='center',
            fontsize=10,
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        )


def heatmap(data):
    """
    Función helper para generar el mapa de calor
    
    Args:
        data: DataFrame con datos de Spotify
    """
    plot = MapaCalor(data)
    plot.generate()