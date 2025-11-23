"""
📉 GRÁFICO 6: GRÁFICO DE PARETO (PRINCIPIO 80/20)
================================================

📋 DESCRIPCIÓN:
Gráfico de barras combinado con línea acumulada que muestra el principio de Pareto:
el 80% del efecto proviene del 20% de las causas.

🎯 OBJETIVO:
Identificar los elementos más importantes:
- Visualizar el principio 80/20
- Identificar los "pocos vitales" vs "muchos triviales"
- Priorizar recursos y esfuerzos
- Análisis de concentración

📊 DATOS QUE VISUALIZA:
- Top 20 artistas con más canciones
- Porcentaje acumulado de canciones
- Línea del 80% como referencia

🎨 ELEMENTOS VISUALES:
- Barras verticales (cantidad por artista)
- Línea de porcentaje acumulado
- Doble eje Y (cantidad + porcentaje)
- Línea de referencia al 80%

💡 CUÁNDO USAR:
- Análisis de concentración (ej: 80% ventas = 20% clientes)
- Priorización de problemas/causas
- Optimización de recursos
- Control de calidad (defectos)

Autores: Anthony (@AnThony69x), Emilio (@EmilioSle)
Universidad: ULEAM - Visualización de Datos
Fecha: 2025-11-23
"""

import matplotlib.pyplot as plt
import seaborn as sns
from .base import BasePlot
from ..config.colors import SPOTIFY

class GraficoPareto(BasePlot):
    
    def __init__(self, data):
        super().__init__(
            data=data,
            title='📉 Gráfico de Pareto - Canciones por Artista\nPrincipio 80/20',
            filename='06_pareto'
        )
    
    def create(self):
        """Crea el gráfico de Pareto"""
        
        # Contar canciones por artista (top 20)
        artist_counts = (self.data['artist_name']
                        .value_counts()
                        .head(20)
                        .sort_values(ascending=False))
        
        # Calcular porcentaje acumulado
        cumsum = artist_counts.cumsum()
        cumsum_pct = 100 * cumsum / cumsum.iloc[-1]
        
        # Crear figura con un eje
        self.fig, ax1 = plt.subplots(figsize=(14, 7))
        
        # === BARRAS (Eje izquierdo) ===
        
        ax1.bar(
            range(len(artist_counts)), 
            artist_counts.values,
            color=SPOTIFY['primary'], 
            edgecolor='black', 
            linewidth=1.5, 
            alpha=0.7,
            label='Cantidad de Canciones'
        )
        
        ax1.set_xlabel('Artistas', fontsize=12, fontweight='bold')
        ax1.set_ylabel(
            'Número de Canciones', 
            fontsize=12, 
            fontweight='bold', 
            color=SPOTIFY['primary']
        )
        ax1.set_xticks(range(len(artist_counts)))
        ax1.set_xticklabels(
            artist_counts.index, 
            rotation=45, 
            ha='right',
            fontsize=9
        )
        ax1.tick_params(axis='y', labelcolor=SPOTIFY['primary'])
        
        # === LÍNEA ACUMULADA (Eje derecho) ===
        
        ax2 = ax1.twinx()
        ax2.plot(
            range(len(artist_counts)), 
            cumsum_pct.values,
            color='#FF6B6B', 
            marker='o', 
            linewidth=3, 
            markersize=8,
            label='% Acumulado'
        )
        
        ax2.set_ylabel(
            'Porcentaje Acumulado (%)', 
            fontsize=12, 
            fontweight='bold', 
            color='#FF6B6B'
        )
        ax2.tick_params(axis='y', labelcolor='#FF6B6B')
        ax2.set_ylim(0, 105)
        
        # === LÍNEA DEL 80% ===
        
        ax2.axhline(
            y=80, 
            color='red', 
            linestyle='--', 
            linewidth=2,
            label='Línea 80%'
        )
        
        # Leyenda
        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax2.legend(lines1 + lines2, labels1 + labels2, loc='lower right')
        
        # Grid
        ax1.grid(axis='y', alpha=0.3, linestyle='--')
        
        # Título
        ax1.set_title(
            self.title,
            fontsize=14,
            fontweight='bold',
            pad=20
        )
        
        # Anotación explicativa
        # Encontrar en qué punto se cruza el 80%
        idx_80 = (cumsum_pct >= 80).idxmax()
        pos_80 = list(artist_counts.index).index(idx_80)
        
        ax2.annotate(
            f'80% de canciones\nalcanzado en {pos_80+1} artistas',
            xy=(pos_80, 80),
            xytext=(pos_80 + 3, 70),
            arrowprops=dict(arrowstyle='->', color='red', lw=2),
            fontsize=10,
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8)
        )


def pareto_chart(data):
    """
    Función helper para generar gráfico de Pareto
    
    Args:
        data: DataFrame con datos de Spotify
    """
    plot = GraficoPareto(data)
    plot.generate()