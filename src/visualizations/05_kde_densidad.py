"""
📈 GRÁFICO 5: GRÁFICOS DE DENSIDAD KDE
=====================================

📋 DESCRIPCIÓN:
Estimación de densidad kernel (KDE) para visualizar distribuciones suaves.
Incluye densidad univariada, bivariada y comparaciones por categorías.

🎯 OBJETIVO:
Visualizar distribuciones de probabilidad de forma suave:
- Estimar la función de densidad de probabilidad
- Comparar distribuciones entre grupos
- Visualizar relaciones bivariadas (2D)
- Identificar modas y concentraciones de datos

📊 DATOS QUE VISUALIZA:
1. Densidad de popularidad (univariada)
2. Densidad de duración por contenido explícito
3. Densidad bivariada: duración vs popularidad
4. Scatter + KDE: seguidores vs popularidad

🎨 ELEMENTOS VISUALES:
- Curvas KDE suaves
- KDE con relleno (fill)
- Contornos de densidad 2D
- Combinación scatter + KDE

💡 CUÁNDO USAR:
- Visualizar distribuciones suaves sin histogramas
- Comparar distribuciones de grupos
- Análisis de densidad bidimensional
- Cuando necesitas una visualización continua

Autores: Anthony (@AnThony69x), Emilio (@EmilioSle)
Universidad: ULEAM - Visualización de Datos
Fecha: 2025-11-23
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from .base import BasePlot
from ..config.colors import SPOTIFY, EXPLICIT

class KDEDensidad(BasePlot):
    
    def __init__(self, data):
        super().__init__(
            data=data,
            title='📈 Análisis de Densidad - Estimación Kernel (KDE)',
            filename='05_kde_densidad'
        )
    
    def create(self):
        """Crea los gráficos KDE"""
        
        # Crear figura con 4 subplots (2x2)
        self.fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        
        # === KDE 1: DENSIDAD SIMPLE ===
        
        sns.kdeplot(
            data=self.data, 
            x='track_popularity', 
            fill=True,
            color=SPOTIFY['primary'], 
            ax=axes[0, 0], 
            linewidth=2
        )
        
        axes[0, 0].set_title(
            'Densidad de Popularidad (KDE)',
            fontsize=12,
            fontweight='bold'
        )
        axes[0, 0].set_xlabel('Popularidad')
        axes[0, 0].set_ylabel('Densidad')
        
        # Añadir línea vertical en la media
        media = self.data['track_popularity'].mean()
        axes[0, 0].axvline(media, color='red', linestyle='--', 
                          linewidth=2, label=f'Media: {media:.1f}')
        axes[0, 0].legend()
        
        # === KDE 2: COMPARACIÓN POR CATEGORÍA ===
        
        sns.kdeplot(
            data=self.data, 
            x='track_duration_min', 
            hue='explicit',
            fill=True, 
            palette=[EXPLICIT[False], EXPLICIT[True]],
            ax=axes[0, 1], 
            alpha=0.5, 
            linewidth=2
        )
        
        axes[0, 1].set_title(
            'Densidad de Duración por Contenido',
            fontsize=12,
            fontweight='bold'
        )
        axes[0, 1].set_xlabel('Duración (minutos)')
        axes[0, 1].set_ylabel('Densidad')
        axes[0, 1].legend(title='Contenido', labels=['No Explícito', 'Explícito'])
        
        # === KDE 3: DENSIDAD BIVARIADA (2D) ===
        
        # Tomar muestra para mejor rendimiento
        sample = self.data.sample(min(1000, len(self.data)))
        sample_filtered = sample[
            (sample['track_duration_min'] > 0) & 
            (sample['track_popularity'] > 0)
        ]
        
        try:
            sns.kdeplot(
                data=sample_filtered, 
                x='track_duration_min', 
                y='track_popularity',
                fill=True, 
                cmap='Greens', 
                ax=axes[1, 0],
                thresh=0.05, 
                levels=10,
                warn_singular=False
            )
            
            axes[1, 0].set_title(
                'Densidad 2D: Duración vs Popularidad',
                fontsize=12,
                fontweight='bold'
            )
            axes[1, 0].set_xlabel('Duración (minutos)')
            axes[1, 0].set_ylabel('Popularidad')
            
        except (ValueError, np.linalg.LinAlgError):
            # Si falla el KDE, hacer scatter
            axes[1, 0].scatter(
                sample_filtered['track_duration_min'],
                sample_filtered['track_popularity'],
                alpha=0.3, color=SPOTIFY['primary'], s=20
            )
            axes[1, 0].set_title(
                'Scatter: Duración vs Popularidad',
                fontsize=12,
                fontweight='bold'
            )
            axes[1, 0].set_xlabel('Duración (minutos)')
            axes[1, 0].set_ylabel('Popularidad')
        
        # === KDE 4: SCATTER + KDE MARGINAL ===
        
        sample2 = self.data.sample(min(500, len(self.data)))
        sample2_filtered = sample2[
            (sample2['artist_followers'] > 0) &
            (sample2['artist_popularity'] > 0) &
            (sample2['artist_followers'] < sample2['artist_followers'].quantile(0.99))
        ]
        
        if len(sample2_filtered) > 50:
            # Scatter
            sns.scatterplot(
                data=sample2_filtered, 
                x='artist_followers', 
                y='artist_popularity',
                hue='explicit', 
                palette=[EXPLICIT[False], EXPLICIT[True]],
                ax=axes[1, 1], 
                alpha=0.6, 
                s=50
            )
            
            # Intentar KDE superpuesto
            try:
                if (sample2_filtered['artist_followers'].nunique() > 10 and 
                    sample2_filtered['artist_popularity'].nunique() > 10):
                    
                    sns.kdeplot(
                        data=sample2_filtered,
                        x='artist_followers',
                        y='artist_popularity',
                        ax=axes[1, 1],
                        levels=3,
                        color='black',
                        linewidths=1.5,
                        alpha=0.5,
                        warn_singular=False
                    )
            except:
                pass  # Si falla, solo mostrar scatter
            
            axes[1, 1].set_xscale('log')
            axes[1, 1].set_title(
                'Seguidores vs Popularidad (scatter + KDE)',
                fontsize=12,
                fontweight='bold'
            )
            axes[1, 1].set_xlabel('Seguidores (log scale)')
            axes[1, 1].set_ylabel('Popularidad')
            axes[1, 1].legend(title='Contenido', labels=['No Explícito', 'Explícito'])
        
        # === AÑADIR GRID ===
        
        for ax in axes.flat:
            ax.grid(alpha=0.3, linestyle='--')


def kde_plots(data):
    """
    Función helper para generar gráficos KDE
    
    Args:
        data: DataFrame con datos de Spotify
    """
    plot = KDEDensidad(data)
    plot.generate()