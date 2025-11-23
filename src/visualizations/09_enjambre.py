"""
🐝 GRÁFICO 9: GRÁFICO DE ENJAMBRE (SWARMPLOT)
============================================

📋 DESCRIPCIÓN:
Muestra todos los puntos de datos sin superposición, creando un efecto de "enjambre".
Similar al scatter pero evita que los puntos se solapen.

🎯 OBJETIVO:
Visualizar distribuciones mostrando cada punto individual:
- Mostrar todos los datos sin pérdida de información
- Evitar superposición de puntos
- Comparar distribuciones entre categorías
- Detectar patrones en datos pequeños/medianos

📊 DATOS QUE VISUALIZA:
1. Popularidad por contenido explícito (muestra de 500)
2. Duración por tipo de álbum con violinplot (muestra de 400)

🎨 ELEMENTOS VISUALES:
- Puntos distribuidos sin superposición
- Swarmplot básico
- Combinación violinplot + swarmplot

💡 CUÁNDO USAR:
- Datasets pequeños/medianos (< 1000 puntos)
- Cuando cada punto importa individualmente
- Para ver distribución completa de datos
- Combinado con boxplot o violinplot

⚠️ LIMITACIONES:
- No escala bien con datasets grandes
- Computacionalmente intensivo

Autores: Anthony (@AnThony69x), Emilio (@EmilioSle)
Universidad: ULEAM - Visualización de Datos
Fecha: 2025-11-23
"""

import matplotlib.pyplot as plt
import seaborn as sns
from .base import BasePlot
from ..config.colors import EXPLICIT, SPOTIFY

class GraficoEnjambre(BasePlot):
    
    def __init__(self, data):
        super().__init__(
            data=data,
            title='🐝 Gráfico de Enjambre - Distribución de Puntos',
            filename='09_enjambre'
        )
    
    def create(self):
        """Crea los gráficos de enjambre"""
        
        # Crear figura con 2 subplots
        self.fig, axes = plt.subplots(1, 2, figsize=(16, 6))
        
        # === SWARMPLOT 1: BÁSICO ===
        
        # Tomar muestra para rendimiento
        sample_data = self.data.sample(min(500, len(self.data)))
        
        sns.swarmplot(
            data=sample_data,
            x='explicit',
            y='track_popularity',
            palette=[EXPLICIT[False], EXPLICIT[True]],
            ax=axes[0],
            size=4,
            alpha=0.7
        )
        
        axes[0].set_title(
            'Popularidad por Contenido Explícito\n(Swarmplot)',
            fontsize=12,
            fontweight='bold'
        )
        axes[0].set_xticklabels(['No Explícito', 'Explícito'])
        axes[0].set_xlabel('Tipo de Contenido', fontsize=11)
        axes[0].set_ylabel('Popularidad', fontsize=11)
        axes[0].grid(axis='y', alpha=0.3, linestyle='--')
        
        # Añadir línea de mediana
        medians = sample_data.groupby('explicit')['track_popularity'].median()
        for i, (explicit, median) in enumerate(medians.items()):
            axes[0].hlines(
                median, i - 0.4, i + 0.4,
                colors='red', linewidth=2,
                label='Mediana' if i == 0 else ''
            )
        axes[0].legend()
        
        # === SWARMPLOT 2: COMBINADO CON VIOLINPLOT ===
        
        # Obtener top 3 tipos de álbum
        top_types = self.data['album_type'].value_counts().head(3).index
        df_types = self.data[self.data['album_type'].isin(top_types)].sample(min(400, len(self.data)))
        
        if len(df_types) > 0:
            # Primero violinplot de fondo
            sns.violinplot(
                data=df_types,
                x='album_type',
                y='track_duration_min',
                palette='muted',
                ax=axes[1],
                inner=None,  # Sin elementos internos
                alpha=0.5
            )
            
            # Luego swarmplot encima
            sns.swarmplot(
                data=df_types,
                x='album_type',
                y='track_duration_min',
                color='black',
                ax=axes[1],
                size=2,
                alpha=0.5
            )
            
            axes[1].set_title(
                'Duración por Tipo de Álbum\n(Violin + Swarm)',
                fontsize=12,
                fontweight='bold'
            )
            axes[1].set_xlabel('Tipo de Álbum', fontsize=11)
            axes[1].set_ylabel('Duración (minutos)', fontsize=11)
            axes[1].tick_params(axis='x', rotation=15)
            axes[1].grid(axis='y', alpha=0.3, linestyle='--')


def swarm_plot(data):
    """
    Función helper para generar gráfico de enjambre
    
    Args:
        data: DataFrame con datos de Spotify
    """
    plot = GraficoEnjambre(data)
    plot.generate()