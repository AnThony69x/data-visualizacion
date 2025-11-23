"""
📦 GRÁFICO 4: DIAGRAMAS DE CAJA Y BIGOTES (BOXPLOTS)
===================================================

📋 DESCRIPCIÓN:
Visualiza la distribución, mediana, cuartiles y outliers de los datos.
Incluye 4 variaciones: básico, por categoría, violinplot y por tipo de álbum.

🎯 OBJETIVO:
Analizar la dispersión y detectar valores atípicos:
- Visualizar la mediana y cuartiles (Q1, Q3)
- Identificar outliers (valores extremos)
- Comparar distribuciones entre grupos
- Detectar asimetría en los datos

📊 DATOS QUE VISUALIZA:
1. Distribución general de popularidad
2. Popularidad por contenido explícito
3. Popularidad por artista (Top 10)
4. Duración por tipo de álbum

🎨 ELEMENTOS VISUALES:
- Boxplot simple
- Boxplot por categorías
- Violinplot con boxplot interno
- Comparación horizontal

💡 CUÁNDO USAR:
- Detectar outliers y valores atípicos
- Comparar distribuciones entre grupos
- Análisis de dispersión de datos
- Identificar asimetría (skewness)

Autores: Anthony (@AnThony69x), Emilio (@EmilioSle)
Universidad: ULEAM - Visualización de Datos
Fecha: 2025-11-23
"""

import matplotlib.pyplot as plt
import seaborn as sns
from .base import BasePlot
from ..config.colors import SPOTIFY, EXPLICIT

class Boxplots(BasePlot):
    
    def __init__(self, data):
        super().__init__(
            data=data,
            title='📦 Análisis de Dispersión - Diagramas de Caja y Bigotes',
            filename='04_boxplots'
        )
    
    def create(self):
        """Crea los boxplots"""
        
        # Crear figura con 4 subplots (2x2)
        self.fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        
        # === BOXPLOT 1: DISTRIBUCIÓN BÁSICA ===
        
        sns.boxplot(
            data=self.data, 
            y='track_popularity', 
            color=SPOTIFY['primary'], 
            ax=axes[0, 0],
            width=0.5
        )
        
        axes[0, 0].set_title(
            'Distribución de Popularidad de Canciones',
            fontsize=12,
            fontweight='bold'
        )
        axes[0, 0].set_ylabel('Popularidad (0-100)')
        axes[0, 0].set_xlabel('')
        
        # Agregar líneas de referencia
        median = self.data['track_popularity'].median()
        axes[0, 0].axhline(median, color='red', linestyle='--', 
                          linewidth=1, alpha=0.5, label=f'Mediana: {median:.1f}')
        axes[0, 0].legend()
        
        # === BOXPLOT 2: POR CONTENIDO EXPLÍCITO ===
        
        sns.boxplot(
            data=self.data, 
            x='explicit', 
            y='track_popularity',
            palette=[EXPLICIT[False], EXPLICIT[True]], 
            ax=axes[0, 1]
        )
        
        axes[0, 1].set_title(
            'Popularidad por Contenido Explícito',
            fontsize=12,
            fontweight='bold'
        )
        axes[0, 1].set_xticklabels(['No Explícito', 'Explícito'])
        axes[0, 1].set_xlabel('Tipo de Contenido')
        axes[0, 1].set_ylabel('Popularidad')
        
        # === BOXPLOT 3: VIOLINPLOT + BOXPLOT (Top 10 artistas) ===
        
        # Obtener top 10 artistas con más canciones
        top_10_artists = self.data['artist_name'].value_counts().head(10).index
        df_top_artists = self.data[self.data['artist_name'].isin(top_10_artists)]
        
        if len(df_top_artists) > 0:
            sns.violinplot(
                data=df_top_artists, 
                y='artist_name', 
                x='track_popularity',
                palette='muted', 
                ax=axes[1, 0], 
                inner='box'  # Mostrar boxplot dentro del violín
            )
            
            axes[1, 0].set_title(
                'Popularidad por Artista (Top 10)',
                fontsize=12,
                fontweight='bold'
            )
            axes[1, 0].set_ylabel('Artista')
            axes[1, 0].set_xlabel('Popularidad')
        
        # === BOXPLOT 4: POR TIPO DE ÁLBUM ===
        
        # Filtrar tipos de álbum más comunes
        top_album_types = self.data['album_type'].value_counts().head(3).index
        df_album_types = self.data[self.data['album_type'].isin(top_album_types)]
        
        if len(df_album_types) > 0:
            sns.boxplot(
                data=df_album_types, 
                x='album_type', 
                y='track_duration_min',
                palette='Set2', 
                ax=axes[1, 1]
            )
            
            axes[1, 1].set_title(
                'Duración por Tipo de Álbum',
                fontsize=12,
                fontweight='bold'
            )
            axes[1, 1].set_xlabel('Tipo de Álbum')
            axes[1, 1].set_ylabel('Duración (minutos)')
            axes[1, 1].tick_params(axis='x', rotation=45)
        
        # === AÑADIR GRID ===
        
        for ax in axes.flat:
            ax.grid(axis='y', alpha=0.3, linestyle='--')


def boxplots(data):
    """
    Función helper para generar boxplots
    
    Args:
        data: DataFrame con datos de Spotify
    """
    plot = Boxplots(data)
    plot.generate()