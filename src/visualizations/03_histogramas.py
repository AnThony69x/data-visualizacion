"""
📊 GRÁFICO 3: HISTOGRAMAS Y DISTRIBUCIONES
=========================================

📋 DESCRIPCIÓN:
Muestra la distribución de frecuencias de variables continuas.
Incluye 4 variaciones: básico, comparativo, logarítmico y temporal.

🎯 OBJETIVO:
Entender la distribución de los datos:
- Detectar la forma de la distribución (normal, sesgada, etc.)
- Identificar outliers
- Comparar distribuciones entre grupos
- Visualizar tendencias temporales

📊 DATOS QUE VISUALIZA:
1. Distribución de popularidad de canciones
2. Duración: explícitas vs no explícitas
3. Distribución de seguidores (escala logarítmica)
4. Canciones por año (desde 2020)

🎨 ELEMENTOS VISUALES:
- Histograma con curva KDE superpuesta
- Histogramas apilados por categoría
- Rugplot (alfombra de puntos)
- Escala logarítmica

💡 CUÁNDO USAR:
- Análisis exploratorio inicial
- Detectar valores atípicos
- Comparar distribuciones entre grupos
- Verificar normalidad de datos

Autores: Anthony (@AnThony69x), Emilio (@EmilioSle)
Universidad: ULEAM - Visualización de Datos
Fecha: 2025-11-23
"""

import matplotlib.pyplot as plt
import seaborn as sns
from .base import BasePlot
from ..config.colors import SPOTIFY, EXPLICIT

class Histogramas(BasePlot):
    
    def __init__(self, data):
        super().__init__(
            data=data,
            title='📊 Análisis de Distribuciones - Histogramas',
            filename='03_histogramas'
        )
    
    def create(self):
        """Crea los histogramas"""
        
        # Crear figura con 4 subplots (2x2)
        self.fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        
        # === HISTOGRAMA 1: POPULARIDAD (básico con KDE) ===
        
        sns.histplot(
            data=self.data,
            x='track_popularity',
            bins=30,                 # 30 barras
            kde=True,                # Curva de densidad superpuesta
            color=SPOTIFY['primary'],
            ax=axes[0, 0],
            edgecolor='black',       # Borde negro en barras
            stat='count'             # Mostrar conteo
        )
        
        axes[0, 0].set_title(
            'Distribución de Popularidad de Canciones',
            fontsize=12,
            fontweight='bold'
        )
        axes[0, 0].set_xlabel('Popularidad (0-100)')
        axes[0, 0].set_ylabel('Frecuencia (número de canciones)')
        
        # Línea vertical en la media
        media = self.data['track_popularity'].mean()
        axes[0, 0].axvline(
            media,
            color='red',
            linestyle='--',
            linewidth=2,
            label=f'Media: {media:.1f}'
        )
        axes[0, 0].legend()
        
        # === HISTOGRAMA 2: DURACIÓN (comparativo) ===
        
        sns.histplot(
            data=self.data,
            x='track_duration_min',
            hue='explicit',          # Separar por explícito/no explícito
            bins=30,
            kde=True,
            palette=[EXPLICIT[False], EXPLICIT[True]],
            ax=axes[0, 1],
            multiple='layer',        # Superponer capas
            alpha=0.6               # Transparencia
        )
        
        axes[0, 1].set_title(
            'Duración: Explícito vs No Explícito',
            fontsize=12,
            fontweight='bold'
        )
        axes[0, 1].set_xlabel('Duración (minutos)')
        axes[0, 1].set_ylabel('Frecuencia')
        axes[0, 1].legend(title='Contenido', labels=['No Explícito', 'Explícito'])
        
        # === HISTOGRAMA 3: SEGUIDORES (logarítmico con rugplot) ===
        
        # Tomar muestra para rugplot (puntos en el eje)
        sample = self.data.sample(min(500, len(self.data)))
        
        sns.histplot(
            data=sample,
            x='artist_followers',
            bins=40,
            color=SPOTIFY['secondary'],
            ax=axes[1, 0],
            log_scale=True          # Escala logarítmica en X
        )
        
        # Rugplot: muestra cada punto como una línea vertical pequeña
        sns.rugplot(
            data=sample,
            x='artist_followers',
            color='red',
            alpha=0.3,
            ax=axes[1, 0]
        )
        
        axes[1, 0].set_title(
            'Distribución de Seguidores (escala logarítmica)',
            fontsize=12,
            fontweight='bold'
        )
        axes[1, 0].set_xlabel('Seguidores (log scale)')
        axes[1, 0].set_ylabel('Frecuencia')
        
        # === HISTOGRAMA 4: CANCIONES POR AÑO ===
        
        # Filtrar años recientes
        df_recent = self.data[self.data['year'] >= 2020]
        
        if len(df_recent) > 0:
            sns.histplot(
                data=df_recent,
                x='year',
                bins=len(df_recent['year'].unique()),  # Una barra por año
                color=SPOTIFY['gray'],
                ax=axes[1, 1],
                discrete=True,           # Valores discretos (años)
                shrink=0.8              # Reducir ancho de barras
            )
            
            axes[1, 1].set_title(
                'Canciones por Año (2020 en adelante)',
                fontsize=12,
                fontweight='bold'
            )
            axes[1, 1].set_xlabel('Año')
            axes[1, 1].set_ylabel('Cantidad de Canciones')
            axes[1, 1].tick_params(axis='x', rotation=45)
        
        # === ANOTACIONES ESTADÍSTICAS ===
        
        # Añadir grid en cada gráfico
        for ax in axes.flat:
            ax.grid(axis='y', alpha=0.3, linestyle='--')


def histograms(data):
    """
    Función helper para generar histogramas
    
    Args:
        data: DataFrame con datos de Spotify
    """
    plot = Histogramas(data)
    plot.generate()