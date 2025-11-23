"""
🎯 GRÁFICO 7: GRÁFICO DE RADAR (SPIDER CHART)
============================================

📋 DESCRIPCIÓN:
Gráfico circular que compara múltiples métricas simultáneamente.
Ideal para comparar perfiles completos de diferentes entidades.

🎯 OBJETIVO:
Comparar múltiples dimensiones a la vez:
- Visualizar perfiles multidimensionales
- Comparar artistas en varias métricas
- Identificar fortalezas y debilidades
- Benchmarking visual

📊 DATOS QUE VISUALIZA:
- Top 5 artistas en 5 métricas:
  1. Popularidad del artista
  2. Seguidores (normalizado)
  3. Popularidad promedio de tracks
  4. Duración promedio (normalizado)
  5. Cantidad de canciones (normalizado)

🎨 ELEMENTOS VISUALES:
- Polígonos superpuestos (uno por artista)
- Ejes radiales (uno por métrica)
- Relleno con transparencia
- Leyenda de colores

💡 CUÁNDO USAR:
- Comparar perfiles completos
- Evaluación de competidores
- Análisis de habilidades/competencias
- Dashboards ejecutivos

Autores: Anthony (@AnThony69x), Emilio (@EmilioSle)
Universidad: ULEAM - Visualización de Datos
Fecha: 2025-11-23
"""

import matplotlib.pyplot as plt
import numpy as np
from math import pi
from .base import BasePlot
from ..config.colors import get_palette

class GraficoRadar(BasePlot):
    
    def __init__(self, data):
        super().__init__(
            data=data,
            title='🎯 Gráfico de Radar - Comparación Multidimensional\nTop 5 Artistas',
            filename='07_radar'
        )
    
    def create(self):
        """Crea el gráfico de radar"""
        
        # Seleccionar top 5 artistas por popularidad
        top_artists = (self.data
                      .nlargest(5, 'artist_popularity')
                      ['artist_name']
                      .unique()[:5])
        
        # Categorías a comparar
        categorias = [
            'Popularidad\nArtista',
            'Seguidores\n(norm)',
            'Popularidad\nTracks',
            'Duración\nPromedio',
            'Cantidad\nCanciones'
        ]
        
        # Crear figura con proyección polar
        self.fig, ax = plt.subplots(
            figsize=(10, 10),
            subplot_kw=dict(projection='polar')
        )
        
        # Calcular ángulos para cada eje (en radianes)
        num_vars = len(categorias)
        angulos = [n / num_vars * 2 * pi for n in range(num_vars)]
        angulos += angulos[:1]  # Cerrar el polígono
        
        # Colores para cada artista
        colores = get_palette('categorical', 5)
        
        # Para cada artista, calcular valores y graficar
        for i, artist in enumerate(top_artists):
            artist_data = self.data[self.data['artist_name'] == artist]
            
            if len(artist_data) == 0:
                continue
            
            # Calcular métricas (normalizar a escala 0-100)
            valores = [
                artist_data['artist_popularity'].mean(),
                (artist_data['artist_followers'].mean() / self.data['artist_followers'].max()) * 100,
                artist_data['track_popularity'].mean(),
                (artist_data['track_duration_min'].mean() / self.data['track_duration_min'].max()) * 100,
                (len(artist_data) / self.data['artist_name'].value_counts().max()) * 100
            ]
            
            # Cerrar el polígono (repetir primer valor)
            valores += valores[:1]
            
            # Graficar línea
            ax.plot(
                angulos, 
                valores, 
                'o-', 
                linewidth=2,
                label=artist, 
                color=colores[i]
            )
            
            # Rellenar área
            ax.fill(
                angulos, 
                valores, 
                alpha=0.15, 
                color=colores[i]
            )
        
        # === PERSONALIZACIÓN ===
        
        # Etiquetas de ejes
        ax.set_xticks(angulos[:-1])
        ax.set_xticklabels(categorias, size=10)
        
        # Límites radiales
        ax.set_ylim(0, 100)
        
        # Título
        ax.set_title(
            self.title,
            fontsize=14,
            fontweight='bold',
            pad=20,
            y=1.08
        )
        
        # Leyenda
        ax.legend(
            loc='upper right',
            bbox_to_anchor=(1.3, 1.1),
            fontsize=10
        )
        
        # Grid
        ax.grid(True, linestyle='--', alpha=0.7)
        
        # Líneas de referencia (cada 25%)
        ax.set_yticks([25, 50, 75, 100])
        ax.set_yticklabels(['25', '50', '75', '100'], size=8)


def radar_chart(data):
    """
    Función helper para generar gráfico de radar
    
    Args:
        data: DataFrame con datos de Spotify
    """
    plot = GraficoRadar(data)
    plot.generate()