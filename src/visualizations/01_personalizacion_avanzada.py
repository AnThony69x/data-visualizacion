"""
🎨 GRÁFICO 1: PERSONALIZACIÓN AVANZADA
======================================

📋 DESCRIPCIÓN:
Gráfico de barras VERTICALES mostrando los artistas más populares
con personalización completa de ejes, colores, etiquetas y estilos.

📊 DATOS QUE VISUALIZA:
- Top 15 artistas por popularidad
- Eje X: Artistas
- Eje Y: Popularidad (0-100)

Autores: Anthony (@AnThony69x), Emilio (@EmilioSle)
Universidad: ULEAM - Visualización de Datos
Fecha: 2025-11-23
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from .base import BasePlot
from ..config.colors import SPOTIFY

class PersonalizacionAvanzada(BasePlot):
    
    def __init__(self, data):
        super().__init__(
            data=data,
            title='🎵 Top 15 Artistas Más Populares en Spotify\nPersonalización Avanzada',
            filename='01_personalizacion_avanzada',
            figsize=(14, 8)
        )
    
    def create(self):
        """Crea el gráfico de personalización avanzada"""
        
        # === PREPARAR DATOS: Top 15 artistas únicos ===
        
        # Agrupar por artista y tomar la popularidad máxima
        artist_popularity = (self.data
                            .groupby('artist_name')['artist_popularity']
                            .max()
                            .reset_index()
                            .nlargest(15, 'artist_popularity')
                            .reset_index(drop=True))
        
        print(f"📊 Mostrando {len(artist_popularity)} artistas")  # Debug
        
        # Crear figura
        self.fig, ax = plt.subplots(figsize=self.figsize)
        
        # Crear paleta de colores degradada
        colors = sns.color_palette('viridis', len(artist_popularity))
        
        # === CREAR GRÁFICO DE BARRAS VERTICALES ===
        
        x_positions = range(len(artist_popularity))
        bars = ax.bar(
            x_positions,
            artist_popularity['artist_popularity'].values,
            color=colors,
            edgecolor='black',
            linewidth=1.5,
            alpha=0.85,
            width=0.7
        )
        
        # === PERSONALIZACIÓN DE EJES ===
        
        # Eje X (Artistas)
        ax.set_xlabel(
            'Artistas', 
            fontsize=14, 
            fontweight='bold', 
            color=SPOTIFY['primary'],
            labelpad=10
        )
        
        # Eje Y (Popularidad)
        ax.set_ylabel(
            'Nivel de Popularidad (0-100)', 
            fontsize=14, 
            fontweight='bold', 
            color=SPOTIFY['primary'],
            labelpad=10
        )
        
        # === ETIQUETAS DEL EJE X (ARTISTAS) ===
        
        ax.set_xticks(x_positions)
        ax.set_xticklabels(
            artist_popularity['artist_name'].values,
            rotation=45,
            ha='right',
            fontsize=9
        )
        
        # === PERSONALIZACIÓN DE TICKS ===
        
        ax.tick_params(
            axis='x',
            labelsize=9,
            colors=SPOTIFY['gray'],
            width=1.5,
            length=5
        )
        
        ax.tick_params(
            axis='y',
            labelsize=10,
            colors=SPOTIFY['gray'],
            width=1.5,
            length=5
        )
        
        # === LÍMITES Y GRID ===
        
        # Límites del eje Y
        ax.set_ylim(0, 105)
        
        # Grid horizontal
        ax.grid(
            axis='y',
            alpha=0.3,
            linestyle='--',
            linewidth=1,
            zorder=0
        )
        
        # Quitar grid vertical
        ax.grid(axis='x', visible=False)
        
        # === AÑADIR VALORES ENCIMA DE LAS BARRAS ===
        
        for i, (bar, value) in enumerate(zip(bars, artist_popularity['artist_popularity'].values)):
            height = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width()/2,
                height + 1.5,
                f'{value:.0f}',
                ha='center',
                va='bottom',
                fontsize=9,
                fontweight='bold',
                color=SPOTIFY['dark']
            )
        
        # === PERSONALIZACIÓN DE SPINES (BORDES) ===
        
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_linewidth(2)
        ax.spines['left'].set_color(SPOTIFY['gray'])
        ax.spines['bottom'].set_linewidth(2)
        ax.spines['bottom'].set_color(SPOTIFY['gray'])
        
        # === LÍNEA DE REFERENCIA (PROMEDIO) ===
        
        promedio = artist_popularity['artist_popularity'].mean()
        ax.axhline(
            y=promedio,
            color='red',
            linestyle='--',
            linewidth=2,
            alpha=0.6,
            label=f'Promedio: {promedio:.1f}'
        )
        
        # === LEYENDA ===
        
        ax.legend(
            loc='upper left',
            fontsize=10,
            frameon=True,
            shadow=True
        )
        
        # === TÍTULO ===
        
        ax.set_title(
            self.title,
            fontsize=15,
            fontweight='bold',
            pad=20,
            color=SPOTIFY['dark']
        )
        
        # === ANOTACIÓN DEL MÁS POPULAR ===
        
        max_idx = artist_popularity['artist_popularity'].idxmax()
        max_artist = artist_popularity.loc[max_idx, 'artist_name']
        max_value = artist_popularity.loc[max_idx, 'artist_popularity']
        
        ax.annotate(
            f'🏆 Más popular:\n{max_artist}\n({max_value:.0f} puntos)',
            xy=(max_idx, max_value),
            xytext=(max_idx - 2, max_value - 12),
            arrowprops=dict(
                arrowstyle='->',
                color=SPOTIFY['primary'],
                lw=2,
                connectionstyle='arc3,rad=0.3'
            ),
            fontsize=9,
            bbox=dict(
                boxstyle='round,pad=0.6',
                facecolor='yellow',
                alpha=0.8,
                edgecolor=SPOTIFY['primary'],
                linewidth=2
            ),
            ha='center',
            va='top'
        )
        
        # === AJUSTE FINAL ===
        
        self.fig.tight_layout()


def personalization_advanced(data):
    """
    Función helper para generar el gráfico
    
    Args:
        data: DataFrame con datos de Spotify
    """
    plot = PersonalizacionAvanzada(data)
    plot.generate()