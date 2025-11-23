"""
💧 GRÁFICO 8: GRÁFICO DE CASCADA (WATERFALL CHART)
=================================================

📋 DESCRIPCIÓN:
Muestra cambios acumulativos a lo largo del tiempo o categorías.
Visualiza incrementos y decrementos de forma secuencial.

🎯 OBJETIVO:
Analizar cambios temporales o secuenciales:
- Visualizar evolución temporal
- Mostrar contribuciones individuales al total
- Identificar periodos de crecimiento/decrecimiento
- Análisis de tendencias

📊 DATOS QUE VISUALIZA:
- Evolución de canciones por año (desde 2015)
- Cambios incrementales año a año
- Acumulación temporal

🎨 ELEMENTOS VISUALES:
- Barras flotantes (verde = incremento, rojo = decremento)
- Líneas conectoras entre periodos
- Etiquetas con valores de cambio
- Colores según signo del cambio

💡 CUÁNDO USAR:
- Análisis de series temporales
- Reportes financieros (ingresos, gastos)
- Evolución de métricas en el tiempo
- Contribución de componentes al total

Autores: Anthony (@AnThony69x), Emilio (@EmilioSle)
Universidad: ULEAM - Visualización de Datos
Fecha: 2025-11-23
"""

import matplotlib.pyplot as plt
import numpy as np
from .base import BasePlot
from ..config.colors import SPOTIFY

class GraficoCascada(BasePlot):
    
    def __init__(self, data):
        super().__init__(
            data=data,
            title='💧 Gráfico de Cascada - Evolución de Canciones por Año',
            filename='08_cascada'
        )
    
    def create(self):
        """Crea el gráfico de cascada"""
        
        # Filtrar años válidos y recientes (desde 2015)
        df_years = (self.data[self.data['year'] >= 2015]
                   .groupby('year')
                   .size()
                   .reset_index(name='count')
                   .sort_values('year'))
        
        if len(df_years) == 0:
            # Si no hay datos, crear gráfico vacío con mensaje
            self.fig, ax = plt.subplots(figsize=(14, 7))
            ax.text(0.5, 0.5, 'No hay datos suficientes para el gráfico de cascada',
                   ha='center', va='center', fontsize=14)
            return
        
        # Calcular cambios año a año
        df_years['change'] = df_years['count'].diff()
        df_years.loc[df_years.index[0], 'change'] = df_years.loc[df_years.index[0], 'count']
        
        # Crear figura
        self.fig, ax = plt.subplots(figsize=(14, 7))
        
        # Posición acumulada para las barras flotantes
        cumulative = 0
        x_pos = range(len(df_years))
        
        # Para cada año, dibujar barra y conector
        for i, (idx, row) in enumerate(df_years.iterrows()):
            year = int(row['year'])
            change = row['change']
            
            # Color según signo del cambio
            color = SPOTIFY['primary'] if change >= 0 else '#FF6B6B'
            
            # Dibujar barra
            bottom = cumulative if i > 0 else 0
            ax.bar(
                i, 
                abs(change),
                bottom=bottom,
                color=color,
                edgecolor='black',
                linewidth=1.5,
                alpha=0.7
            )
            
            # Línea conectora al siguiente periodo
            if i < len(df_years) - 1:
                next_cumulative = cumulative + change
                ax.plot(
                    [i + 0.4, i + 0.6],
                    [cumulative + change, cumulative + change],
                    color='black',
                    linewidth=2,
                    linestyle='--'
                )
            
            # Etiqueta con el valor del cambio
            label_y = cumulative + change/2
            sign = '+' if change > 0 else ''
            ax.text(
                i,
                label_y,
                f'{sign}{int(change)}',
                ha='center',
                va='center',
                fontsize=10,
                fontweight='bold',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8)
            )
            
            # Actualizar acumulado
            cumulative += change
        
        # === PERSONALIZACIÓN ===
        
        ax.set_xticks(x_pos)
        ax.set_xticklabels([int(y) for y in df_years['year']])
        ax.set_xlabel('Año', fontsize=12, fontweight='bold')
        ax.set_ylabel('Cambio en Canciones', fontsize=12, fontweight='bold')
        
        ax.set_title(
            self.title,
            fontsize=14,
            fontweight='bold',
            pad=20
        )
        
        # Grid
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        
        # Línea en y=0
        ax.axhline(y=0, color='black', linewidth=1, alpha=0.5)
        
        # Leyenda
        from matplotlib.patches import Patch
        legend_elements = [
            Patch(facecolor=SPOTIFY['primary'], label='Incremento'),
            Patch(facecolor='#FF6B6B', label='Decremento')
        ]
        ax.legend(handles=legend_elements, loc='upper left')


def waterfall_chart(data):
    """
    Función helper para generar gráfico de cascada
    
    Args:
        data: DataFrame con datos de Spotify
    """
    plot = GraficoCascada(data)
    plot.generate()